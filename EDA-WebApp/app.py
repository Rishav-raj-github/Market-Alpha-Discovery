"""
EDA Automation Web Application
A Flask-based web application for comprehensive Exploratory Data Analysis

Author: Rishav Raj
GitHub: @Rishav-raj-github
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from werkzeug.utils import secure_filename
from sklearn.ensemble import RandomForestRegressor, IsolationForest
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import mutual_info_regression
import warnings
import json
import base64
from io import BytesIO
import PyPDF2
from openpyxl import load_workbook

warnings.filterwarnings('ignore')

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size

# Allowed file extensions
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls', 'pdf'}

# Create upload directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    """Check if uploaded file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def load_data(file_path):
    """Load data from various file formats"""
    try:
        file_ext = file_path.rsplit('.', 1)[1].lower()
        
        if file_ext == 'csv':
            df = pd.read_csv(file_path)
        elif file_ext in ['xlsx', 'xls']:
            df = pd.read_excel(file_path)
        elif file_ext == 'pdf':
            # Basic PDF text extraction (simplified)
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text()
                # Create a simple dataframe from extracted text
                lines = text.split('\n')
                df = pd.DataFrame({'text': lines})
        
        return df
    except Exception as e:
        raise Exception(f"Error loading file: {str(e)}")

def get_basic_info(df):
    """Get basic information about the dataset"""
    info = {
        'shape': df.shape,
        'columns': list(df.columns),
        'dtypes': df.dtypes.to_dict(),
        'memory_usage': df.memory_usage(deep=True).sum(),
        'null_counts': df.isnull().sum().to_dict(),
        'null_percentage': (df.isnull().sum() / len(df) * 100).to_dict()
    }
    return info

def get_descriptive_stats(df):
    """Get descriptive statistics for numerical columns"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 0:
        return df[numeric_cols].describe().to_dict()
    return {}

def detect_outliers(df, method='iqr'):
    """Detect outliers using various methods"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    outliers = {}
    
    for col in numeric_cols:
        if method == 'iqr':
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers[col] = df[(df[col] < lower_bound) | (df[col] > upper_bound)].index.tolist()
        
        elif method == 'zscore':
            z_scores = np.abs((df[col] - df[col].mean()) / df[col].std())
            outliers[col] = df[z_scores > 3].index.tolist()
    
    return outliers

def create_visualizations(df, viz_type):
    """Create various visualizations"""
    plots = []
    
    if viz_type == 'distribution':
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols[:5]:  # Limit to first 5 columns
            fig = px.histogram(df, x=col, title=f'Distribution of {col}')
            plots.append({
                'title': f'Distribution of {col}',
                'plot': fig.to_json()
            })
    
    elif viz_type == 'correlation':
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        if len(numeric_cols) > 1:
            corr_matrix = df[numeric_cols].corr()
            fig = px.imshow(corr_matrix, 
                          title='Correlation Matrix',
                          color_continuous_scale='RdBu_r')
            plots.append({
                'title': 'Correlation Matrix',
                'plot': fig.to_json()
            })
    
    elif viz_type == 'boxplot':
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols[:5]:  # Limit to first 5 columns
            fig = px.box(df, y=col, title=f'Box Plot of {col}')
            plots.append({
                'title': f'Box Plot of {col}',
                'plot': fig.to_json()
            })
    
    return plots

def calculate_feature_importance(df, target_col=None):
    """Calculate feature importance using various methods"""
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if len(numeric_cols) < 2:
        return {}
    
    # Correlation-based importance
    corr_importance = {}
    if target_col and target_col in numeric_cols:
        correlations = df[numeric_cols].corr()[target_col].abs().sort_values(ascending=False)
        corr_importance = correlations.to_dict()
    
    # Random Forest importance (if enough data)
    rf_importance = {}
    if len(df) > 10 and len(numeric_cols) > 1:
        try:
            X = df[numeric_cols].fillna(df[numeric_cols].mean())
            if target_col and target_col in numeric_cols:
                y = X[target_col]
                X = X.drop(target_col, axis=1)
            else:
                # Use first column as target
                y = X.iloc[:, 0]
                X = X.iloc[:, 1:]
            
            if len(X.columns) > 0:
                rf = RandomForestRegressor(n_estimators=50, random_state=42)
                rf.fit(X, y)
                rf_importance = dict(zip(X.columns, rf.feature_importances_))
        except:
            pass
    
    return {
        'correlation_importance': corr_importance,
        'random_forest_importance': rf_importance
    }

@app.route('/')
def index():
    """Home page with file upload interface"""
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    if 'file' not in request.files:
        flash('No file selected')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        try:
            # Load and process data
            df = load_data(file_path)
            
            # Store basic info in session or pass to template
            basic_info = get_basic_info(df)
            
            return render_template('analysis.html', 
                                 filename=filename,
                                 basic_info=basic_info)
        except Exception as e:
            flash(f'Error processing file: {str(e)}')
            return redirect(url_for('index'))
    else:
        flash('Invalid file format. Please upload CSV, Excel, or PDF files.')
        return redirect(url_for('index'))

@app.route('/analyze/<filename>/<analysis_type>')
def analyze(filename, analysis_type):
    """Perform specific analysis on uploaded data"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        df = load_data(file_path)
        result = {}
        
        if analysis_type == 'summary':
            result = {
                'basic_info': get_basic_info(df),
                'descriptive_stats': get_descriptive_stats(df)
            }
        
        elif analysis_type == 'nulls':
            null_info = {
                'null_counts': df.isnull().sum().to_dict(),
                'null_percentage': (df.isnull().sum() / len(df) * 100).to_dict(),
                'total_nulls': df.isnull().sum().sum()
            }
            result = null_info
        
        elif analysis_type == 'visualizations':
            viz_type = request.args.get('viz_type', 'distribution')
            plots = create_visualizations(df, viz_type)
            result = {'plots': plots}
        
        elif analysis_type == 'outliers':
            method = request.args.get('method', 'iqr')
            outliers = detect_outliers(df, method)
            result = {'outliers': outliers}
        
        elif analysis_type == 'feature_importance':
            target_col = request.args.get('target_col')
            importance = calculate_feature_importance(df, target_col)
            result = importance
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_columns/<filename>')
def get_columns(filename):
    """Get column names for dropdown menus"""
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    try:
        df = load_data(file_path)
        columns = {
            'all_columns': list(df.columns),
            'numeric_columns': list(df.select_dtypes(include=[np.number]).columns),
            'categorical_columns': list(df.select_dtypes(include=['object']).columns)
        }
        return jsonify(columns)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

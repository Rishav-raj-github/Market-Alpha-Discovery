# 🌐 **EDA Web Application - Access Now!**

## **💻 Local Website Link:** 
### **[http://localhost:5000](http://localhost:5000)**

*Start the app by running `python app.py` and visit the link above to begin your data analysis journey!*

---

# EDA Automation Web Application

## Overview
A professional Exploratory Data Analysis (EDA) web application built with Flask that provides comprehensive data analysis capabilities through an intuitive dropdown-driven interface. This application enables users to perform advanced statistical analysis and visualization on their datasets without writing code.

## Features

### 🚀 Advanced EDA Capabilities
- **Dropdown-Driven Analysis**: Navigate through different EDA sections using intuitive dropdown menus
- **Comprehensive Statistical Summary**: Descriptive statistics, data types, and basic information
- **Missing Value Analysis**: Identify, visualize, and understand null patterns
- **Advanced Visualizations**: Interactive charts using Plotly, Seaborn, and Matplotlib
- **Outlier Detection**: Statistical and visual outlier identification methods
- **Data Encoding**: Automatic handling of categorical variables
- **Feature Importance**: ML-based feature ranking and correlation analysis
- **Distribution Analysis**: Histogram, box plots, and probability distributions
- **Correlation Matrix**: Heatmaps and correlation insights

### 📁 File Upload Support
- **Drag-and-Drop Interface**: Easy file upload with visual feedback
- **Multiple Format Support**:
  - CSV files (.csv)
  - Excel files (.xlsx, .xls)
  - PDF files (.pdf) with text extraction
- **File Validation**: Automatic format detection and error handling
- **Large File Support**: Efficient processing of datasets up to 100MB

### 🎨 User Interface Design
- **Responsive Web Design**: Mobile and desktop friendly
- **Professional Dashboard**: Clean, modern interface
- **Interactive Menu System**: 
  - Main navigation dropdown
  - Section-specific analysis options
  - Dynamic result displays
- **Real-time Feedback**: Progress indicators and status updates
- **Export Capabilities**: Download analysis results and visualizations

### 🌐 Local Website Access
**Access your EDA application locally at:** `http://localhost:5000`

## Interface Menu Structure

```
📊 EDA Dashboard
├── 📈 Data Summary
│   ├── Basic Information
│   ├── Descriptive Statistics
│   └── Data Types Overview
│
├── 🕳️ Missing Values Analysis
│   ├── Null Patterns
│   ├── Missing Data Visualization
│   └── Imputation Suggestions
│
├── 📊 Data Visualizations
│   ├── Distribution Plots
│   ├── Correlation Heatmaps
│   ├── Scatter Plots
│   └── Box Plots
│
├── 🎯 Outlier Detection
│   ├── Statistical Methods (IQR, Z-score)
│   ├── Isolation Forest
│   └── Visual Outlier Identification
│
├── 🔤 Data Encoding
│   ├── Label Encoding
│   ├── One-Hot Encoding
│   └── Target Encoding
│
└── ⭐ Feature Importance
    ├── Correlation-based Ranking
    ├── Mutual Information
    └── Random Forest Importance
```

## Quick Start

1. **Installation**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Application**:
   ```bash
   python app.py
   ```

3. **Access Interface**:
   Open `http://localhost:5000` in your web browser

4. **Upload Data**:
   - Drag and drop your file or click to browse
   - Supported formats: CSV, Excel, PDF
   - Maximum file size: 100MB

5. **Analyze Data**:
   - Use dropdown menus to navigate analysis sections
   - View interactive visualizations
   - Export results as needed

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly, Matplotlib, Seaborn
- **Frontend**: HTML5, CSS3, JavaScript
- **File Processing**: openpyxl, PyPDF2
- **Machine Learning**: Scikit-learn

## Project Structure

```
EDA-WebApp/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   └── upload.html      # File upload interface
├── static/              # Static assets
│   ├── css/            # Custom stylesheets
│   ├── js/             # JavaScript files
│   └── images/         # Image assets
└── uploads/             # Temporary file storage
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**Rishav Raj**  
GitHub: [@Rishav-raj-github](https://github.com/Rishav-raj-github)

---

*Built with ❤️ for data scientists and analysts*

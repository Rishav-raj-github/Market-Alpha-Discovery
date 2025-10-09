# EDA-WebApp: Advanced Exploratory Data Analysis Platform

## Overview
EDA-WebApp is an advanced, interactive web application designed for comprehensive Exploratory Data Analysis (EDA) on user-uploaded files. This platform provides a streamlined, dropdown-based interface for analyzing Excel, CSV, and PDF files with professional-grade statistical analysis and visualizations.

## Features

### 📊 Supported File Formats
- **Excel files** (.xlsx, .xls)
- **CSV files** (.csv)
- **PDF files** (.pdf) - Extract tabular data for analysis

### 🔍 Advanced EDA Capabilities
All analysis options are accessible through intuitive dropdown menus:

1. **Data Overview**
   - Dataset preview (first/last rows)
   - Data types and shape information
   - Column names and structure

2. **Statistical Analysis**
   - Summary statistics (mean, median, mode, std dev)
   - Quartile analysis
   - Distribution analysis
   - Skewness and kurtosis

3. **Data Quality Assessment**
   - Missing values detection and visualization
   - Duplicate rows identification
   - Outlier detection (IQR method, Z-score)
   - Data completeness percentage

4. **Visualizations**
   - Interactive histograms
   - Box plots for outlier detection
   - Scatter plots for relationship analysis
   - Correlation heatmaps
   - Distribution plots
   - Pair plots for multivariate analysis

5. **Correlation Analysis**
   - Pearson correlation matrix
   - Spearman correlation
   - Interactive correlation heatmaps
   - Feature relationship insights

6. **Advanced Analytics**
   - Feature importance analysis
   - Categorical variable analysis
   - Time series analysis (if date columns detected)
   - Group-by operations with aggregations

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rishav-raj-github/Market-Alpha-Discovery.git
   cd Market-Alpha-Discovery
   git checkout eda-automation-webapp
   cd EDA-WebApp
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run EDA_app.py
   ```

4. **Access the application**
   - The app will automatically open in your default browser
   - Or manually navigate to: **http://localhost:8501**

## Usage

1. **Launch the app** using `streamlit run EDA_app.py`
2. **Upload your file** (Excel, CSV, or PDF) using the file uploader
3. **Select analysis type** from the dropdown menu
4. **Choose specific options** from sub-dropdown menus
5. **View interactive results** with dynamic charts and reports
6. **Download analysis** results if needed

## User Interface

The application features a clean, dropdown-based interface:
- 🎯 **Main Menu Dropdown**: Select primary analysis category
- 📋 **Sub-Menu Dropdowns**: Choose specific analysis within category
- 🎨 **Interactive Visualizations**: Powered by Plotly for zoom, pan, and export
- 📊 **Real-time Updates**: Analysis updates automatically based on selections

## Technical Stack

- **Frontend Framework**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Visualizations**: Plotly, Seaborn, Matplotlib
- **PDF Processing**: PyPDF2, Tabula-py
- **Excel Support**: openpyxl, xlrd
- **Statistical Analysis**: SciPy, Scikit-learn

## Project Structure

```
EDA-WebApp/
│
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── EDA_app.py            # Main Streamlit application
```

## Features in Detail

### Dropdown-Based Navigation
Every feature is accessible through organized dropdowns:
- No cluttered interface
- Easy navigation
- Beginner-friendly
- Professional appearance

### Interactive Charts
- Zoom and pan capabilities
- Hover for detailed information
- Export charts as images
- Responsive design

### Real-time Analysis
- Instant feedback on file upload
- Fast processing with caching
- Progress indicators for long operations
- Error handling with helpful messages

## Best Practices

- **Data Privacy**: All processing happens locally; no data is sent to external servers
- **File Size**: Recommended maximum file size is 200MB for optimal performance
- **Data Format**: Ensure your CSV/Excel files have headers in the first row
- **PDF Files**: Work best with structured tables

## Troubleshooting

**App won't start?**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.8+)

**File upload fails?**
- Verify file format is supported (.csv, .xlsx, .xls, .pdf)
- Check file size (should be under 200MB)
- Ensure file is not corrupted

**Visualization not showing?**
- Refresh the browser
- Check if the selected column contains numeric data
- Try a different visualization type

## Future Enhancements

- [ ] Support for more file formats (JSON, Parquet)
- [ ] Machine learning model suggestions
- [ ] Automated report generation (PDF/HTML)
- [ ] Data cleaning and preprocessing tools
- [ ] Multi-file comparison analysis
- [ ] Database connectivity
- [ ] Export processed data

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is open-source and available for educational and commercial use.

## Author

Developed by Rishav Raj

## Support

For questions or issues, please open an issue on the GitHub repository.

---

**Ready to explore your data? Run `streamlit run EDA_app.py` and visit http://localhost:8501** 🚀

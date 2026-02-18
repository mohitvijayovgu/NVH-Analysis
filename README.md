# NVH Analysis - Noise, Vibration, Harshness Vehicle Analysis

A comprehensive analysis tool for evaluating Noise, Vibration, and Harshness (NVH) performance in vehicles. This project combines data processing, analysis, and visualization to assess vehicle quality and customer satisfaction.

## 📋 Project Overview

NVH (Noise, Vibration, Harshness) is a critical quality metric in the automotive industry. This project provides tools and analysis for:

- Processing NVH measurement data
- Analyzing vehicle performance metrics
- Gathering and analyzing customer feedback
- Generating comprehensive reports
- Creating interactive dashboards for data visualization

## 📁 Project Structure

```
NVH-Analysis/
├── vehicle_master.py              # Main Python script for data processing
├── Vehicle.xlsx                    # Vehicle master data and specifications
├── NVH_Measurements.xlsx           # NVH measurement data and results
├── Customer_Feedback.xlsx          # Customer feedback and ratings
├── NVH Report.pdf                  # Generated NVH analysis report
├── NVH Vehicle Analysis.pbix       # Power BI dashboard
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## 📊 Files Description

### Python Scripts
- **vehicle_master.py** - Main script for:
  - Loading and processing vehicle data
  - Analyzing NVH measurements
  - Correlating with customer feedback
  - Generating reports and visualizations

### Data Files
- **Vehicle.xlsx** - Contains vehicle specifications, models, and identifiers
- **NVH_Measurements.xlsx** - Raw and processed NVH measurement data including noise, vibration levels
- **Customer_Feedback.xlsx** - Customer ratings and feedback related to NVH performance

### Reports & Dashboards
- **NVH Report.pdf** - Comprehensive PDF report with findings and recommendations
- **NVH Vehicle Analysis.pbix** - Interactive Power BI dashboard for data exploration

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pandas
- openpyxl
- matplotlib/seaborn (for visualizations)
- Power BI Desktop (for dashboard)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mohitvijayovgu/NVH-Analysis.git
cd NVH-Analysis
```

2. Install required Python packages:
```bash
pip install pandas openpyxl matplotlib seaborn
```

3. Run the analysis script:
```bash
python vehicle_master.py
```

## 📈 Usage

1. **Update data files** with the latest measurements and customer feedback
2. **Run the Python script** to process and analyze data
3. **Open the Power BI dashboard** for interactive visualization
4. **Review the generated report** for insights and recommendations

## 🔍 Key Metrics

- **Noise Levels** - Measured in decibels (dB)
- **Vibration** - Measured in acceleration (m/s²)
- **Harshness** - Qualitative and quantitative assessment
- **Customer Satisfaction** - Ratings and feedback scores

## 📝 Notes

- Ensure all Excel files are formatted consistently before running analysis
- Measurement data should include timestamps and vehicle identifiers
- Customer feedback is linked to specific vehicles/models

## 👤 Author

Mohit Vijay  
Email: mv.sit.me@gmail.com  
GitHub: [@mohitvijayovgu](https://github.com/mohitvijayovgu)

## 📄 License

This project is available under the MIT License. See LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

## 📞 Support

For questions or issues, please open an issue on GitHub or contact the author.

---

*Last Updated: February 18, 2026*

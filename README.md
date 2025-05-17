# Multi-Themed Financial Machine Learning Application

A collaborative Streamlit application that combines four unique visual themes with financial machine learning models. This project demonstrates the integration of financial data analysis, machine learning, and creative UI design.

## 🌟 Features

- **Multiple Visual Themes:**
  - Zombie Theme: Dark horror aesthetic with eerie elements
  - Futuristic Theme: Neon colors and space animations
  - Game of Thrones Theme: Medieval styling with fire and ice elements
  - Gaming Theme: Bright colors and pixel art

- **Machine Learning Models:**
  - Linear Regression
  - Logistic Regression
  - K-Means Clustering

- **Data Sources:**
  - Kragle datasets
  - Real-time Yahoo Finance data

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

## 📁 Project Structure

```
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md             # Project documentation
├── data/                 # Data storage directory
│   ├── raw/             # Raw datasets
│   └── processed/       # Processed datasets
├── src/                  # Source code
│   ├── themes/          # Theme implementations
│   │   ├── zombie.py
│   │   ├── futuristic.py
│   │   ├── got.py
│   │   └── gaming.py
│   ├── models/          # ML model implementations
│   │   ├── regression.py
│   │   ├── classification.py
│   │   └── clustering.py
│   └── utils/           # Utility functions
│       ├── data_loader.py
│       └── visualizations.py
└── assets/              # Static assets (images, GIFs, etc.)
    ├── zombie/
    ├── futuristic/
    ├── got/
    └── gaming/
```

## 🎨 Theme Descriptions

### Zombie Theme
- Dark color scheme
- Horror-themed GIFs
- Eerie fonts and styling
- Focus on survival and apocalypse aesthetics

### Futuristic Theme
- Neon colors
- Space animations
- Modern tech-inspired design
- Cyberpunk elements

### Game of Thrones Theme
- Medieval fonts
- Fire and ice imagery
- House sigils and banners
- Westeros-inspired color schemes

### Gaming Theme
- Bright, vibrant colors
- Pixel art GIFs
- Retro gaming aesthetics
- Arcade-style elements

## 🤝 Contributing

This is a group project with specific contributions from each team member. Please refer to the project documentation for contribution guidelines.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team Members

[Team member names and roles to be added]

## 📅 Submission Deadline

May 17, 2025 
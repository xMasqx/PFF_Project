from setuptools import setup, find_packages

setup(
    name="pff_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "pandas",
        "numpy",
        "plotly",
        "scikit-learn",
        "yfinance"
    ],
    python_requires=">=3.8",
) 
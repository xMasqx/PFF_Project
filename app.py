import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
import streamlit as st
from src.themes.zombie_theme import ZombieTheme
from src.themes.futuristic_theme import FuturisticTheme
from src.themes.got_theme import GoTTheme
from src.themes.gaming_theme import GamingTheme

# Set page configuration
st.set_page_config(
    page_title="Multi-Themed Financial ML App",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for theme switching
def load_css(theme):
    css = {
        "zombie": """
            :root {
                --primary-color: #2d2d2d;
                --secondary-color: #4a0000;
                --text-color: #e0e0e0;
                --background-color: #1a1a1a;
            }
        """,
        "futuristic": """
            :root {
                --primary-color: #00ff9d;
                --secondary-color: #0066ff;
                --text-color: #ffffff;
                --background-color: #000000;
            }
        """,
        "got": """
            :root {
                --primary-color: #8b0000;
                --secondary-color: #4682b4;
                --text-color: #d4af37;
                --background-color: #2f4f4f;
            }
        """,
        "gaming": """
            :root {
                --primary-color: #ff00ff;
                --secondary-color: #00ff00;
                --text-color: #ffffff;
                --background-color: #000000;
            }
        """
    }
    st.markdown(f"<style>{css[theme]}</style>", unsafe_allow_html=True)

# Sidebar navigation
def sidebar_navigation():
    st.sidebar.title("Navigation")
    theme = st.sidebar.selectbox(
        "Choose Theme",
        ["Welcome", "Zombie Theme", "Futuristic Theme", "Game of Thrones Theme", "Gaming Theme"]
    )
    return theme

# Welcome page
def welcome_page():
    st.title("Welcome to Multi-Themed Financial ML App")
    st.markdown("""
    ### 🎯 Project Overview
    This application combines financial machine learning with creative visual themes.
    Each theme offers unique insights into financial data using different machine learning models.
    
    ### 📊 Available Features
    - Real-time stock data analysis
    - Machine learning predictions
    - Interactive visualizations
    - Multiple themed interfaces
    
    ### 🎨 Themes
    1. **Zombie Theme**: Dark and eerie financial analysis
    2. **Futuristic Theme**: Neon-powered predictions
    3. **Game of Thrones Theme**: Medieval-styled market insights
    4. **Gaming Theme**: Pixel-perfect financial gaming
    
    ### 🚀 Getting Started
    Select a theme from the sidebar to begin your financial analysis journey!
    """)

# Main application logic
def main():
    theme = sidebar_navigation()
    
    if theme == "Welcome":
        welcome_page()
    elif theme == "Zombie Theme":
        ZombieTheme().run_theme()
    elif theme == "Futuristic Theme":
        FuturisticTheme().run_theme()
    elif theme == "Game of Thrones Theme":
        GoTTheme().run_theme()
    elif theme == "Gaming Theme":
        GamingTheme().run_theme()

if __name__ == "__main__":
    main() 
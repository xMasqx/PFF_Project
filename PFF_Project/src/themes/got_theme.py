from .base_theme import BaseTheme
from typing import Dict
import os
import streamlit as st
import pandas as pd
from ..utils.data_loader import data_loader
import plotly.express as px
import plotly.graph_objects as go
from src.utils.visualizations import ThemeVisualizer

class GoTTheme(BaseTheme):
    def __init__(self):
        super().__init__("Game of Thrones")
    
    def _get_theme_css(self) -> str:
        return """
            /* Main theme colors */
            :root {
                --primary-color: #b0b0b0;  /* Iron/steel gray */
                --secondary-color: #222831; /* Dark stone */
                --accent-color: #d4af37;    /* Gold for highlights */
                --background-color: #181818; /* Iron Throne dark */
                --text-color: #e0e0e0;
                --warning-color: #ff4500;   /* Fire red */
                --success-color: #b0b0b0;   /* Steel gray */
                --error-color: #a83232;     /* Blood red */
                --button-text: #1a1a1a;  /* Dark text for better contrast */
                --button-glow: #ffd700;  /* Bright gold for gleam effect */
            }
            
            /* Global styles */
            .stApp {
                background-color: var(--background-color);
                color: var(--text-color);
                background-image: url('assets/got/got_bg.jpg');
                background-size: cover;
                background-attachment: fixed;
            }
            
            /* Headers with medieval/gothic style */
            .theme-header h1 {
                color: var(--primary-color);
                font-family: 'UnifrakturCook', 'MedievalSharp', cursive, serif;
                text-shadow: 0 0 8px var(--accent-color), 2px 2px 0px #000, 0 0 20px #d4af37;
                border-bottom: 2px solid var(--accent-color);
                padding-bottom: 10px;
                margin-bottom: 20px;
                text-align: center;
                letter-spacing: 2px;
                font-size: 3em;
            }
            
            /* Add new CSS for decorative subheader with swords */
            .theme-subheader {
                position: relative;
                text-align: center;
                margin: 30px 0;
                padding: 15px 0;
            }
            
            .theme-subheader h2 {
                color: var(--accent-color);
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                text-shadow: 1px 1px 2px var(--primary-color);
                margin: 0;
                padding: 0 60px;
                letter-spacing: 1px;
                position: relative;
                display: inline-block;
            }
            
            .theme-subheader h2::before,
            .theme-subheader h2::after {
                content: '⚔';  /* Sword emoji as decorative element */
                position: absolute;
                top: 50%;
                transform: translateY(-50%);
                font-size: 1.5em;
                color: var(--accent-color);
                text-shadow: 0 0 10px var(--button-glow);
                animation: swordGlow 2s ease-in-out infinite alternate;
            }
            
            .theme-subheader h2::before {
                left: 20px;
            }
            
            .theme-subheader h2::after {
                right: 20px;
            }
            
            @keyframes swordGlow {
                0% {
                    text-shadow: 0 0 5px var(--button-glow);
                    transform: translateY(-50%) rotate(0deg);
                }
                100% {
                    text-shadow: 0 0 15px var(--button-glow);
                    transform: translateY(-50%) rotate(5deg);
                }
            }
            
            /* Info boxes with stone/gothic style */
            .theme-info {
                background-color: rgba(34, 40, 49, 0.92);
                border: 1px solid var(--primary-color);
                border-radius: 7px;
                padding: 15px;
                margin: 10px 0;
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                box-shadow: 0 0 10px var(--primary-color);
            }
            
            /* Warning boxes */
            .theme-warning {
                background-color: rgba(168, 50, 50, 0.9);
                border: 1px solid var(--warning-color);
                border-radius: 7px;
                padding: 15px;
                margin: 10px 0;
                color: var(--warning-color);
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                box-shadow: 0 0 10px var(--warning-color);
            }
            
            /* Success boxes */
            .theme-success {
                background-color: rgba(176, 176, 176, 0.15);
                border: 1px solid var(--success-color);
                border-radius: 7px;
                padding: 15px;
                margin: 10px 0;
                color: var(--success-color);
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                box-shadow: 0 0 10px var(--success-color);
            }
            
            /* Error boxes */
            .theme-error {
                background-color: rgba(168, 50, 50, 0.15);
                border: 1px solid var(--error-color);
                border-radius: 7px;
                padding: 15px;
                margin: 10px 0;
                color: var(--error-color);
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                box-shadow: 0 0 10px var(--error-color);
            }
            
            /* Sidebar with gothic style */
            .css-1d391kg {
                background-color: rgba(24, 24, 24, 0.97);
                border-right: 2px solid var(--primary-color);
            }
            
            /* Buttons with metallic/gothic style */
            .stButton>button {
                background: linear-gradient(
                    90deg,
                    var(--primary-color) 0%,
                    var(--accent-color) 50%,
                    var(--primary-color) 100%
                );
                background-size: 200% 100%;
                color: var(--button-text);
                border: 2px solid var(--accent-color);
                border-radius: 7px;
                padding: 10px 20px;
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                font-size: 1.1em;
                font-weight: bold;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: 0 0 10px rgba(212, 175, 55, 0.3);
                text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
                position: relative;
                overflow: hidden;
            }
            
            .stButton>button:hover {
                animation: swordGleam 1.5s linear infinite;
                box-shadow: 
                    0 0 15px var(--button-glow),
                    0 0 30px var(--accent-color),
                    inset 0 0 15px var(--button-glow);
                transform: translateY(-2px);
                border-color: var(--button-glow);
            }
            
            .stButton>button:active {
                transform: translateY(1px);
                box-shadow: 0 0 5px var(--accent-color);
            }
            
            .stButton>button::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(
                    45deg,
                    rgba(255, 255, 255, 0.1) 0%,
                    rgba(255, 255, 255, 0) 50%,
                    rgba(0, 0, 0, 0.1) 100%
                );
                pointer-events: none;
            }
            
            /* Data frames with gothic style */
            .stDataFrame {
                background-color: rgba(34, 40, 49, 0.92);
                border: 1px solid var(--primary-color);
                border-radius: 7px;
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
            }
            
            /* Charts with gothic style */
            .js-plotly-plot {
                background-color: rgba(34, 40, 49, 0.92) !important;
                border: 1px solid var(--primary-color);
                border-radius: 7px;
            }
            
            /* Metrics with gothic style */
            .stMetric {
                background-color: rgba(34, 40, 49, 0.92);
                border: 1px solid var(--primary-color);
                border-radius: 7px;
                padding: 15px;
                margin: 5px 0;
            }
            
            .stMetric label {
                color: var(--accent-color);
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
                text-transform: uppercase;
            }
            
            .stMetric div {
                color: var(--text-color);
                font-family: 'MedievalSharp', 'UnifrakturCook', cursive, serif;
            }

            /* Add the gleam animation keyframes */
            @keyframes swordGleam {
                0% {
                    background-position: -200% center;
                }
                100% {
                    background-position: 200% center;
                }
            }

            .got-bg-welcome {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                z-index: 0;
                background: url("data:{mime};base64,{bg_base64}") center center/cover no-repeat;
                opacity: 0.32;
                pointer-events: none;
            }
        """
    
    def _get_theme_fonts(self) -> Dict[str, str]:
        return {
            'UnifrakturCook': 'https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap',
            'MedievalSharp': 'https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap'
        }
    
    def _get_theme_images(self) -> Dict[str, str]:
        assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'got')
        os.makedirs(assets_dir, exist_ok=True)
        background_path = os.path.join(assets_dir, 'got_bg.jpg')
        header_path = os.path.join(assets_dir, 'got_header.gif')
        return {
            'background': background_path,
            'header': header_path,
            'loading': os.path.join(assets_dir, 'got_loading.gif'),
            'success': os.path.join(assets_dir, 'got_success.gif'),
            'error': os.path.join(assets_dir, 'got_error.gif')
        }
    
    def display_header(self, title: str) -> None:
        """Display the original text header only, no GIF, no custom container."""
        st.markdown(
            f"""
            <div class="theme-header">
                <h1>{title}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_subheader(self, title: str) -> None:
        """Display a themed subheader with decorative sword elements."""
        st.markdown(
            f"""
            <div class="theme-subheader">
                <h2>{title}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    def apply_theme(self) -> None:
        """Apply the GoT background to the whole app, like the futuristic theme."""
        st.markdown(f"<style>{self._get_theme_css()}</style>", unsafe_allow_html=True)
        # Always display the background image (GIF or JPG)
        bg_path = self.images.get('background', '')
        import base64, os
        if os.path.exists(bg_path):
            with open(bg_path, 'rb') as f:
                bg_bytes = f.read()
                bg_base64 = base64.b64encode(bg_bytes).decode('utf-8')
            # Determine MIME type
            if bg_path.endswith('.gif'):
                mime = 'image/gif'
            else:
                mime = 'image/jpeg'
            st.markdown(f'''
                <style>
                .got-bg-welcome {{
                    position: fixed;
                    top: 0; left: 0; width: 100vw; height: 100vh;
                    z-index: 0;
                    background: url("data:{mime};base64,{bg_base64}") center center/cover no-repeat;
                    opacity: 0.32;
                    pointer-events: none;
                }}
                .got-welcome-content {{
                    position: relative;
                    z-index: 1;
                }}
                </style>
                <div class="got-bg-welcome"></div>
            ''', unsafe_allow_html=True)

    def display_footer_gif(self) -> None:
        """Display the GoT header GIF at the bottom of the analysis."""
        st.markdown(
            """
            <div style="
                width: 100%;
                margin-top: 30px;
                padding: 20px 0;
                text-align: center;
                background: rgba(0, 0, 0, 0.3);
                border-top: 2px solid var(--accent-color);
                border-bottom: 2px solid var(--accent-color);
            ">
                <img src="data:image/gif;base64,{}" 
                     style="
                        max-width: 100%;
                        height: auto;
                        border-radius: 8px;
                        box-shadow: 0 0 20px var(--accent-color);
                     "
                />
            </div>
            """.format(self._get_base64_gif('header')),
            unsafe_allow_html=True
        )

    def _get_base64_gif(self, image_type: str) -> str:
        """Helper method to get base64 encoded GIF."""
        import base64
        image_path = self.images.get(image_type, '')
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                return base64.b64encode(f.read()).decode('utf-8')
        return ''

    def run_theme(self) -> None:
        """
        Run the Game of Thrones theme's main interface with medieval elements.
        """
        # Apply theme and show the header only once at the top
        self.apply_theme()
        self.display_header("Game of Thrones Theme")

        # Add theme-specific content (sidebar, data selection, etc.)
        st.sidebar.title(f"{self.name} Theme Settings")

        # Data selection
        data_source = st.sidebar.radio(
            "Select Data Source",
            ["Yahoo Finance", "Upload Kragle Dataset"],
            key=f"{self.name.lower()}_data_source"
        )

        if data_source == "Yahoo Finance":
            # Stock selection
            symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL", key=f"{self.name.lower()}_symbol")

            # Date range selection
            col1, col2 = st.sidebar.columns(2)
            with col1:
                start_date = st.date_input("Start Date", value=pd.Timestamp.now() - pd.Timedelta(days=365), key=f"{self.name.lower()}_start_date")
            with col2:
                end_date = st.date_input("End Date", value=pd.Timestamp.now(), key=f"{self.name.lower()}_end_date")

            # Add a load data button
            if st.sidebar.button("Load Stock Data", key=f"{self.name.lower()}_load_data"):
                try:
                    # Convert dates to datetime
                    start_dt = pd.Timestamp(start_date)
                    end_dt = pd.Timestamp(end_date)

                    # Load data
                    data = data_loader.load_stock_data(symbol, start_dt, end_dt)

                    # Calculate technical indicators
                    data = data_loader.calculate_technical_indicators(data)

                    # Store data in session state
                    st.session_state['stock_data'] = data
                    st.session_state['symbol'] = symbol

                    # Display success message
                    self.display_success(f"Successfully loaded data for {symbol}")

                except Exception as e:
                    self.display_error(f"Error loading stock data: {str(e)}")

            # Display data if available
            if 'stock_data' in st.session_state:
                data = st.session_state['stock_data']
                symbol = st.session_state['symbol']

                # Display data
                self.display_subheader(f"Stock Data for {symbol}")
                st.dataframe(data.tail())

                # Model selection
                model_type = st.sidebar.selectbox(
                    "Select Model Type",
                    ["regression", "classification", "clustering"],
                    key=f"{self.name.lower()}_model_type"
                )

                # Run analysis
                if st.sidebar.button("Run Analysis", key=f"{self.name.lower()}_run_analysis"):
                    self.run_analysis(data, model_type)

        else:  # Kragle dataset
            uploaded_file = st.sidebar.file_uploader(
                "Upload Kragle Dataset",
                type=['csv', 'xlsx'],
                key=f"{self.name.lower()}_file_uploader"
            )

            if uploaded_file is not None:
                try:
                    # Load data
                    data = data_loader.load_kragle_dataset(uploaded_file)

                    # Display data
                    self.display_subheader("Kragle Dataset")
                    st.dataframe(data.head())

                    # Model selection
                    model_type = st.sidebar.selectbox(
                        "Select Model Type",
                        ["regression", "classification", "clustering"],
                        key=f"{self.name.lower()}_kragle_model_type"
                    )

                    # Run analysis
                    if st.sidebar.button("Run Analysis", key=f"{self.name.lower()}_kragle_run_analysis"):
                        self.run_analysis(data, model_type)

                except Exception as e:
                    self.display_error(f"Error loading Kragle dataset: {str(e)}")
        
        # Add clear analysis button after analysis is run
        if 'analysis_run' in st.session_state and st.session_state['analysis_run']:
            if st.sidebar.button("Clear Analysis", key="got_theme_clear_analysis"):
                del st.session_state['analysis_run']
                st.rerun()

    def run_analysis(self, data: pd.DataFrame, model_type: str) -> None:
        # Remove all data cleaning, st.write, and plotly_chart calls here!
        super().run_analysis(data, model_type)
        self.display_footer_gif() 
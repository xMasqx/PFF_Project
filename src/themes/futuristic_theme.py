from .base_theme import BaseTheme
from typing import Dict
import os
import streamlit as st
import base64
from PIL import Image
import pandas as pd

class FuturisticTheme(BaseTheme):
    def __init__(self):
        super().__init__("Futuristic")
    
    def _get_theme_css(self) -> str:
        return """
            /* Main theme colors */
            :root {
                --primary-color: #00ff9d;    /* Neon green */
                --secondary-color: #0066ff;   /* Electric blue */
                --accent-color: #ff00ff;      /* Neon pink */
                --background-color: #000000;  /* Deep space black */
                --text-color: #ffffff;
                --warning-color: #ff3d00;     /* Neon orange */
                --success-color: #00ff9d;     /* Neon green */
                --error-color: #ff0000;       /* Neon red */
            }
            
            /* Global styles */
            .stApp {
                background-color: var(--background-color);
                color: var(--text-color);
                background-image: url('assets/futuristic/futuristic_background.jpg');
                background-size: cover;
                background-attachment: fixed;
            }
            
            /* Headers with neon glow effect */
            .theme-header h1 {
                color: var(--primary-color);
                font-family: 'Orbitron', sans-serif;
                text-shadow: 0 0 10px var(--primary-color),
                            0 0 20px var(--primary-color),
                            0 0 30px var(--primary-color);
                border-bottom: 2px solid var(--primary-color);
                padding-bottom: 10px;
                margin-bottom: 20px;
                text-align: center;
                letter-spacing: 2px;
                animation: neonPulse 1.5s ease-in-out infinite alternate;
            }
            
            @keyframes neonPulse {
                from {
                    text-shadow: 0 0 10px var(--primary-color),
                                0 0 20px var(--primary-color),
                                0 0 30px var(--primary-color);
                }
                to {
                    text-shadow: 0 0 15px var(--primary-color),
                                0 0 25px var(--primary-color),
                                0 0 35px var(--primary-color);
                }
            }
            
            .theme-subheader h2 {
                color: var(--secondary-color);
                font-family: 'Orbitron', sans-serif;
                text-shadow: 0 0 5px var(--secondary-color);
                margin-bottom: 15px;
                letter-spacing: 1px;
            }
            
            /* Info boxes with glass morphism effect */
            .theme-info {
                background: rgba(0, 0, 0, 0.7);
                backdrop-filter: blur(10px);
                border: 1px solid var(--primary-color);
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                font-family: 'Orbitron', sans-serif;
                box-shadow: 0 0 10px var(--primary-color);
            }
            
            /* Warning boxes */
            .theme-warning {
                background: rgba(255, 61, 0, 0.2);
                backdrop-filter: blur(10px);
                border: 1px solid var(--warning-color);
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                color: var(--warning-color);
                font-family: 'Orbitron', sans-serif;
                box-shadow: 0 0 10px var(--warning-color);
            }
            
            /* Success boxes */
            .theme-success {
                background: rgba(0, 255, 157, 0.2);
                backdrop-filter: blur(10px);
                border: 1px solid var(--success-color);
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                color: var(--success-color);
                font-family: 'Orbitron', sans-serif;
                box-shadow: 0 0 10px var(--success-color);
            }
            
            /* Error boxes */
            .theme-error {
                background: rgba(255, 0, 0, 0.2);
                backdrop-filter: blur(10px);
                border: 1px solid var(--error-color);
                border-radius: 10px;
                padding: 15px;
                margin: 10px 0;
                color: var(--error-color);
                font-family: 'Orbitron', sans-serif;
                box-shadow: 0 0 10px var(--error-color);
            }
            
            /* Sidebar with glass morphism */
            .css-1d391kg {
                background: rgba(0, 0, 0, 0.8);
                backdrop-filter: blur(10px);
                border-right: 1px solid var(--primary-color);
            }
            
            /* Buttons with neon effect */
            .stButton>button {
                background-color: transparent;
                color: var(--primary-color);
                border: 2px solid var(--primary-color);
                border-radius: 5px;
                padding: 10px 20px;
                font-family: 'Orbitron', sans-serif;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
                box-shadow: 0 0 5px var(--primary-color);
            }
            
            .stButton>button:hover {
                background-color: var(--primary-color);
                color: var(--background-color);
                box-shadow: 0 0 20px var(--primary-color);
            }
            
            /* Data frames with glass morphism */
            .stDataFrame {
                background: rgba(0, 0, 0, 0.7);
                backdrop-filter: blur(10px);
                border: 1px solid var(--primary-color);
                border-radius: 10px;
                box-shadow: 0 0 10px var(--primary-color);
            }
            
            /* Charts with futuristic styling */
            .js-plotly-plot {
                background: rgba(0, 0, 0, 0.7) !important;
                backdrop-filter: blur(10px);
                border: 1px solid var(--primary-color);
                border-radius: 10px;
                box-shadow: 0 0 10px var(--primary-color);
            }
            
            /* Metrics with neon effect */
            .stMetric {
                background: rgba(0, 0, 0, 0.7);
                backdrop-filter: blur(10px);
                border: 1px solid var(--primary-color);
                border-radius: 10px;
                padding: 15px;
                margin: 5px 0;
                box-shadow: 0 0 10px var(--primary-color);
            }
            
            .stMetric label {
                color: var(--primary-color);
                font-family: 'Orbitron', sans-serif;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .stMetric div {
                color: var(--text-color);
                font-family: 'Orbitron', sans-serif;
                text-shadow: 0 0 5px var(--primary-color);
            }
        """
    
    def _get_theme_fonts(self) -> Dict[str, str]:
        return {
            'Orbitron': 'https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&display=swap'
        }
    
    def _get_theme_images(self) -> Dict[str, str]:
        assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'futuristic')
        os.makedirs(assets_dir, exist_ok=True)
        # Prefer GIF for background if it exists
        gif_path = os.path.join(assets_dir, 'futuristic_background.gif')
        jpg_path = os.path.join(assets_dir, 'futuristic_background.jpg')
        if os.path.exists(gif_path):
            background_path = gif_path
        else:
            background_path = jpg_path
        return {
            'background': background_path,
            'header': os.path.join(assets_dir, 'futuristic_header.gif'),
            'loading': os.path.join(assets_dir, 'futuristic_loading.gif'),
            'success': os.path.join(assets_dir, 'futuristic_success.gif'),
            'error': os.path.join(assets_dir, 'futuristic_error.gif')
        }
    
    def display_gif(self, gif_name: str, caption: str = None) -> None:
        """Display a GIF image with an optional caption, but do nothing if missing or unreadable."""
        path = self.images.get(gif_name)
        if path and os.path.exists(path):
            try:
                # Try to open with PIL to check if it's a valid image
                with Image.open(path) as img:
                    pass
                st.image(path, caption=caption)
            except Exception:
                pass  # Do nothing if not a valid image
        # else: do nothing (no error, no placeholder)

    def run_theme(self) -> None:
        """
        Run the futuristic theme's main interface with space-age elements.
        """
        # Apply base theme
        self.apply_theme()

        # Always display the background image (GIF or JPG)
        bg_path = self.images.get('background', '')
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
                .futuristic-bg-welcome {{
                    position: fixed;
                    top: 0; left: 0; width: 100vw; height: 100vh;
                    z-index: 0;
                    background: url("data:{mime};base64,{bg_base64}") center center/cover no-repeat;
                    opacity: 0.35;
                }}
                .futuristic-welcome-content {{
                    position: relative;
                    z-index: 1;
                }}
                </style>
                <div class="futuristic-bg-welcome"></div>
            ''', unsafe_allow_html=True)

        # Show the welcome overlay content only if no data is loaded and analysis hasn't started
        if 'stock_data' not in st.session_state and 'analysis_run' not in st.session_state:
            st.markdown('<div class="futuristic-welcome-content">', unsafe_allow_html=True)
            self.display_gif('header', "Welcome to the Future of Financial Analysis")
            st.markdown(
                """
                <div class="theme-info">
                    🚀 Welcome to the Future of Financial Analysis! 🚀
                    <br><br>
                    In this quantum-powered interface, we harness the power of advanced algorithms
                    to predict market movements with unprecedented accuracy.
                    <br><br>
                    Prepare to transcend traditional financial analysis and enter the realm of
                    next-generation market predictions!
                </div>
                """,
                unsafe_allow_html=True
            )
            self.display_warning("""
                ⚡ WARNING: Market volatility detected! Quantum fluctuations may affect predictions.<br>
                Always verify your analysis with multiple data points across the space-time continuum.
            """)
            st.markdown('</div>', unsafe_allow_html=True)

        # Add clear analysis button after analysis is run
        if 'analysis_run' in st.session_state and st.session_state['analysis_run']:
            if st.sidebar.button("Clear Analysis", key="futuristic_theme_clear_analysis"):
                del st.session_state['analysis_run']
                st.rerun()

        # Always show the sidebar and analysis workflow
        super().run_theme() 
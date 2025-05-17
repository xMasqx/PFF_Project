from .base_theme import BaseTheme
from typing import Dict
import os
import base64
import streamlit as st
from PIL import Image

class GamingTheme(BaseTheme):
    def __init__(self):
        super().__init__("Gaming")
    
    def _get_theme_css(self) -> str:
        return """
            /* Main theme colors */
            :root {
                --primary-color: #ff00ff;    /* Hot pink */
                --secondary-color: #00ff00;   /* Neon green */
                --accent-color: #ffff00;      /* Bright yellow */
                --background-color: #000000;  /* Black */
                --text-color: #ffffff;
                --warning-color: #ff4500;     /* Orange red */
                --success-color: #00ff00;     /* Neon green */
                --error-color: #ff0000;       /* Red */
            }
            
            /* Global styles */
            .stApp {
                background-color: var(--background-color);
                color: var(--text-color);
                background-image: url('assets/gaming/gaming_background.jpg');
                background-size: cover;
                background-attachment: fixed;
                image-rendering: pixelated;
            }
            
            /* Headers with pixel art style */
            .theme-header h1 {
                color: var(--primary-color);
                font-family: 'Press Start 2P', cursive;
                text-shadow: 4px 4px 0px var(--secondary-color);
                border-bottom: 4px solid var(--primary-color);
                padding-bottom: 10px;
                margin-bottom: 20px;
                text-align: center;
                letter-spacing: 2px;
                animation: pixelGlow 1s steps(2) infinite;
            }
            
            @keyframes pixelGlow {
                0% { text-shadow: 4px 4px 0px var(--secondary-color); }
                50% { text-shadow: 4px 4px 0px var(--accent-color); }
                100% { text-shadow: 4px 4px 0px var(--secondary-color); }
            }
            
            .theme-subheader h2 {
                color: var(--secondary-color);
                font-family: 'Press Start 2P', cursive;
                text-shadow: 2px 2px 0px var(--primary-color);
                margin-bottom: 15px;
                letter-spacing: 1px;
            }
            
            /* Info boxes with pixel border */
            .theme-info {
                background-color: rgba(0, 0, 0, 0.8);
                border: 4px solid var(--primary-color);
                border-image: repeating-linear-gradient(
                    45deg,
                    var(--primary-color),
                    var(--primary-color) 10px,
                    var(--secondary-color) 10px,
                    var(--secondary-color) 20px
                ) 4;
                padding: 15px;
                margin: 10px 0;
                font-family: 'Press Start 2P', cursive;
                font-size: 0.8em;
                line-height: 1.5;
            }
            
            /* Warning boxes */
            .theme-warning {
                background-color: rgba(0, 0, 0, 0.8);
                border: 4px solid var(--warning-color);
                border-image: repeating-linear-gradient(
                    45deg,
                    var(--warning-color),
                    var(--warning-color) 10px,
                    var(--accent-color) 10px,
                    var(--accent-color) 20px
                ) 4;
                padding: 15px;
                margin: 10px 0;
                color: var(--warning-color);
                font-family: 'Press Start 2P', cursive;
                font-size: 0.8em;
                line-height: 1.5;
            }
            
            /* Success boxes */
            .theme-success {
                background-color: rgba(0, 0, 0, 0.8);
                border: 4px solid var(--success-color);
                border-image: repeating-linear-gradient(
                    45deg,
                    var(--success-color),
                    var(--success-color) 10px,
                    var(--accent-color) 10px,
                    var(--accent-color) 20px
                ) 4;
                padding: 15px;
                margin: 10px 0;
                color: var(--success-color);
                font-family: 'Press Start 2P', cursive;
                font-size: 0.8em;
                line-height: 1.5;
            }
            
            /* Error boxes */
            .theme-error {
                background-color: rgba(0, 0, 0, 0.8);
                border: 4px solid var(--error-color);
                border-image: repeating-linear-gradient(
                    45deg,
                    var(--error-color),
                    var(--error-color) 10px,
                    var(--accent-color) 10px,
                    var(--accent-color) 20px
                ) 4;
                padding: 15px;
                margin: 10px 0;
                color: var(--error-color);
                font-family: 'Press Start 2P', cursive;
                font-size: 0.8em;
                line-height: 1.5;
            }
            
            /* Sidebar with pixel art style */
            .css-1d391kg {
                background-color: rgba(0, 0, 0, 0.9);
                border-right: 4px solid var(--primary-color);
                border-image: repeating-linear-gradient(
                    to bottom,
                    var(--primary-color),
                    var(--primary-color) 10px,
                    var(--secondary-color) 10px,
                    var(--secondary-color) 20px
                ) 4;
            }
            
            /* Buttons with pixel art style */
            .stButton>button {
                background-color: var(--primary-color);
                color: var(--background-color);
                border: 4px solid var(--secondary-color);
                border-radius: 0;
                padding: 10px 20px;
                font-family: 'Press Start 2P', cursive;
                font-size: 0.8em;
                transition: all 0.1s steps(2);
                text-transform: uppercase;
                letter-spacing: 1px;
                position: relative;
                top: 0;
            }
            
            .stButton>button:hover {
                background-color: var(--secondary-color);
                color: var(--background-color);
                border-color: var(--primary-color);
                top: -2px;
                box-shadow: 4px 4px 0px var(--accent-color);
            }
            
            .stButton>button:active {
                top: 2px;
                box-shadow: none;
            }
            
            /* Data frames with pixel art style */
            .stDataFrame {
                background-color: rgba(0, 0, 0, 0.8);
                border: 4px solid var(--primary-color);
                border-radius: 0;
                font-family: 'Press Start 2P', cursive;
                font-size: 0.7em;
            }
            
            /* Charts with pixel art style */
            .js-plotly-plot {
                background-color: rgba(0, 0, 0, 0.8) !important;
                border: 4px solid var(--primary-color);
                border-radius: 0;
            }
            
            /* Metrics with pixel art style */
            .stMetric {
                background-color: rgba(0, 0, 0, 0.8);
                border: 4px solid var(--primary-color);
                border-radius: 0;
                padding: 15px;
                margin: 5px 0;
            }
            
            .stMetric label {
                color: var(--primary-color);
                font-family: 'Press Start 2P', cursive;
                font-size: 0.8em;
                text-transform: uppercase;
            }
            
            .stMetric div {
                color: var(--text-color);
                font-family: 'Press Start 2P', cursive;
                font-size: 0.9em;
            }
        """
    
    def _get_theme_fonts(self) -> Dict[str, str]:
        return {
            'Press Start 2P': 'https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap'
        }
    
    def _get_theme_images(self) -> Dict[str, str]:
        assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'gaming')
        os.makedirs(assets_dir, exist_ok=True)
        return {
            'background': os.path.join(assets_dir, 'gaming_background.jpg'),
            'header': os.path.join(assets_dir, 'gaming_header.gif'),
            'loading': os.path.join(assets_dir, 'gaming_loading.gif'),
            'success': os.path.join(assets_dir, 'gaming_success.gif'),
            'error': os.path.join(assets_dir, 'gaming_error.gif')
        }
    
    def run_theme(self) -> None:
        """
        Run the gaming theme's main interface with retro gaming elements.
        """
        # Add base64-encoded background overlay
        bg_path = self.images.get('background', '')
        if os.path.exists(bg_path):
            with open(bg_path, 'rb') as f:
                bg_bytes = f.read()
                bg_base64 = base64.b64encode(bg_bytes).decode('utf-8')
            mime = 'image/jpeg' if bg_path.endswith('.jpg') else 'image/png'
            st.markdown(f'''
                <style>
                .gaming-bg-welcome {{
                    position: fixed;
                    top: 0; left: 0; width: 100vw; height: 100vh;
                    z-index: 0;
                    background: url("data:{mime};base64,{bg_base64}") center center/cover no-repeat;
                    opacity: 0.32;
                    pointer-events: none;
                }}
                .gaming-welcome-content {{
                    position: relative;
                    z-index: 1;
                }}
                </style>
                <div class="gaming-bg-welcome"></div>
            ''', unsafe_allow_html=True)
        # Add gaming_analysis.jpg above the welcome GIF and message
        analysis_img_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'gaming', 'gaming_analysis.jpg')
        if os.path.exists(analysis_img_path):
            img = Image.open(analysis_img_path)
            width, height = img.size
            crop_width, crop_height = 1920, 1080
            # If image is smaller, pad/crop as needed
            left = max(0, (width - crop_width) // 2)
            upper = max(0, height - crop_height)
            right = left + crop_width
            lower = upper + crop_height
            img_cropped = img.crop((left, upper, right, lower))
            st.image(img_cropped, caption="Welcome to the Financial Gaming Arena", use_container_width=True)
        # Apply base theme
        super().run_theme()

        # Add a warning about market volatility
        self.display_warning("""
            ⚠️ GAME OVER WARNING: Market volatility detected!
            Make sure to collect enough power-ups (data points) before
            facing the final boss (market predictions).
        """)

        # Add clear analysis button and show GIF after analysis
        if 'analysis_run' in st.session_state and st.session_state['analysis_run']:
            if st.sidebar.button("Clear Analysis", key="gaming_theme_clear_analysis"):
                del st.session_state['analysis_run']
                st.rerun()
            # Show the gaming_eldenring.gif at the bottom
            eldenring_gif_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'gaming', 'gaming_eldenring.gif')
            if os.path.exists(eldenring_gif_path):
                with open(eldenring_gif_path, 'rb') as f:
                    gif_base64 = base64.b64encode(f.read()).decode('utf-8')
                st.markdown(
                    f'''<div style="width: 100%; margin-top: 30px; padding: 20px 0; text-align: center; background: rgba(0,0,0,0.3); border-top: 2px solid var(--accent-color); border-bottom: 2px solid var(--accent-color);">
                        <img src="data:image/gif;base64,{gif_base64}" style="max-width: 100%; height: auto; border-radius: 8px; box-shadow: 0 0 20px var(--accent-color);" />
                    </div>''',
                    unsafe_allow_html=True
                ) 
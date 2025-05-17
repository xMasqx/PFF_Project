from .base_theme import BaseTheme
from typing import Dict
import os
import streamlit as st
import pandas as pd
from ..utils.data_loader import data_loader
from src.utils.visualizations import ThemeVisualizer

class ZombieTheme(BaseTheme):
    def __init__(self):
        super().__init__("Zombie")
    
    def _get_theme_css(self) -> str:
        return """
            /* Main theme colors */
            :root {
                --primary-color: #2d2d2d;    /* Dark gray */
                --secondary-color: #4a0000;   /* Blood red */
                --accent-color: #e0e0e0;      /* Ghostly white */
                --background-color: #1a1a1a;  /* Dark background */
                --text-color: #e0e0e0;        /* Light text */
                --warning-color: #ff4500;     /* Fire orange */
                --success-color: #00ff00;     /* Toxic green */
                --error-color: #ff0000;       /* Blood red */
            }
            
            /* Global styles */
            .stApp {
                background-color: var(--background-color);
                color: var(--text-color);
            }
            
            /* Welcome message styles */
            .welcome-message {
                font-family: 'Creepster', cursive;
                font-size: 1.5em;
                color: var(--accent-color);
                text-shadow: 2px 2px 4px var(--primary-color),
                            0 0 10px var(--secondary-color);
                letter-spacing: 2px;
                line-height: 1.6;
                text-align: center;
                padding: 20px;
                margin: 20px 0;
                animation: flicker 3s infinite;
            }
            
            .welcome-message .zombie-emoji {
                font-size: 1.8em;
                animation: float 2s ease-in-out infinite;
                display: inline-block;
                margin: 0 5px;
            }
            
            .welcome-message .highlight {
                color: var(--secondary-color);
                font-weight: bold;
                text-shadow: 0 0 5px var(--secondary-color);
            }
            
            @keyframes flicker {
                0% { opacity: 1; }
                50% { opacity: 0.8; }
                100% { opacity: 1; }
            }
            
            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-5px); }
                100% { transform: translateY(0px); }
            }
            
            /* Welcome container styles */
            .welcome-container {
                background-color: rgba(26, 26, 26, 0.9);
                border: 2px solid var(--secondary-color);
                border-radius: 10px;
                padding: 20px;
                margin: 20px 0;
                position: relative;
                overflow: hidden;
            }
            
            .welcome-background {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                z-index: 0;
                opacity: 0.3;
            }
            
            .welcome-content {
                position: relative;
                z-index: 1;
            }
            
            /* Headers with horror style */
            .theme-header h1 {
                color: var(--secondary-color);
                font-family: 'Creepster', cursive;
                text-shadow: 2px 2px 4px var(--primary-color),
                            0 0 10px var(--secondary-color);
                border-bottom: 2px solid var(--secondary-color);
                padding-bottom: 10px;
                margin-bottom: 20px;
                text-align: center;
                letter-spacing: 2px;
                animation: bloodDrip 2s infinite;
            }
            
            @keyframes bloodDrip {
                0% { text-shadow: 2px 2px 4px var(--primary-color),
                            0 0 10px var(--secondary-color); }
                50% { text-shadow: 2px 2px 4px var(--primary-color),
                            0 0 20px var(--secondary-color); }
                100% { text-shadow: 2px 2px 4px var(--primary-color),
                            0 0 10px var(--secondary-color); }
            }
            
            .theme-subheader h2 {
                color: var(--accent-color);
                font-family: 'Creepster', cursive;
                text-shadow: 1px 1px 2px var(--primary-color);
                margin-bottom: 15px;
                letter-spacing: 1px;
            }
            
            /* Info boxes with horror style */
            .theme-info {
                background-color: rgba(45, 45, 45, 0.9);
                border: 1px solid var(--secondary-color);
                border-radius: 5px;
                padding: 15px;
                margin: 10px 0;
                font-family: 'Creepster', cursive;
                box-shadow: 0 0 10px var(--secondary-color);
            }
            
            /* Warning boxes */
            .theme-warning {
                background-color: rgba(74, 0, 0, 0.9);
                border: 1px solid var(--warning-color);
                border-radius: 5px;
                padding: 15px;
                margin: 10px 0;
                color: var(--warning-color);
                font-family: 'Creepster', cursive;
                box-shadow: 0 0 10px var(--warning-color);
            }
            
            /* Success boxes */
            .theme-success {
                background-color: rgba(0, 255, 0, 0.1);
                border: 1px solid var(--success-color);
                border-radius: 5px;
                padding: 15px;
                margin: 10px 0;
                color: var(--success-color);
                font-family: 'Creepster', cursive;
                box-shadow: 0 0 10px var(--success-color);
            }
            
            /* Error boxes */
            .theme-error {
                background-color: rgba(255, 0, 0, 0.1);
                border: 1px solid var(--error-color);
                border-radius: 5px;
                padding: 15px;
                margin: 10px 0;
                color: var(--error-color);
                font-family: 'Creepster', cursive;
                box-shadow: 0 0 10px var(--error-color);
            }
            
            /* Sidebar with horror style */
            .css-1d391kg {
                background-color: rgba(26, 26, 26, 0.95);
                border-right: 1px solid var(--secondary-color);
            }
            
            /* Buttons with horror style */
            .stButton>button {
                background-color: var(--primary-color);
                color: var(--accent-color);
                border: 1px solid var(--secondary-color);
                border-radius: 5px;
                padding: 10px 20px;
                font-family: 'Creepster', cursive;
                transition: all 0.3s ease;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .stButton>button:hover {
                background-color: var(--secondary-color);
                color: var(--accent-color);
                box-shadow: 0 0 10px var(--secondary-color);
            }
            
            /* Data frames with horror style */
            .stDataFrame {
                background-color: rgba(45, 45, 45, 0.9);
                border: 1px solid var(--secondary-color);
                border-radius: 5px;
                font-family: 'Creepster', cursive;
            }
            
            /* Charts with horror style */
            .js-plotly-plot {
                background-color: rgba(45, 45, 45, 0.9) !important;
                border: 1px solid var(--secondary-color);
                border-radius: 5px;
            }
            
            /* Metrics with horror style */
            .stMetric {
                background-color: rgba(45, 45, 45, 0.9);
                border: 1px solid var(--secondary-color);
                border-radius: 5px;
                padding: 15px;
                margin: 5px 0;
            }
            
            .stMetric label {
                color: var(--accent-color);
                font-family: 'Creepster', cursive;
                text-transform: uppercase;
            }
            
            .stMetric div {
                color: var(--text-color);
                font-family: 'Creepster', cursive;
            }
        """
    
    def _get_theme_fonts(self) -> Dict[str, str]:
        return {
            'Creepster': 'https://fonts.googleapis.com/css2?family=Creepster&display=swap',
            'Nosifer': 'https://fonts.googleapis.com/css2?family=Nosifer&display=swap'
        }
    
    def _get_theme_images(self) -> Dict[str, str]:
        """Get paths to theme-specific images and videos."""
        assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets', 'zombie')
        os.makedirs(assets_dir, exist_ok=True)
        
        # Define media paths - only include files we actually use
        media_paths = {
            'background': os.path.join(assets_dir, 'zombie_background.gif'),
            'header': os.path.join(assets_dir, 'zombie_video.mp4')  # Changed to video
        }
        
        # Create a new dictionary for verified paths
        verified_paths = {}
        
        # Verify files exist
        for key, path in media_paths.items():
            if os.path.exists(path):
                verified_paths[key] = path
            else:
                # For background, try jpg version if gif not found
                if key == 'background':
                    jpg_path = path.replace('.gif', '.jpg')
                    if os.path.exists(jpg_path):
                        verified_paths[key] = jpg_path
                    else:
                        st.warning(f"Warning: {key} image not found at {path} or {jpg_path}")
                else:
                    st.warning(f"Warning: {key} media not found at {path}")
        
        return verified_paths
    
    def run_theme(self) -> None:
        """
        Run the zombie theme's main interface with horror elements.
        """
        # Apply theme
        self.apply_theme()
        
        # Display theme header
        self.display_header(f"{self.name} Theme")
        
        # Add theme-specific content
        st.sidebar.title(f"{self.name} Theme Settings")
        
        # Show welcome message by default
        if 'analysis_run' not in st.session_state:
            # Create a container for the welcome section
            with st.container():
                # Add zombie-specific elements
                self.display_header("Welcome to the Zombie Financial Apocalypse")
                
                # Add a horror message with enhanced styling
                st.markdown("""
                    <div class="welcome-message">
                        <span class="zombie-emoji">🧟</span> 
                        <span class="highlight">Welcome to the Zombie Financial Apocalypse!</span> 
                        <span class="zombie-emoji">🧟</span>
                        <br><br>
                        In this <span class="highlight">undead market</span>, only the strongest survive.<br>
                        Choose your <span class="highlight">weapon</span> (model) wisely, for the market<br>
                        <span class="highlight">hungers</span> for your portfolio.<br><br>
                        May the <span class="highlight">walking dead</span> guide your financial decisions!
                    </div>
                """, unsafe_allow_html=True)
                
                # Add a warning about market volatility
                self.display_warning("""
                    ⚰️ WARNING: The market is more volatile than a zombie outbreak!
                    Proceed with caution and always keep your portfolio well-protected.
                """)
                
                # Add some spacing
                st.markdown("<br>", unsafe_allow_html=True)
                
                # Display the background GIF in full width
                if 'background' in self.images:
                    try:
                        st.image(
                            self.images['background'],
                            use_container_width=True,
                            caption="The Undead Market Awaits...",
                            output_format="GIF" if self.images['background'].endswith('.gif') else "JPEG"
                        )
                    except Exception as e:
                        st.error(f"Error loading background image: {str(e)}")
        
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
                
                # Run analysis button
                if st.sidebar.button("Run Analysis", key="zombie_theme_run_analysis"):
                    st.session_state['analysis_run'] = True
                    st.rerun()
                
                # Show clear analysis button after analysis is run
                if 'analysis_run' in st.session_state and st.session_state['analysis_run']:
                    if st.sidebar.button("Clear Analysis", key="zombie_theme_clear_analysis"):
                        del st.session_state['analysis_run']
                        st.rerun()
                    
                    # Run analysis
                    self.run_analysis(data, model_type)
                    
                    # Add some spacing
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    # Display the zombie video after analysis
                    if 'header' in self.images:
                        try:
                            # Create a container for the video
                            with st.container():
                                # Use HTML to create an autoplaying, looping, muted video
                                st.markdown(f"""
                                    <div style="width: 100%; margin: 0 auto;">
                                        <video 
                                            autoplay 
                                            loop 
                                            muted 
                                            playsinline 
                                            style="width: 100%; height: auto; pointer-events: none;"
                                        >
                                            <source src="data:video/mp4;base64,{self._get_video_base64(self.images['header'])}" type="video/mp4">
                                        </video>
                                        <div style="text-align: center; font-family: Creepster, cursive; color: #4a0000; margin-top: 10px;">
                                            The Undead Market Continues...
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
                        except Exception as e:
                            st.error(f"Error loading header video: {str(e)}")
        
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
                    
                    # Store data in session state
                    st.session_state['stock_data'] = data
                    
                    # Display data
                    self.display_subheader("Kragle Dataset")
                    st.dataframe(data.head())
                    
                    # Model selection
                    model_type = st.sidebar.selectbox(
                        "Select Model Type",
                        ["regression", "classification", "clustering"],
                        key=f"{self.name.lower()}_kragle_model_type"
                    )
                    
                    # Run analysis button
                    if st.sidebar.button("Run Analysis", key="zombie_theme_kragle_run_analysis"):
                        st.session_state['analysis_run'] = True
                        st.rerun()
                    
                    # Show clear analysis button after analysis is run
                    if 'analysis_run' in st.session_state and st.session_state['analysis_run']:
                        if st.sidebar.button("Clear Analysis", key="zombie_theme_kragle_clear_analysis"):
                            del st.session_state['analysis_run']
                            st.rerun()
                        
                        # Run analysis
                        self.run_analysis(data, model_type)
                        
                        # Add some spacing
                        st.markdown("<br>", unsafe_allow_html=True)
                        
                        # Display the zombie video after analysis
                        if 'header' in self.images:
                            try:
                                # Create a container for the video
                                with st.container():
                                    # Use HTML to create an autoplaying, looping, muted video
                                    st.markdown(f"""
                                        <div style="width: 100%; margin: 0 auto;">
                                            <video 
                                                autoplay 
                                                loop 
                                                muted 
                                                playsinline 
                                                style="width: 100%; height: auto; pointer-events: none;"
                                            >
                                                <source src="data:video/mp4;base64,{self._get_video_base64(self.images['header'])}" type="video/mp4">
                                            </video>
                                            <div style="text-align: center; font-family: Creepster, cursive; color: #4a0000; margin-top: 10px;">
                                                The Undead Market Continues...
                                            </div>
                                        </div>
                                    """, unsafe_allow_html=True)
                            except Exception as e:
                                st.error(f"Error loading header video: {str(e)}")
                
                except Exception as e:
                    self.display_error(f"Error loading Kragle dataset: {str(e)}")
    
    def _get_regression_message(self, data: pd.DataFrame, metrics: Dict[str, float]) -> None:
        """Get zombie-themed regression analysis message."""
        if metrics:
            r2 = metrics.get('r2', 0)
            mse = metrics.get('mse', 0)
            
            if r2 > 0.8:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE UNDEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your regression model has risen from the grave with terrifying accuracy!</p>
                        <p>R² of <span class="highlight">{:.2f}</span> suggests this model hungers for market predictions...</p>
                        <p><span class="highlight">WARNING:</span> The model's MSE of <span class="highlight">{:.2f}</span> indicates
                        some volatility in its predictions. Keep your portfolio well-protected!</p>
                    </div>
                """.format(r2, mse), unsafe_allow_html=True)
            elif r2 > 0.5:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE WALKING DEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your regression model shows signs of life with moderate accuracy.</p>
                        <p>R² of <span class="highlight">{:.2f}</span> suggests it's still learning to walk...</p>
                        <p><span class="highlight">CAUTION:</span> The model's MSE of <span class="highlight">{:.2f}</span> indicates
                        it might be a bit... unstable. Proceed with care!</p>
                    </div>
                """.format(r2, mse), unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE DEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your regression model seems to be... well, dead.</p>
                        <p>R² of <span class="highlight">{:.2f}</span> suggests it's time to put this one down.</p>
                        <p><span class="highlight">DANGER:</span> The model's MSE of <span class="highlight">{:.2f}</span> indicates
                        it's completely lost its mind. Time to find a new weapon!</p>
                    </div>
                """.format(r2, mse), unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="theme-info">
                    <h3>🧟 THE UNDEAD HAVE SPOKEN! 🧟</h3>
                    <p>Your regression model has completed its analysis of the market's
                    walking patterns. Check the charts above to see how it predicts
                    the market's next moves...</p>
                </div>
            """, unsafe_allow_html=True)
    
    def _get_classification_message(self, data: pd.DataFrame, metrics: Dict[str, float]) -> None:
        """Get zombie-themed classification analysis message."""
        if metrics:
            accuracy = metrics.get('accuracy', 0)
            f1 = metrics.get('f1', 0)
            
            if accuracy > 0.8:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE UNDEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your classification model has risen with terrifying precision!</p>
                        <p>Accuracy of <span class="highlight">{:.2f}</span> and F1 score of <span class="highlight">{:.2f}</span> suggest
                        it can smell market opportunities from miles away...</p>
                        <p><span class="highlight">WARNING:</span> Even the most accurate models
                        can turn on you. Stay vigilant!</p>
                    </div>
                """.format(accuracy, f1), unsafe_allow_html=True)
            elif accuracy > 0.5:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE WALKING DEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your classification model shows signs of life with moderate accuracy.</p>
                        <p>Accuracy of <span class="highlight">{:.2f}</span> and F1 score of <span class="highlight">{:.2f}</span> suggest
                        it's still learning to distinguish friend from foe...</p>
                        <p><span class="highlight">CAUTION:</span> The model might be a bit confused.
                        Double-check its predictions!</p>
                    </div>
                """.format(accuracy, f1), unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE DEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your classification model seems to be... well, dead.</p>
                        <p>Accuracy of <span class="highlight">{:.2f}</span> and F1 score of <span class="highlight">{:.2f}</span> suggest
                        it's time to put this one down.</p>
                        <p><span class="highlight">DANGER:</span> The model is completely lost.
                        Time to find a new weapon!</p>
                    </div>
                """.format(accuracy, f1), unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="theme-info">
                    <h3>🧟 THE UNDEAD HAVE SPOKEN! 🧟</h3>
                    <p>Your classification model has completed its analysis of market patterns.
                    Check the charts above to see how it categorizes market movements...</p>
                </div>
            """, unsafe_allow_html=True)
    
    def _get_clustering_message(self, data: pd.DataFrame, metrics: Dict[str, float]) -> None:
        """Get zombie-themed clustering analysis message."""
        if metrics:
            silhouette = metrics.get('silhouette', 0)
            
            if silhouette > 0.5:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE UNDEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your clustering model has found distinct hordes in the market!</p>
                        <p>Silhouette score of <span class="highlight">{:.2f}</span> suggests clear separation
                        between different market behaviors...</p>
                        <p><span class="highlight">WARNING:</span> Even the most distinct clusters
                        can merge in volatile markets. Stay alert!</p>
                    </div>
                """.format(silhouette), unsafe_allow_html=True)
            elif silhouette > 0.3:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE WALKING DEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your clustering model has found some wandering groups in the market.</p>
                        <p>Silhouette score of <span class="highlight">{:.2f}</span> suggests moderate separation
                        between market behaviors...</p>
                        <p><span class="highlight">CAUTION:</span> The clusters might be a bit
                        confused. Watch them carefully!</p>
                    </div>
                """.format(silhouette), unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div class="theme-info">
                        <h3>🧟 THE DEAD HAVE SPOKEN! 🧟</h3>
                        <p>Your clustering model has found a chaotic mess in the market.</p>
                        <p>Silhouette score of <span class="highlight">{:.2f}</span> suggests everything
                        is just one big horde...</p>
                        <p><span class="highlight">DANGER:</span> The market is too chaotic
                        for this model. Time to find a new approach!</p>
                    </div>
                """.format(silhouette), unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class="theme-info">
                    <h3>🧟 THE UNDEAD HAVE SPOKEN! 🧟</h3>
                    <p>Your clustering model has completed its analysis of market hordes.
                    Check the charts above to see how it groups market behaviors...</p>
                </div>
            """, unsafe_allow_html=True)
    
    def _get_video_base64(self, video_path: str) -> str:
        """Convert video file to base64 string for embedding."""
        import base64
        try:
            with open(video_path, 'rb') as video_file:
                video_bytes = video_file.read()
                return base64.b64encode(video_bytes).decode('utf-8')
        except Exception as e:
            st.error(f"Error converting video to base64: {str(e)}")
            return "" 
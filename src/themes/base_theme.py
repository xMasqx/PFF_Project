from abc import ABC, abstractmethod
import streamlit as st
from typing import Dict, Any, Optional
import pandas as pd
import numpy as np
from ..utils.data_loader import data_loader
from ..utils.visualizations import ThemeVisualizer
from ..models.regression import LinearRegressionModel
from ..models.classification import LogisticRegressionModel
from ..models.clustering import KMeansModel
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import traceback

class BaseTheme(ABC):
    def __init__(self, name: str):
        """
        Initialize the base theme.
        
        Args:
            name: Name of the theme
        """
        self.name = name
        self.visualizer = ThemeVisualizer(name.lower())
        self.css = self._get_theme_css()
        self.fonts = self._get_theme_fonts()
        self.images = self._get_theme_images()
    
    @abstractmethod
    def _get_theme_css(self) -> str:
        """
        Get the theme's CSS styles.
        
        Returns:
            CSS string
        """
        pass
    
    @abstractmethod
    def _get_theme_fonts(self) -> Dict[str, str]:
        """
        Get the theme's fonts.
        
        Returns:
            Dictionary of font names and URLs
        """
        pass
    
    @abstractmethod
    def _get_theme_images(self) -> Dict[str, str]:
        """
        Get the theme's images and GIFs.
        
        Returns:
            Dictionary of image names and paths
        """
        pass
    
    def apply_theme(self) -> None:
        """
        Apply the theme's styles to the Streamlit app.
        """
        # Apply CSS
        st.markdown(f"<style>{self.css}</style>", unsafe_allow_html=True)
        
        # Apply fonts
        for font_name, font_url in self.fonts.items():
            st.markdown(
                f"""
                <link href="{font_url}" rel="stylesheet">
                <style>
                    .{font_name.lower()}-font {{
                        font-family: '{font_name}', sans-serif;
                    }}
                </style>
                """,
                unsafe_allow_html=True
            )
    
    def display_header(self, title: str) -> None:
        """
        Display a themed header.
        
        Args:
            title: Header title
        """
        st.markdown(
            f"""
            <div class="theme-header">
                <h1>{title}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_subheader(self, title: str) -> None:
        """
        Display a themed subheader.
        
        Args:
            title: Subheader title
        """
        st.markdown(
            f"""
            <div class="theme-subheader">
                <h2>{title}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_info(self, text: str) -> None:
        """
        Display themed information text.
        
        Args:
            text: Information text
        """
        st.markdown(
            f"""
            <div class="theme-info">
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_warning(self, text: str) -> None:
        """
        Display a themed warning.
        
        Args:
            text: Warning text
        """
        st.markdown(
            f"""
            <div class="theme-warning">
                ⚠️ {text}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_success(self, text: str) -> None:
        """
        Display a themed success message.
        
        Args:
            text: Success text
        """
        st.markdown(
            f"""
            <div class="theme-success">
                ✅ {text}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_error(self, text: str) -> None:
        """
        Display a themed error message.
        
        Args:
            text: Error text
        """
        st.markdown(
            f"""
            <div class="theme-error">
                ❌ {text}
            </div>
            """,
            unsafe_allow_html=True
        )
    
    def display_image(self, image_name: str, caption: Optional[str] = None) -> None:
        """
        Display a themed image.
        
        Args:
            image_name: Name of the image in the theme's images dictionary
            caption: Optional image caption
        """
        if image_name in self.images:
            st.image(self.images[image_name], caption=caption)
        else:
            self.display_error(f"Image '{image_name}' not found in theme")
    
    def display_gif(self, gif_name: str, caption: str = None) -> None:
        """
        Display a GIF image with an optional caption.
        
        Args:
            gif_name: Name of the GIF file (must be in self.images)
            caption: Optional caption for the GIF
        """
        try:
            st.image(self.images[gif_name], caption=caption)
        except Exception as e:
            # If image is missing, display a themed message instead
            st.markdown(f"""
                <div style='text-align: center; padding: 20px; border: 2px solid var(--primary-color); border-radius: 10px;'>
                    <h2 style='color: var(--primary-color);'>{caption or 'Theme Image'}</h2>
                    <p style='color: var(--text-color);'>Image placeholder for {self.name} theme</p>
                </div>
            """, unsafe_allow_html=True)
    
    def get_model(self, model_type: str) -> Any:
        """
        Get a model instance for the theme.
        
        Args:
            model_type: Type of model ('regression', 'classification', or 'clustering')
            
        Returns:
            Model instance
        """
        if model_type == 'regression':
            return LinearRegressionModel(name=f"{self.name} Linear Regression")
        elif model_type == 'classification':
            return LogisticRegressionModel(name=f"{self.name} Logistic Regression")
        elif model_type == 'clustering':
            return KMeansModel(name=f"{self.name} K-Means Clustering")
        else:
            raise ValueError(f"Unknown model type: {model_type}")
    
    def display_analysis_results(self, data: pd.DataFrame, analysis_type: str, metrics: Dict[str, float] = None) -> None:
        """
        Display themed analysis results with appropriate messaging.
        
        Args:
            data: The analyzed data
            analysis_type: Type of analysis performed
            metrics: Optional dictionary of model metrics
        """
        # Get the theme-specific message based on analysis type
        if analysis_type == 'regression':
            self._get_regression_message(data, metrics)
        elif analysis_type == 'classification':
            self._get_classification_message(data, metrics)
        else:  # clustering
            self._get_clustering_message(data, metrics)
    
    def _get_regression_message(self, data: pd.DataFrame, metrics: Dict[str, float]) -> None:
        self.display_info("Regression analysis completed. Check the charts above for detailed results.")
    
    def _get_classification_message(self, data: pd.DataFrame, metrics: Dict[str, float]) -> None:
        self.display_info("Classification analysis completed. Check the charts above for detailed results.")
    
    def _get_clustering_message(self, data: pd.DataFrame, metrics: Dict[str, float]) -> None:
        self.display_info("Clustering analysis completed. Check the charts above for detailed results.")
    
    def run_analysis(self, data: pd.DataFrame, analysis_type: str = 'regression'):
        """Run the selected analysis type on the data."""
        try:
            # Data cleaning and debugging output
            st.write('Data head:', data.head())
            st.write('Data dtypes:', data.dtypes)
            st.write('Data index:', data.index)
            # Flatten MultiIndex columns if present
            if isinstance(data.columns, pd.MultiIndex):
                data.columns = ['_'.join([str(level) for level in col if str(level) != '']) for col in data.columns.values]
            # Print and clean columns
            st.write('Data columns:', data.columns)
            data.columns = data.columns.str.strip()
            # Optionally, rename columns if needed (only if not already correct)
            expected_cols = ['Open', 'High', 'Low', 'Close', 'Volume']
            if not all(col in data.columns for col in expected_cols):
                # Try to rename first 5 columns if not matching
                rename_map = {data.columns[i]: expected_cols[i] for i in range(min(5, len(data.columns)))}
                data = data.rename(columns=rename_map)
            # Ensure numeric types
            for col in expected_cols:
                if col in data.columns:
                    data[col] = pd.to_numeric(data[col], errors='coerce')
            data = data[expected_cols].dropna()
            if not isinstance(data.index, pd.DatetimeIndex):
                data.index = pd.to_datetime(data.index)

            # Prepare data based on analysis type
            X, y, valid_dates = data_loader.prepare_ml_data(
                data,
                analysis_type=analysis_type
            )
            # Get visualization data
            viz_data = data_loader.get_visualization_data(data)

            # Display market overview
            st.subheader("Market Overview")
            col1, col2, col3 = st.columns(3)

            with col1:
                # Price and Volume Chart using ThemeVisualizer
                visualizer = ThemeVisualizer(theme=self.name)
                fig = visualizer.create_candlestick_chart(data, title="Price and Volume", show_volume=True)
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Returns Distribution
                fig = go.Figure()
                fig.add_trace(go.Histogram(
                    x=viz_data['returns_data']['Daily_Return'].dropna(),
                    nbinsx=50,
                    name='Daily Returns'
                ))
                fig.update_layout(
                    title='Returns Distribution',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col3:
                # Volatility Chart
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=viz_data['volatility_data'].index,
                    y=viz_data['volatility_data']['Volatility'],
                    name='Volatility'
                ))
                fig.update_layout(
                    title='Price Volatility',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            # Technical Analysis
            st.subheader("Technical Analysis")
            col1, col2 = st.columns(2)
            
            with col1:
                # Bollinger Bands
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=viz_data['bollinger_bands'].index,
                    y=viz_data['bollinger_bands']['Close'],
                    name='Price'
                ))
                fig.add_trace(go.Scatter(
                    x=viz_data['bollinger_bands'].index,
                    y=viz_data['bollinger_bands']['BB_Upper'],
                    name='Upper Band',
                    line=dict(dash='dash')
                ))
                fig.add_trace(go.Scatter(
                    x=viz_data['bollinger_bands'].index,
                    y=viz_data['bollinger_bands']['BB_Lower'],
                    name='Lower Band',
                    line=dict(dash='dash')
                ))
                fig.update_layout(
                    title='Bollinger Bands',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # RSI and MACD
                fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)
                
                # RSI
                rsi_data = viz_data['momentum_data']['RSI'].dropna()
                fig.add_trace(
                    go.Scatter(
                        x=rsi_data.index,
                        y=rsi_data,
                        name='RSI',
                        line=dict(color='blue')
                    ),
                    row=1, col=1
                )
                # Add RSI reference lines
                fig.add_hline(y=70, line_dash="dash", line_color="red", row=1, col=1)
                fig.add_hline(y=30, line_dash="dash", line_color="green", row=1, col=1)
                
                # MACD
                macd_data = viz_data['technical_indicators'].dropna()
                fig.add_trace(
                    go.Scatter(
                        x=macd_data.index,
                        y=macd_data['MACD'],
                        name='MACD',
                        line=dict(color='blue')
                    ),
                    row=2, col=1
                )
                fig.add_trace(
                    go.Scatter(
                        x=macd_data.index,
                        y=macd_data['Signal_Line'],
                        name='Signal Line',
                        line=dict(color='orange', dash='dash')
                    ),
                    row=2, col=1
                )
                
                # Update layout
                fig.update_layout(
                    title='RSI and MACD Indicators',
                    height=600,
                    showlegend=True,
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1
                    )
                )
                
                # Update y-axes labels
                fig.update_yaxes(title_text="RSI", row=1, col=1)
                fig.update_yaxes(title_text="MACD", row=2, col=1)
                
                # Add range slider
                fig.update_xaxes(rangeslider_visible=False)
                
                st.plotly_chart(fig, use_container_width=True)
            
            # Correlation Heatmap
            st.subheader("Feature Correlations")
            fig = go.Figure(data=go.Heatmap(
                z=viz_data['correlation_data'].values,
                x=viz_data['correlation_data'].columns,
                y=viz_data['correlation_data'].columns,
                colorscale='RdBu',
                zmin=-1,
                zmax=1
            ))
            fig.update_layout(
                title='Feature Correlation Heatmap',
                height=600
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Run the selected analysis
            if analysis_type == 'regression':
                model = LinearRegressionModel(name=f"{self.name} Linear Regression")
            elif analysis_type == 'classification':
                model = LogisticRegressionModel(name=f"{self.name} Logistic Regression")
            else:  # clustering
                model = KMeansModel(name=f"{self.name} K-Means Clustering")
            
            # Train the model
            model.train(X, y)
            
            # Get predictions
            if analysis_type != 'clustering':
                predictions = model.predict(X)
                
                # Create prediction chart
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=valid_dates,
                    y=y,
                    name='Actual',
                    mode='lines'
                ))
                fig.add_trace(go.Scatter(
                    x=valid_dates,
                    y=predictions,
                    name='Predicted',
                    mode='lines',
                    line=dict(dash='dash')
                ))
                fig.update_layout(
                    title=f'{analysis_type.title()} Analysis Results',
                    height=400
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Display model metrics
                metrics = model.evaluate(X, y)
                st.write("Model Performance Metrics:")
                for metric, value in metrics.items():
                    st.metric(metric.upper(), f"{value:.4f}")
            else:
                # For clustering, show cluster assignments
                clusters = model.predict(X)
                st.write("Cluster Assignments:")
                st.write(pd.Series(clusters).value_counts())
                
                # Visualize clusters (if 2D or 3D)
                if X.shape[1] >= 2:
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(
                        x=X[:, 0],
                        y=X[:, 1],
                        mode='markers',
                        marker=dict(
                            color=clusters,
                            colorscale='Viridis',
                            showscale=True
                        ),
                        name='Clusters'
                    ))
                    fig.update_layout(
                        title='Cluster Visualization',
                        height=400
                    )
                    st.plotly_chart(fig, use_container_width=True)
            
            # After running the analysis and displaying charts, show themed message
            self.display_analysis_results(data, analysis_type, metrics if 'metrics' in locals() else None)
            
        except Exception as e:
            st.error(f"Error in analysis: {str(e)}")
            st.error(f"Detailed error: {traceback.format_exc()}")
    
    def run_theme(self) -> None:
        """
        Run the theme's main interface.
        """
        # Apply theme
        self.apply_theme()
        
        # Display theme header
        self.display_header(f"{self.name} Theme")
        
        # Add theme-specific content
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
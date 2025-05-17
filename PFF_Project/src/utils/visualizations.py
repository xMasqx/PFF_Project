import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
from typing import Dict, List, Optional, Tuple

class ThemeVisualizer:
    def __init__(self, theme: str):
        """
        Initialize the visualizer with a specific theme.
        
        Args:
            theme: One of 'zombie', 'futuristic', 'got', or 'gaming'
        """
        self.theme = theme
        self.theme_colors = {
            'zombie': {
                'primary': '#2d2d2d',
                'secondary': '#4a0000',
                'accent': '#e0e0e0',
                'background': '#1a1a1a',
                'text': '#e0e0e0'
            },
            'futuristic': {
                'primary': '#00ff9d',
                'secondary': '#0066ff',
                'accent': '#ff00ff',
                'background': '#000000',
                'text': '#ffffff'
            },
            'got': {
                'primary': '#8b0000',
                'secondary': '#4682b4',
                'accent': '#d4af37',
                'background': '#2f4f4f',
                'text': '#ffffff'
            },
            'gaming': {
                'primary': '#ff00ff',
                'secondary': '#00ff00',
                'accent': '#ffff00',
                'background': '#000000',
                'text': '#ffffff'
            }
        }
        
        self.colors = self.theme_colors.get(theme, self.theme_colors['futuristic'])
    
    def create_candlestick_chart(
        self,
        data: pd.DataFrame,
        title: str = "Stock Price",
        show_volume: bool = True
    ) -> go.Figure:
        """
        Create a themed candlestick chart with optional volume.
        
        Args:
            data: DataFrame with OHLCV data
            title: Chart title
            show_volume: Whether to show volume subplot
            
        Returns:
            Plotly figure object
        """
        if show_volume:
            fig = make_subplots(
                rows=2, cols=1,
                shared_xaxes=True,
                vertical_spacing=0.03,
                row_heights=[0.7, 0.3]
            )
        else:
            fig = go.Figure()
        
        # Add candlestick
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name='Price',
                increasing_line_color=self.colors['secondary'],
                decreasing_line_color=self.colors['primary']
            ),
            row=1, col=1 if show_volume else None
        )
        
        if show_volume:
            # Ensure index is unique to avoid ambiguous Series comparison
            if not data.index.is_unique:
                data = data.reset_index(drop=True)
            # Add volume bars
            colors = [
                'red' if float(row['Close']) < float(row['Open']) else 'green'
                for _, row in data.iterrows()
            ]
            fig.add_trace(
                go.Bar(
                    x=data.index,
                    y=data['Volume'],
                    name='Volume',
                    marker_color=colors
                ),
                row=2, col=1
            )
        
        # Update layout
        fig.update_layout(
            title=title,
            template='plotly_dark',
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            font=dict(color=self.colors['text']),
            xaxis_rangeslider_visible=False,
            height=800 if show_volume else 600
        )
        
        return fig
    
    def create_technical_indicators_chart(
        self,
        data: pd.DataFrame,
        indicators: List[str] = ['SMA_20', 'SMA_50', 'RSI', 'MACD']
    ) -> go.Figure:
        """
        Create a chart with technical indicators.
        
        Args:
            data: DataFrame with price and indicator data
            indicators: List of indicators to show
            
        Returns:
            Plotly figure object
        """
        n_indicators = len(indicators)
        fig = make_subplots(
            rows=n_indicators + 1,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            row_heights=[0.4] + [0.6/n_indicators] * n_indicators
        )
        
        # Add price candlestick
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name='Price',
                increasing_line_color=self.colors['secondary'],
                decreasing_line_color=self.colors['primary']
            ),
            row=1, col=1
        )
        
        # Add indicators
        for i, indicator in enumerate(indicators, 2):
            if indicator in ['SMA_20', 'SMA_50', 'EMA_20', 'EMA_50']:
                fig.add_trace(
                    go.Scatter(
                        x=data.index,
                        y=data[indicator],
                        name=indicator,
                        line=dict(color=self.colors['accent'])
                    ),
                    row=1, col=1
                )
            elif indicator == 'RSI':
                fig.add_trace(
                    go.Scatter(
                        x=data.index,
                        y=data[indicator],
                        name='RSI',
                        line=dict(color=self.colors['accent'])
                    ),
                    row=i, col=1
                )
                # Add RSI levels
                fig.add_hline(y=70, line_dash="dash", line_color="red", row=i, col=1)
                fig.add_hline(y=30, line_dash="dash", line_color="green", row=i, col=1)
            elif indicator == 'MACD':
                fig.add_trace(
                    go.Scatter(
                        x=data.index,
                        y=data['MACD'],
                        name='MACD',
                        line=dict(color=self.colors['accent'])
                    ),
                    row=i, col=1
                )
                fig.add_trace(
                    go.Scatter(
                        x=data.index,
                        y=data['Signal_Line'],
                        name='Signal Line',
                        line=dict(color=self.colors['secondary'])
                    ),
                    row=i, col=1
                )
        
        # Update layout
        fig.update_layout(
            title="Technical Analysis",
            template='plotly_dark',
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            font=dict(color=self.colors['text']),
            xaxis_rangeslider_visible=False,
            height=1000
        )
        
        return fig
    
    def create_prediction_chart(
        self,
        actual: pd.Series,
        predicted: pd.Series,
        title: str = "Price Prediction"
    ) -> go.Figure:
        """
        Create a chart comparing actual vs predicted values.
        
        Args:
            actual: Series of actual values
            predicted: Series of predicted values
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        fig = go.Figure()
        
        # Add actual values
        fig.add_trace(
            go.Scatter(
                x=actual.index,
                y=actual.values,
                name='Actual',
                line=dict(color=self.colors['secondary'])
            )
        )
        
        # Add predicted values
        fig.add_trace(
            go.Scatter(
                x=predicted.index,
                y=predicted.values,
                name='Predicted',
                line=dict(color=self.colors['accent'], dash='dash')
            )
        )
        
        # Update layout
        fig.update_layout(
            title=title,
            template='plotly_dark',
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            font=dict(color=self.colors['text']),
            xaxis_title="Date",
            yaxis_title="Price",
            height=600
        )
        
        return fig
    
    def create_cluster_chart(
        self,
        data: pd.DataFrame,
        clusters: np.ndarray,
        x_col: str,
        y_col: str,
        title: str = "Cluster Analysis"
    ) -> go.Figure:
        """
        Create a scatter plot showing clusters.
        
        Args:
            data: DataFrame with the data
            clusters: Array of cluster assignments
            x_col: Column name for x-axis
            y_col: Column name for y-axis
            title: Chart title
            
        Returns:
            Plotly figure object
        """
        fig = px.scatter(
            data,
            x=x_col,
            y=y_col,
            color=clusters.astype(str),
            title=title,
            template='plotly_dark'
        )
        
        # Update layout
        fig.update_layout(
            paper_bgcolor=self.colors['background'],
            plot_bgcolor=self.colors['background'],
            font=dict(color=self.colors['text'])
        )
        
        return fig

# Create theme-specific visualizers
zombie_visualizer = ThemeVisualizer('zombie')
futuristic_visualizer = ThemeVisualizer('futuristic')
got_visualizer = ThemeVisualizer('got')
gaming_visualizer = ThemeVisualizer('gaming') 
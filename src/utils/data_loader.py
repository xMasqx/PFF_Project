import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
from typing import Tuple, Optional

class DataLoader:
    def __init__(self):
        self.cache = {}  # Simple cache for storing downloaded data
    
    def load_stock_data(
        self,
        symbol: str,
        start_date: datetime,
        end_date: datetime,
        force_refresh: bool = False
    ) -> pd.DataFrame:
        """
        Load stock data from Yahoo Finance with caching.
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL')
            start_date: Start date for data
            end_date: End date for data
            force_refresh: Whether to force refresh the data from Yahoo Finance
            
        Returns:
            DataFrame containing stock data
        """
        cache_key = f"{symbol}_{start_date.date()}_{end_date.date()}"
        
        if not force_refresh and cache_key in self.cache:
            return self.cache[cache_key].copy()
        
        try:
            # Download data and ensure index is datetime
            data = yf.download(symbol, start=start_date, end=end_date)
            if data.empty:
                raise ValueError(f"No data found for symbol {symbol}")
            
            # Ensure index is datetime and sorted
            data.index = pd.to_datetime(data.index)
            data = data.sort_index()
            
            # Reset index to ensure clean state
            data = data.reset_index()
            data['Date'] = pd.to_datetime(data['Date'])
            data = data.set_index('Date')
            
            # Cache the processed data
            self.cache[cache_key] = data.copy()
            return data
            
        except Exception as e:
            raise Exception(f"Error downloading data for {symbol}: {str(e)}")
    
    def _create_price_movement_classes(self, prices: np.ndarray, threshold: float = 0.01) -> np.ndarray:
        """
        Convert continuous price data into discrete classes based on price movements.
        
        Args:
            prices: Array of price values
            threshold: Minimum percentage change to consider as a movement
            
        Returns:
            Array of class labels (0: down, 1: stable, 2: up)
        """
        # Calculate percentage changes
        pct_change = np.diff(prices) / prices[:-1]
        
        # Create classes based on threshold
        classes = np.zeros(len(prices))
        classes[1:] = np.where(pct_change > threshold, 2,  # Up
                     np.where(pct_change < -threshold, 0,  # Down
                     1))  # Stable
        
        return classes

    def prepare_ml_data(
        self,
        data: pd.DataFrame,
        target_column: str = 'Close',
        feature_columns: Optional[list] = None,
        prediction_days: int = 1,
        analysis_type: str = 'regression'
    ) -> Tuple[np.ndarray, np.ndarray, pd.DatetimeIndex]:
        """
        Prepare data for machine learning models.
        
        Args:
            data: DataFrame containing stock data
            target_column: Column to use as target variable
            feature_columns: Columns to use as features (if None, uses all numeric columns)
            prediction_days: Number of days to predict ahead
            analysis_type: Type of analysis ('regression', 'classification', or 'clustering')
            
        Returns:
            Tuple of (X, y, dates) for machine learning, where dates is the index of valid samples
        """
        # Ensure we're working with a copy and the index is datetime
        df = data.copy()
        if not isinstance(df.index, pd.DatetimeIndex):
            df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        
        if feature_columns is None:
            # Exclude target column from features if it's not explicitly included
            feature_columns = [col for col in df.select_dtypes(include=[np.number]).columns 
                             if col != target_column]
        
        # Create target variable (shifted by prediction_days)
        shifted_target = df[target_column].shift(-prediction_days)
        # Ensure shifted_target is a Series (1D)
        if isinstance(shifted_target, pd.DataFrame):
            shifted_target = shifted_target.iloc[:, 0]
        y = pd.Series(shifted_target, name=target_column, index=df.index)
        
        # Create features matrix
        X = df[feature_columns].copy()
        
        # Drop rows with NaN values
        valid_data = pd.concat([X, y.to_frame()], axis=1).dropna()
        
        # Get the valid dates
        valid_dates = valid_data.index
        
        # Convert to numpy arrays
        X_array = valid_data[feature_columns].values
        y_array = valid_data[target_column].values
        
        # Process target variable based on analysis type
        if analysis_type == 'classification':
            y_array = self._create_price_movement_classes(y_array)
        elif analysis_type == 'clustering':
            # For clustering, we don't need a target variable
            y_array = None
        
        # Verify shapes match for regression and classification
        if analysis_type != 'clustering' and X_array.shape[0] != y_array.shape[0]:
            raise ValueError(f"Feature and target shapes don't match: X={X_array.shape}, y={y_array.shape}")
        
        return X_array, y_array, valid_dates
    
    def calculate_technical_indicators(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Calculate common technical indicators for the stock data.
        
        Args:
            data: DataFrame containing stock data
            
        Returns:
            DataFrame with additional technical indicators
        """
        # Ensure we're working with a copy and the index is datetime
        df = data.copy()
        if not isinstance(df.index, pd.DatetimeIndex):
            df.index = pd.to_datetime(df.index)
        df = df.sort_index()
        
        # Ensure numeric columns are float32 instead of float64 for better PyArrow compatibility
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = df[col].astype('float32')
        
        # Simple Moving Averages
        df['SMA_20'] = df['Close'].rolling(window=20).mean().astype('float32')
        df['SMA_50'] = df['Close'].rolling(window=50).mean().astype('float32')
        
        # Exponential Moving Averages
        df['EMA_20'] = df['Close'].ewm(span=20, adjust=False).mean().astype('float32')
        df['EMA_50'] = df['Close'].ewm(span=50, adjust=False).mean().astype('float32')
        
        # Relative Strength Index (RSI)
        delta = df['Close'].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        # Calculate average gain and loss
        avg_gain = gain.rolling(window=14).mean()
        avg_loss = loss.rolling(window=14).mean()
        
        # Calculate RS and RSI
        rs = avg_gain / avg_loss
        df['RSI'] = (100 - (100 / (1 + rs))).astype('float32')
        
        # Moving Average Convergence Divergence (MACD)
        # Calculate the 12 and 26 day EMAs
        ema12 = df['Close'].ewm(span=12, adjust=False).mean()
        ema26 = df['Close'].ewm(span=26, adjust=False).mean()
        
        # Calculate MACD line
        df['MACD'] = (ema12 - ema26).astype('float32')
        
        # Calculate Signal line (9-day EMA of MACD)
        df['Signal_Line'] = df['MACD'].ewm(span=9, adjust=False).mean().astype('float32')
        
        # Bollinger Bands
        close_series = df['Close']
        bb_window = 20
        bb_middle = close_series.rolling(window=bb_window).mean()
        bb_std = close_series.rolling(window=bb_window).std()
        
        # Calculate bands using Series operations
        df['BB_Middle'] = bb_middle.astype('float32')
        df['BB_Upper'] = (bb_middle + (2.0 * bb_std)).astype('float32')
        df['BB_Lower'] = (bb_middle - (2.0 * bb_std)).astype('float32')
        
        # Additional indicators
        # Average True Range (ATR)
        high_low = df['High'] - df['Low']
        high_close = np.abs(df['High'] - df['Close'].shift())
        low_close = np.abs(df['Low'] - df['Close'].shift())
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        df['ATR'] = true_range.rolling(window=14).mean().astype('float32')
        
        # On-Balance Volume (OBV)
        df['OBV'] = (np.sign(df['Close'].diff()) * df['Volume']).fillna(0).cumsum().astype('float32')
        
        # Clean up NaN values using bfill and ffill
        df = df.bfill().ffill()
        
        # Ensure all numeric columns are float32
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = df[col].astype('float32')
        
        return df
    
    def load_kragle_dataset(self, file_path: str) -> pd.DataFrame:
        """
        Load a dataset from Kragle.
        
        Args:
            file_path: Path to the Kragle dataset file
            
        Returns:
            DataFrame containing the dataset
        """
        try:
            # Add support for different file formats
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            elif file_path.endswith('.xlsx'):
                return pd.read_excel(file_path)
            else:
                raise ValueError("Unsupported file format. Please use .csv or .xlsx files.")
        except Exception as e:
            raise Exception(f"Error loading Kragle dataset: {str(e)}")

    def get_visualization_data(self, data: pd.DataFrame) -> dict:
        """
        Prepare data for various visualizations.
        
        Args:
            data: DataFrame containing stock data
            
        Returns:
            Dictionary containing data for different visualizations
        """
        df = data.copy()
        
        # Ensure numeric columns are float32
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        for col in numeric_cols:
            df[col] = df[col].astype('float32')
        
        # Calculate daily returns
        df['Daily_Return'] = df['Close'].pct_change().astype('float32')
        
        # Calculate cumulative returns
        df['Cumulative_Return'] = ((1 + df['Daily_Return']).cumprod() - 1).astype('float32')
        
        # Calculate volatility (20-day rolling standard deviation)
        df['Volatility'] = df['Daily_Return'].rolling(window=20).std().astype('float32')
        
        # Calculate trading volume moving average
        df['Volume_MA'] = df['Volume'].rolling(window=20).mean().astype('float32')
        
        # Calculate price momentum (12-day rate of change)
        df['Momentum'] = df['Close'].pct_change(periods=12).astype('float32')
        
        # Calculate price ranges
        df['Daily_Range'] = ((df['High'] - df['Low']) / df['Close']).astype('float32')
        
        # Calculate technical indicators
        df = self.calculate_technical_indicators(df)
        
        # Prepare correlation data
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        correlation_data = df[numeric_cols].corr().astype('float32')
        
        # Ensure all returned DataFrames use float32
        return {
            'price_data': df[['Close', 'High', 'Low']].astype('float32'),
            'volume_data': df[['Volume', 'Volume_MA']].astype('float32'),
            'returns_data': df[['Daily_Return', 'Cumulative_Return']].astype('float32'),
            'volatility_data': df[['Volatility', 'Daily_Range']].astype('float32'),
            'momentum_data': df[['Momentum', 'RSI']].astype('float32'),
            'technical_indicators': df[['SMA_20', 'SMA_50', 'EMA_20', 'EMA_50', 'MACD', 'Signal_Line']].astype('float32'),
            'correlation_data': correlation_data,
            'bollinger_bands': df[['Close', 'BB_Upper', 'BB_Middle', 'BB_Lower']].astype('float32')
        }

# Create a singleton instance
data_loader = DataLoader() 
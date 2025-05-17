from .base_model import BaseModel
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from typing import Optional, Tuple

class LinearRegressionModel(BaseModel):
    def __init__(self, name: str = "Linear Regression"):
        """
        Initialize the linear regression model.
        
        Args:
            name: Name of the model
        """
        super().__init__(name)
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.model_type = 'regression'
        self.feature_names = None
    
    def train(
        self,
        X: np.ndarray,
        y: np.ndarray,
        feature_names: Optional[list] = None,
        **kwargs
    ) -> None:
        """
        Train the linear regression model.
        
        Args:
            X: Training features
            y: Training target
            feature_names: Optional list of feature names
            **kwargs: Additional training parameters
        """
        # Store feature names if provided
        self.feature_names = feature_names
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train model
        self.model.fit(X_scaled, y)
        self.is_fitted = True
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the linear regression model.
        
        Args:
            X: Features to predict on
            
        Returns:
            Array of predictions
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before making predictions")
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Make predictions
        return self.model.predict(X_scaled)
    
    def get_coefficients(self) -> Tuple[np.ndarray, Optional[list]]:
        """
        Get the model coefficients.
        
        Returns:
            Tuple of (coefficients, feature_names)
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting coefficients")
        
        return self.model.coef_, self.feature_names
    
    def get_intercept(self) -> float:
        """
        Get the model intercept.
        
        Returns:
            Model intercept
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting intercept")
        
        return self.model.intercept_ 
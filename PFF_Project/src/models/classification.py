from .base_model import BaseModel
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from typing import Optional, Tuple

class LogisticRegressionModel(BaseModel):
    def __init__(
        self,
        name: str = "Logistic Regression",
        max_iter: int = 1000,
        C: float = 1.0
    ):
        """
        Initialize the logistic regression model.
        
        Args:
            name: Name of the model
            max_iter: Maximum number of iterations
            C: Inverse of regularization strength
        """
        super().__init__(name)
        self.model = LogisticRegression(max_iter=max_iter, C=C)
        self.scaler = StandardScaler()
        self.model_type = 'classification'
        self.feature_names = None
    
    def train(
        self,
        X: np.ndarray,
        y: np.ndarray,
        feature_names: Optional[list] = None,
        **kwargs
    ) -> None:
        """
        Train the logistic regression model.
        
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
        Make predictions using the logistic regression model.
        
        Args:
            X: Features to predict on
            
        Returns:
            Array of predicted classes
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before making predictions")
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Make predictions
        return self.model.predict(X_scaled)
    
    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        """
        Get probability estimates for each class.
        
        Args:
            X: Features to predict on
            
        Returns:
            Array of probability estimates
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before making predictions")
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Get probability estimates
        return self.model.predict_proba(X_scaled)
    
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
    
    def get_classes(self) -> np.ndarray:
        """
        Get the unique classes in the training data.
        
        Returns:
            Array of unique classes
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting classes")
        
        return self.model.classes_ 
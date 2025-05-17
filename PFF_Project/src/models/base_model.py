from abc import ABC, abstractmethod
import numpy as np
import pandas as pd
from typing import Tuple, Optional, Dict, Any
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, silhouette_score

class BaseModel(ABC):
    def __init__(self, name: str):
        """
        Initialize the base model.
        
        Args:
            name: Name of the model
        """
        self.name = name
        self.model = None
        self.is_fitted = False
    
    @abstractmethod
    def train(self, X: np.ndarray, y: np.ndarray, **kwargs) -> None:
        """
        Train the model.
        
        Args:
            X: Training features
            y: Training target
            **kwargs: Additional training parameters
        """
        pass
    
    @abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using the model.
        
        Args:
            X: Features to predict on
            
        Returns:
            Array of predictions
        """
        pass
    
    def evaluate(self, X: np.ndarray, y: np.ndarray) -> Dict[str, float]:
        """
        Evaluate the model's performance.
        
        Args:
            X: Test features
            y: True target values
            
        Returns:
            Dictionary of evaluation metrics
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before evaluation")
        
        predictions = self.predict(X)
        
        # Calculate appropriate metrics based on model type
        metrics = {}
        
        if hasattr(self, 'model_type'):
            if self.model_type == 'regression':
                metrics['mse'] = mean_squared_error(y, predictions)
                metrics['r2'] = r2_score(y, predictions)
            elif self.model_type == 'classification':
                metrics['accuracy'] = accuracy_score(y, predictions)
            elif self.model_type == 'clustering':
                metrics['silhouette'] = silhouette_score(X, predictions)
        
        return metrics
    
    def save_model(self, path: str) -> None:
        """
        Save the model to disk.
        
        Args:
            path: Path to save the model
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before saving")
        
        import joblib
        joblib.dump(self.model, path)
    
    def load_model(self, path: str) -> None:
        """
        Load the model from disk.
        
        Args:
            path: Path to load the model from
        """
        import joblib
        self.model = joblib.load(path)
        self.is_fitted = True
    
    def get_feature_importance(self) -> Optional[pd.Series]:
        """
        Get feature importance if available.
        
        Returns:
            Series of feature importances or None if not available
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting feature importance")
        
        if hasattr(self.model, 'feature_importances_'):
            return pd.Series(
                self.model.feature_importances_,
                index=self.feature_names if hasattr(self, 'feature_names') else None
            )
        elif hasattr(self.model, 'coef_'):
            return pd.Series(
                self.model.coef_,
                index=self.feature_names if hasattr(self, 'feature_names') else None
            )
        return None
    
    def get_model_params(self) -> Dict[str, Any]:
        """
        Get the model's parameters.
        
        Returns:
            Dictionary of model parameters
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting parameters")
        
        return self.model.get_params() if hasattr(self.model, 'get_params') else {} 
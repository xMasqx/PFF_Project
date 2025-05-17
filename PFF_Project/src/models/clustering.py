from .base_model import BaseModel
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from typing import Optional, Tuple
from sklearn.metrics import silhouette_score

class KMeansModel(BaseModel):
    def __init__(
        self,
        name: str = "K-Means Clustering",
        n_clusters: int = 3,
        max_iter: int = 300,
        random_state: Optional[int] = None
    ):
        """
        Initialize the K-means clustering model.
        
        Args:
            name: Name of the model
            n_clusters: Number of clusters
            max_iter: Maximum number of iterations
            random_state: Random state for reproducibility
        """
        super().__init__(name)
        self.model = KMeans(
            n_clusters=n_clusters,
            max_iter=max_iter,
            random_state=random_state
        )
        self.scaler = StandardScaler()
        self.model_type = 'clustering'
        self.feature_names = None
    
    def train(
        self,
        X: np.ndarray,
        y: Optional[np.ndarray] = None,  # Not used in clustering
        feature_names: Optional[list] = None,
        **kwargs
    ) -> None:
        """
        Train the K-means clustering model.
        
        Args:
            X: Training features
            y: Not used in clustering
            feature_names: Optional list of feature names
            **kwargs: Additional training parameters
        """
        # Store feature names if provided
        self.feature_names = feature_names
        
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train model
        self.model.fit(X_scaled)
        self.is_fitted = True
    
    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Predict cluster assignments for new data.
        
        Args:
            X: Features to predict on
            
        Returns:
            Array of cluster assignments
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before making predictions")
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Make predictions
        return self.model.predict(X_scaled)
    
    def get_cluster_centers(self) -> np.ndarray:
        """
        Get the cluster centers.
        
        Returns:
            Array of cluster centers
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting cluster centers")
        
        return self.scaler.inverse_transform(self.model.cluster_centers_)
    
    def get_inertia(self) -> float:
        """
        Get the model's inertia (within-cluster sum of squares).
        
        Returns:
            Model inertia
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before getting inertia")
        
        return self.model.inertia_
    
    def get_silhouette_score(self, X: np.ndarray) -> float:
        """
        Calculate the silhouette score for the clustering.
        
        Args:
            X: Features to calculate score on
            
        Returns:
            Silhouette score
        """
        if not self.is_fitted:
            raise ValueError("Model must be trained before calculating silhouette score")
        
        # Scale features
        X_scaled = self.scaler.transform(X)
        
        # Get predictions
        labels = self.model.predict(X_scaled)
        
        # Calculate silhouette score
        return silhouette_score(X_scaled, labels)
    
    def find_optimal_clusters(
        self,
        X: np.ndarray,
        max_clusters: int = 10,
        metric: str = 'silhouette'
    ) -> Tuple[int, float]:
        """
        Find the optimal number of clusters using the specified metric.
        
        Args:
            X: Features to analyze
            max_clusters: Maximum number of clusters to try
            metric: Metric to use ('silhouette' or 'inertia')
            
        Returns:
            Tuple of (optimal number of clusters, best score)
        """
        # Scale features
        X_scaled = self.scaler.fit_transform(X)
        
        best_score = float('-inf') if metric == 'silhouette' else float('inf')
        best_n_clusters = 2
        
        for n_clusters in range(2, max_clusters + 1):
            # Create and fit model
            kmeans = KMeans(
                n_clusters=n_clusters,
                random_state=self.model.random_state
            )
            labels = kmeans.fit_predict(X_scaled)
            
            # Calculate score
            if metric == 'silhouette':
                score = silhouette_score(X_scaled, labels)
                if score > best_score:
                    best_score = score
                    best_n_clusters = n_clusters
            else:  # inertia
                score = kmeans.inertia_
                if score < best_score:
                    best_score = score
                    best_n_clusters = n_clusters
        
        return best_n_clusters, best_score 
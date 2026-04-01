import numpy as np


class StandardScalerScratch:

    # Standardizes features using: (X - mean) / std


    def __init__(self):
        self.means = None
        self.stds = None

    def fit(self, X: np.ndarray):
        
        # Compute mean and std for each feature.
        self.means = np.mean(X, axis=0)
        self.stds = np.std(X, axis=0)

        # Prevent division by zero
        self.stds[self.stds == 0] = 1

    def transform(self, X: np.ndarray) -> np.ndarray:
        
       # Apply standardization.
        return (X - self.means) / self.stds

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        
        # Fit + transform in one step.
        self.fit(X)
        return self.transform(X)
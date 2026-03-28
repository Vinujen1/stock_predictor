import numpy as np


class LinearRegressionScratch:
    """
    A from-scratch implementation of Linear Regression
    using Gradient Descent.
    """

    def __init__(self, learning_rate: float = 0.01, n_iterations: int = 1000):
        # Step size for gradient descent
        self.learning_rate = learning_rate

        # Number of training loops
        self.n_iterations = n_iterations

        # Model parameters to learn
        self.weights = None
        self.bias = None

        # Store training loss over time
        self.loss_history = []

    def fit(self, X: np.ndarray, y: np.ndarray):
        """
        Train the model using gradient descent.

        Parameters:
            X: Feature matrix of shape (n_samples, n_features)
            y: Target vector of shape (n_samples,)
        """
        n_samples, n_features = X.shape

        # Initialize weights and bias to zero
        self.weights = np.zeros(n_features)
        self.bias = 0.0

        # Gradient descent loop
        for _ in range(self.n_iterations):
            # Compute current predictions
            y_pred = self.predict(X)

            # Compute error
            error = y_pred - y

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, error)
            db = (1 / n_samples) * np.sum(error)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Compute and store loss
            loss = np.mean(error ** 2)
            self.loss_history.append(loss)

    def predict(self, X: np.ndarray) -> np.ndarray:
        """
        Make predictions using learned weights and bias.
        """
        return np.dot(X, self.weights) + self.bias

    def mse(self, y_true: np.ndarray, y_pred: np.ndarray) -> float:
        """
        Compute Mean Squared Error.
        """
        return np.mean((y_true - y_pred) ** 2)
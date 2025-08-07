import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create a synthetic dataset for regression
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 random data points
y = 4 + 3 * X + np.random.randn(100, 1)  # Linear relation with some noise

# Split the dataset into training and validation sets (80% training, 20% validation)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training set size:", len(X_train))
print("Validation set size:", len(X_val))

# Initialize the model
model = LinearRegression()

# Implement 5-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
mse_scores = []

for train_index, val_index in kf.split(X):
    X_train_cv, X_val_cv = X[train_index], X[val_index]
    y_train_cv, y_val_cv = y[train_index], y[val_index]

    # Train the model
    model.fit(X_train_cv, y_train_cv)

    # Make predictions
    y_pred = model.predict(X_val_cv)

    # Calculate the Mean Squared Error for this fold
    mse = mean_squared_error(y_val_cv, y_pred)
    mse_scores.append(mse)

print(f"Mean Squared Error for each fold: {mse_scores}")
print(f"Average MSE across all folds: {np.mean(mse_scores)}")

# Train the model on the entire training set
model.fit(X_train, y_train)

# Make predictions on the validation set
y_pred_val = model.predict(X_val)

# Calculate the MSE on the validation set
mse_val = mean_squared_error(y_val, y_pred_val)

print(f"Mean Squared Error on the validation set: {mse_val}")
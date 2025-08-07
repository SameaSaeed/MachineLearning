import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Load the Iris dataset
url = "iris.csv"  # Adjust the path if the file is located elsewhere
column_names = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
df = pd.read_csv(url, header=None, names=column_names)

# Display the first few rows of the dataset
print(df.head())

# Simulate missing values in the dataset
df.loc[2, 'sepal_length'] = None  # Set a value to None (NaN)
df.loc[5, 'petal_width'] = None

# Display dataset with missing values
print("\nDataset with missing values:")
print(df)

# Handle missing values - Replace NaN with the mean of the column
df['sepal_length'].fillna(df['sepal_length'].mean(), inplace=True)
df['petal_width'].fillna(df['petal_width'].mean(), inplace=True)

# Display the dataset after handling missing values
print("\nDataset after handling missing values:")
print(df)

# Select the numerical columns
numerical_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

# Initialize MinMaxScaler
scaler = MinMaxScaler()

# Normalize the numerical columns
df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

# Display the normalized dataset
print("\nDataset after normalization:")
print(df.head())

# Separate features and target
X = df[numerical_columns]
y = df['class']

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the resulting datasets
print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)
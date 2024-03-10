# -*- coding: utf-8 -*-
"""iNeuron DS Assessment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_eRA2va7ePQcmfjElkYzrzsFX7CqMoli

**Python Questions**

Question: 1


You have an input dictionary given,

input_dict = {"abc":{"def":{"ghi":{"jkl":{"mno":{"pqr":{"stu":{"vwx":{"yz":"you are finally here !!!"}}}}}}}}}

Task:  You have to write a Python function that will take this input and print it like that,

output = {"abc":["def","ghi","jkl","mno","pqr","stu","vwx","yz"],
 "def":["ghi","jkl","mno","pqr","stu","vwx","yz"],
 "ghi":["jkl","mno","pqr","stu","vwx","yz"],
 "jkl":["mno","pqr","stu","vwx","yz"],
 "mno":["pqr","stu","vwx","yz"],
 "pqr":["stu","vwx","yz"],
 "stu":["vwx","yz"],
 "vwx":["yz"],
 "yz":["you are finally here !!!"]}
"""

def construct_output(input_dict, prefix=None):
    output = {}
    if prefix is None:
        prefix = []

    for key, value in input_dict.items():
        if isinstance(value, dict):
            new_prefix = prefix + [key]
            inner_output = construct_output(value, new_prefix)
            output[key] = list(inner_output.keys())
            output.update(inner_output)
        else:
            output[key] = value

    return {"/".join(prefix): output}


input_dict = {
    "abc": {
        "def": {
            "ghi": {
                "jkl": {
                    "mno": {
                        "pqr": {
                            "stu": {
                                "vwx": {
                                    "yz": "you are finally here !!!"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

output = construct_output(input_dict)
print(output)

"""Question: 2
Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an integer ‘K’ which denotes the number of horses that are mad. To prevent the horses from hurting each other, you need to assign the horses to the stalls, such that the minimum distance between any two of them is as large as possible. Return the largest minimum distance.

array: 1,2,4,8,9  &  k=3

O/P: 3

Explanation: 1st horse at stall 1, 2nd horse at stall 4 and 3rd horse at stall 8

"""

def min_distance_between_horses(stalls, k):
    stalls.sort()
    low = 1  # Minimum possible distance
    high = stalls[-1] - stalls[0]  # Maximum possible distance

    while low < high:
        mid = (low + high) // 2
        count = 1  # Number of horses placed so far
        current_stall = stalls[0]  # Current stall being considered

        # Greedily place horses, keeping the minimum distance in mind
        for stall in stalls:
            if stall - current_stall >= mid:
                count += 1
                current_stall = stall
        if count >= k:
            low = mid + 1
        else:
            high = mid

    return low - 1

# Test the function
stalls = [1, 2, 4, 8, 9]
k = 3
print(min_distance_between_horses(stalls, k))  # Output: 3

"""Question 3
Mr. Karthiken works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

             a) Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
              b) The design should have ‘WELCOME’ written in the center.
              c) The design pattern should only use |, . and – characters.

    Sample Design is given above image, Write a python code for this.
"""

def create_door_mat(N, M):
    # Calculate the size of the mat
    middle_row = N // 2
    middle_col = M // 2

    # Print the top part of the mat
    for i in range(middle_row):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

    # Print the center of the mat with 'WELCOME'
    print("WELCOME".center(M, "-"))

    # Print the bottom part of the mat
    for i in range(middle_row - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

# Sample usage
N = 7  # Example odd natural number
M = 3 * N
create_door_mat(N, M)

"""Question 4
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

   a) 0 <= a, b, c, d < n
   b) a, b, c, and d are distinct.
   c) nums[a] + nums[b] + nums[c] + nums[d] == target
"""

def fourSum(nums, target):
    nums.sort()
    quadruplets = []

    n = len(nums)
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets

# Example usage:
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(fourSum(nums, target))

"""**Statistics:**

**Question: 4**

What is correlation? Give an example with a dataset & graphical representation on jupyter Notebook

Solution:
Correlation is a statistical measure that describes the relationship between two variables. It indicates the extent to which changes in one variable are associated with changes in another variable. Correlation values range from -1 to 1, where:

1 indicates a perfect positive correlation: As one variable increases, the other variable also increases proportionally.
-1 indicates a perfect negative correlation: As one variable increases, the other variable decreases proportionally.
0 indicates no correlation: There is no apparent relationship between the variables.
Here's an example dataset and a graphical representation of correlation using a scatter plot in Google colab Notebook:
"""

import numpy as np
import matplotlib.pyplot as plt

# Example dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Independent variable
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])  # Dependent variable

# Calculate correlation coefficient
correlation_coefficient = np.corrcoef(x, y)[0, 1]

# Plot the data
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue')
plt.title(f'Scatter Plot of X vs Y\nCorrelation Coefficient: {correlation_coefficient:.2f}', fontsize=14)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True)
plt.show()

"""In this example, x represents the independent variable, and y represents the dependent variable. Since y is a linear function of x (y = 2x), we expect to see a perfect positive correlation between x and y.

**Machine learning:**

**Question: 1**

Imagine you have a dataset where you have different Instagram features like u sername , Caption , Hashtag , Followers , Time_Since_posted , and likes , now your task is to predict the number of likes and Time Since posted and the rest of the features are your input features. Now you have to build a model which can predict the number of likes and Time Since posted.
Dataset This is the Dataset You can use this dataset for this question.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv("/content/drive/MyDrive/iNeuron/Dataset_Q1/instagram_reach.csv")

# Convert time duration strings to numeric values (e.g., hours)
def convert_time_to_hours(time_str):
    if "hour" in time_str:
        return int(time_str.split()[0])
    elif "day" in time_str:
        return int(time_str.split()[0]) * 24
    else:
        return None

# Apply conversion function to "Time_Since_posted" column
data["Time_since_posted_numeric"] = data["Time_since_posted"].apply(convert_time_to_hours)

# Drop rows with missing or invalid values
data.dropna(subset=["Time_since_posted_numeric"], inplace=True)

# Split features and target variables
X = data.drop(columns=["likes", "Time_since_posted", "Time_since_posted_numeric"])
y_likes = data["likes"]
y_time_since_posted = data["Time_since_posted_numeric"]

# Split the data into training and testing sets
X_train, X_test, y_likes_train, y_likes_test, y_time_train, y_time_test = train_test_split(
    X, y_likes, y_time_since_posted, test_size=0.2, random_state=42
)

# Preprocessing
numeric_features = ["Followers"]
numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

categorical_features = ["Username", "Caption", "Hashtag"]
categorical_transformer = Pipeline(
    steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

# Model for predicting likes
model_likes = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(random_state=42)),
    ]
)

# Model for predicting time since posted
model_time = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(random_state=42)),
    ]
)

# Train the models
model_likes.fit(X_train, y_likes_train)
model_time.fit(X_train, y_time_train)

# Predictions
y_likes_pred = model_likes.predict(X_test)
y_time_pred = model_time.predict(X_test)

# Evaluate the models
mse_likes = mean_squared_error(y_likes_test, y_likes_pred)
mse_time = mean_squared_error(y_time_test, y_time_pred)

print("Mean Squared Error (Likes):", mse_likes)
print("Mean Squared Error (Time Since Posted):", mse_time)

"""** Question: 2**
Train an SVM regressor on : Bengaluru housing dataset

    Must include in details:

  - EDA

  - Feature engineering
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error

# Load the dataset
data = pd.read_csv("/content/drive/MyDrive/iNeuron/Dataset_Q1/Bengaluru_House_Data.csv")

# EDA
print("Shape of the dataset:", data.shape)
print("\nColumns in the dataset:", data.columns)
print("\nSample data:")
print(data.head())
print("\nSummary statistics:")
print(data.describe())
print("\nMissing values:")
print(data.isnull().sum())

# Feature engineering
data.drop(["area_type", "availability", "society", "balcony"], axis=1, inplace=True)

# Handle missing values in 'size' column
data['size'] = data['size'].fillna('0 BHK')

# Preprocess 'size' column
data['size'] = data['size'].apply(lambda x: int(x.split(' ')[0]))

# Preprocess 'total_sqft' column
def preprocess_total_sqft(total_sqft_str):
    try:
        return float(total_sqft_str)
    except:
        tokens = total_sqft_str.split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        else:
            return None

data['total_sqft'] = data['total_sqft'].apply(preprocess_total_sqft)

# Handle missing values
imputer = SimpleImputer(strategy='mean')
data[['size', 'total_sqft', 'bath']] = imputer.fit_transform(data[['size', 'total_sqft', 'bath']])

data = pd.get_dummies(data, columns=["location"])

scaler = StandardScaler()
data[['size', 'total_sqft', 'bath', 'price']] = scaler.fit_transform(data[['size', 'total_sqft', 'bath', 'price']])

X = data.drop(columns=["price"])
y = data["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the SVM regressor
svm_regressor = SVR(kernel='rbf')
svm_regressor.fit(X_train, y_train)

# Make predictions
y_pred = svm_regressor.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

"""**Question: 3**

Train and fine tune a decision tree using the wine dataset by following the following steps:-

  1. Use load_wine() to generate wine dataset
  2. Split the dataset into train and test  dataset
  3. Use random search CV to hyperparameter tune the Decision Tree
  4. Try to achieve an accuracy of at least 85%


Grow a random forest using the following steps:-

  1. Continuing the previous question, create 10 subsets of the training dataset. You can use the ShuffleSplit                class for it.
  2. Train 1 decision tree on each subset, using the best hyperparameter values found in the previous question.
  3. Evaluate all the trees on the test dataset. Are they performing better than the tree created in the previous question?
"""

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split, RandomizedSearchCV, ShuffleSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import randint
import numpy as np

# Step 1: Load the wine dataset
wine = load_wine()
X, y = wine.data, wine.target

# Step 2: Split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Hyperparameter tuning for Decision Tree
param_dist = {
    'max_depth': randint(1, 20),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 20),
    'criterion': ['gini', 'entropy']
}

tree_classifier = DecisionTreeClassifier()
random_search = RandomizedSearchCV(tree_classifier, param_distributions=param_dist, n_iter=100, cv=5, scoring='accuracy', random_state=42)
random_search.fit(X_train, y_train)

print("Best hyperparameters for Decision Tree:", random_search.best_params_)
print("Best accuracy for Decision Tree:", random_search.best_score_)

# Step 4: Train Decision Tree classifier on entire training dataset
best_tree_params = random_search.best_params_
tree_classifier = DecisionTreeClassifier(**best_tree_params)
tree_classifier.fit(X_train, y_train)

# Step 5: Create 10 subsets of training dataset using ShuffleSplit
shuffle_split = ShuffleSplit(n_splits=10, test_size=0.2, random_state=42)

# Step 6: Train 10 Decision Tree classifiers on each subset
forest_classifiers = []
for train_index, _ in shuffle_split.split(X_train):
    X_subset, y_subset = X_train[train_index], y_train[train_index]
    tree = DecisionTreeClassifier(**best_tree_params)
    tree.fit(X_subset, y_subset)
    forest_classifiers.append(tree)

# Step 7: Evaluate all trees on the test dataset
test_accuracy = []
for tree in forest_classifiers:
    y_pred = tree.predict(X_test)
    test_accuracy.append(accuracy_score(y_test, y_pred))

print("Test accuracy for each tree in the forest:", test_accuracy)
print("Mean test accuracy for the forest:", np.mean(test_accuracy))

"""**Deep Learning :**

**Question: 2**

Train a Pure ANN with less than 10000 trainable parameters using the MNIST Dataset
"""

import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

# Load the MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the pixel values to the range [0, 1]
x_train, x_test = x_train / 255.0, x_test / 255.0

# Flatten the input images
x_train = x_train.reshape((x_train.shape[0], -1))
x_test = x_test.reshape((x_test.shape[0], -1))

# Define the model architecture
model = Sequential([
    Dense(128, activation='relu', input_shape=(784,)),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Print the model summary
model.summary()

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Test accuracy:", test_accuracy)

"""Question: 3

Perform Regression Task using ANN

Note: You are feel free to use any Regression ML dataset
"""

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the Boston Housing dataset
(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

# Normalize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the model architecture
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dropout(0.5),
    Dense(1)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=0)

# Evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
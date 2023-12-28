import numpy as np

# This function generates a random matrix of a given shape. The values in the matrix are uniformly distributed between 0.0 and 1.0.
# Parameters:
# size_in: int, Number of rows in the output matrix
# size_out: int, Number of columns in the output matrix
# Returns: np.ndarray, A matrix of shape (size_in, size_out) with random values

def random_init(size_in, size_out):
    return np.random.uniform(0.0, 1.0, size=(size_in, size_out))

# This function counts the occurrences of each unique value in the input array y and prints them.
# Parameters:
# y: np.ndarray, Input array of target values
# Returns: None

def count_occurances(y):
    arr = np.unique(y, return_counts=True)
    for i in range(len(arr[0])):
        print("class ", arr[0][i], " has ", arr[1][i], " items")

# This function prints the shapes of the input arrays X and y.
# Parameters:
# X: np.ndarray, Input array of features
# y: np.ndarray, Input array of target values
# Returns: None

def print_shape(X, y):
    print("X shape is ", X.shape)
    print("y shape is ", y.shape)

# This function generates a random n-class classification problem.
# Parameters:
# n_samples: int, Number of samples
# n_features: int, Number of features
# n_classes: int, Number of classes
# noise: float, Standard deviation of Gaussian noise added to the features
# balanced: bool, Whether to generate balanced samples
# random_state: int, Seed for the random number generator
# init: function, Function to initialize weights and bias
# Returns: tuple, A tuple containing the feature matrix X and the target vector y

def make_classification(n_samples=101, n_features=20, n_classes=2, noise=0.0, balanced=True, random_state=None, init = random_init):
    # Select random state
    np.random.seed(random_state)

    # Create balanaced or unbalanced samples
    size = n_samples // n_classes
    rest = n_samples % n_classes
    prob = np.random.uniform(size=(n_classes))
    prob = np.where(balanced == True, [1/n_classes] * n_classes, prob / sum(prob))

    # Generate target values
    y = np.random.choice(n_classes, n_samples, replace=True, p=prob)

    # Initialize weights and bias
    weights = init(1, n_features)[0]
    bias = init(1, 1)[0]

    # Generate random features
    X = np.random.uniform(size=(n_samples, n_features))

    # Add noise to features before any adjustments
    X += np.random.normal(scale=noise, size=(n_samples, n_features))

    # Calculate y_pred such that X * weights + bias = y
    y_pred = np.dot(X, weights) + bias

    # Adjust X to satisfy the equation
    X += (y - y_pred)[:, np.newaxis] * weights
    return X, y

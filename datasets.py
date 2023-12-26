import numpy as np

# Random Initialization
def random_init(size_in, size_out):
    return np.random.uniform(0.0, 1.0, size=(size_in, size_out))

def count_occurances(y):
    arr = np.unique(y, return_counts=True)
    for i in range(len(arr[0])):
        print("class ", arr[0][i], " has ", arr[1][i], " items")

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

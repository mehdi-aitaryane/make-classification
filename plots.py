import matplotlib.pyplot as plt

# This function creates a 2D scatter plot of the input data.
# Parameters:
# title: str, Title of the plot
# xlabel: str, Label for the x-axis
# ylabel: str, Label for the y-axis
# X: np.ndarray, Input array of features
# y: np.ndarray, Input array of target values
# Returns: None

def scatter2D(title, xlabel, ylabel, X, y):
    plt.scatter(X[:, 0], X[:, 1], c = y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# This function creates a 3D scatter plot of the input data.
# Parameters:
# title: str, Title of the plot
# xlabel: str, Label for the x-axis
# ylabel: str, Label for the y-axis
# zlabel: str, Label for the z-axis
# X: np.ndarray, Input array of features
# y: np.ndarray, Input array of target values
# Returns: None

def scatter3D(title, xlabel, ylabel, zlabel, X, y):
    # Creating plot
    ax = plt.axes(projection ="3d")
    ax.scatter3D(X[:, 0], X[:, 1], X[:, 2], c = y)
    plt.title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    # Rotate the plot (change the angles as needed)
    ax.view_init(elev=30 , azim=-75 )
    plt.show()
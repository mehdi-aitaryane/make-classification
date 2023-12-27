# Make-Classification

This repository contains two modules and a notebook that are used to generate and visualize classification datasets.

## Mathematics Behind the Algorithm

The algorithm is based on the concept of linear classification. The goal is to find a hyperplane in an n-dimensional space (n is the number of features) that distinctly classifies the data points.

To achieve this, the algorithm initializes weights and bias randomly. It then generates random features and adds noise to these features. The target values are generated based on the probability distribution of the classes.

The algorithm then calculates the predicted values (y_pred) using the equation of a hyperplane, which is y_pred = X * weights + bias. Here, X is the feature matrix, weights are the coefficients of the hyperplane, and bias is the y-intercept.

Finally, the algorithm adjusts the features X to satisfy the equation X * weights + bias = y, where y is the actual target values.

## Pseudocode of the Algorithm

```
Procedure make_classification:
  Input: n_samples, n_features, n_classes, noise, balanced, random_state, init

  // Set the random state
  Set seed of random number generator to random_state

  // Create balanced or unbalanced samples
  Generate a uniform random vector of size n_classes, named prob
  If balanced is True, set all elements of prob to 1/n_classes
  Else, normalize prob by its sum

  // Generate target values
  Generate n_samples random numbers from 0 to n_classes-1, with probabilities given by prob, named y

  // Initialize weights and bias
  Generate a random vector of size n_features, named weights
  Generate a random number, named bias

  // Generate random features
  Generate a random matrix of size n_samples by n_features, named X

  // Add noise to features
  Add Gaussian noise with standard deviation equal to noise to X

  // Calculate predicted values
  Calculate dot product of X and weights, add bias, named y_pred

  // Adjust features to satisfy the equation
  For each row in X, add (y - y_pred) times weights

  Output: X, y
End Procedure
```


## Modules

### 1. Datasets

This module is used to generate classification datasets. It contains the following functions:

- `random_init(size_in, size_out)`: Initializes random values.
- `count_occurances(y)`: Counts the occurrences of each class in the target array.
- `print_shape(X, y)`: Prints the shape of the feature and target arrays.
- `make_classification(n_samples=101, n_features=20, n_classes=2, noise=0.0, balanced=True, random_state=None, init = random_init)`: Generates a classification dataset.

### 2. Plots

This module is used to visualize the datasets. It contains the following functions:

- `scatter2D(title, xlabel, ylabel, X, y)`: Creates a 2D scatter plot.
- `scatter3D(title, xlabel, ylabel, zlabel, X, y)`: Creates a 3D scatter plot.

## Notebook

The `Example` notebook demonstrates how to use the modules to generate and visualize a classification dataset.

## Usage

To use this repository, first, import the necessary modules. Then, you can generate a dataset using the `make_classification` function from the `datasets` module. Finally, you can visualize the dataset using the `scatter2D` or `scatter3D` functions from the `plots` module.

## Contributing

Contributions are welcome. Please open an issue to discuss your ideas or submit a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.

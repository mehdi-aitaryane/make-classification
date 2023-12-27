# Make-Classification

This repository contains two modules and a notebook that are used to generate and visualize classification datasets.

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

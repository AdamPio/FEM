# FEM
 Finite element method for classes 2021

Code calculates changes in symmetrical grids composed of 4-node elements over time.
The purpose of each of file:
* Agregate.py - functions for transforming matrices from the local system to the global system,
* data.py - contains basic variables for grid creation and calculus,
* Element4.py - Basic structures for grid calculation,
* gauss.py - Integration by Gauss method. Needed for classes, but irrelevant in the program,
* Grid.py - Grid, nodes and elements creation
* Jakob.py - Calculating Jacob and inverted Jacob for single element,
* main.py - 
* MatrixC.py - Calculating MatrixC for provided arguments
* MatrixH.py - Calculating MatrixH for provided arguments
* MatrixHbc.py - Calculating MatrixHbc for provided arguments
* MatrixP.py - Calculating vector P for provided arguments
* SolveTemp - Method for calcuating thermal state of a grid after a given time
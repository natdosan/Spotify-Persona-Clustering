# src
This repo contains code contributions from Nathaniel del Rosario during the winter of 2022 and 2023.
## Overall Goal of this Project:
* Establish pipeline to process data from Spotify API
* Perform feature extraction, engineering, and selection on the data
* Run multiple supervised/unsupervised methods to create models 
* Optimize models to generate valuable insights on Spotify songs by clustering different consumer listening personas
* Revisit this project every quarter to improve its design 

## Dependencies:
* Make sure to install conda
* The Visual Studio Code Python extension installed

## To run this project:
1. `cd src` (if not already in the directory)
2. `conda env create --file environment.yml` to create a conda environment with the required dependencies. *If you already have the environment installed you can skip this step.*
3. Open Visual Studio Code in the current directory with `code .`
4. To point VSCode to the right conda environment, select a python/ipynb file within src/.
5. Wait a few seconds for VSCode's Python extension to get started up.
6. In the bottom right corner, there should be a button that says "Select Python Interpreter". Click it and it should bring up a menu in the top middle. Select the environment that says `Python 3.XX.X ('spotify')`.
7. You're ready! Opening the terminal in VSCode will automatically put you in the correct environment to run the Python files. 

Visual Studio Code will remember all these settings, so there is no need to open the terminal and repeating these steps. Just open the folder in VSCode next time you need to open this project.

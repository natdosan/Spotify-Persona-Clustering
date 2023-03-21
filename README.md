# Spotify-Top-200

This project is in its beginning stages. For an overview, click [here](https://purrfect-zinc-f80.notion.site/Spotify-57e38776f1fc4f30a1381f45c42b1d36)

Structure
```
Spotify Persona Clustering
├── code
│   ├── data
│   │    ├── README.md
│   │    ├── songs.csv
│   │    │ 
│   │    └── features.csv
│   │    
│   └── src
│        ├── README.md
│        ├── environment.yml
│        ├── preprocess
│        │        ├── scrape_spotify.py
│        │        └── preprocess.ipynb
│        │     
│        ├── supervised
│        │        └── knn.ipynb
│        └── unsupervised
│                 └── kmeans.ipynb
├── LICENSE
├── requirements.txt
└── README.md
```

# Usage

## Install
clone the repository
```
git clone https://github.com/natdosan/Spotify-Persona-Clustering
```
Go the repository directory, switch the branch if running branch other than master
```
cd Spotify-Persona-Clustering
git checkout <branch you'd like to run>
```
Create conda environment and activate it
```
cd front-end-vis
conda env create -f environment.MacOS.Linux.yml
conda activate vhfd
```

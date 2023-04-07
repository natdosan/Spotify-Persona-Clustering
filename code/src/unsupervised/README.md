# Curse of Dimensionality

## One shortcoming of high dimensional data (many features) is that clustering algorithms that use distance as a Loss Function in Empirical Risk Minimization become less and less effective as dimensions increase.

For dimensionality reduction in the context of unsupervised learning for Spotify audio features, the best technique would be either Principal Component Analysis (PCA) or t-SNE.

* PCA is a good choice when you want to preserve as much information as possible while reducing the dimensions of the dataset. It can also help you identify the most important audio features that contribute the most to the clustering.

* On the other hand, t-SNE is a non-linear technique that is particularly useful when you want to visualize the clusters in a low-dimensional space. It can preserve the global structure of the data while emphasizing the local structure, making it easier to identify clusters and subclusters.

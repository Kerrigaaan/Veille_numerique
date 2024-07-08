from sklearn.cluster import KMeans
import numpy as np

def cluster_informations(informations):
    descriptions = np.array([info['description_length'] for info in informations]).reshape(-1, 1)
    
    n_samples = len(descriptions)
    n_clusters = 3  # Nombre de clusters souhaité

    if n_samples < n_clusters:
        print(f"Nombre d'échantillons ({n_samples}) est inférieur au nombre de clusters ({n_clusters}). Skipping clustering.")
        clusters = [-1] * n_samples
    else:
        kmeans = KMeans(n_clusters=n_clusters)
        kmeans.fit(descriptions)
        clusters = kmeans.predict(descriptions)

    for info, cluster in zip(informations, clusters):
        info['cluster'] = cluster

    return informations



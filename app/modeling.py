from sklearn.cluster import KMeans

def cluster_informations(informations):
    descriptions = np.array([info['description_length'] for info in informations]).reshape(-1, 1)
    kmeans = KMeans(n_clusters=3)
    kmeans.fit(descriptions)
    clusters = kmeans.predict(descriptions)

    for info, cluster in zip(informations, clusters):
        info['cluster'] = cluster

    return informations

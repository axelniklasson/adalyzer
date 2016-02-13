from sklearn import cluster
import numpy as np

def find_optimal_locations(data, count = 5, no_clusters = 10):
	kmeans = cluster.KMeans(no_clusters, max_iter=300, n_init=10, init='kmeans++', precompute_distances='auto')
	clusters = kmeans.fit_predict(data)

	classes_count = np.zeros([no_clusters,2])
	for i in range(0, clusters.size):
		classes_count[clusters[i], 0] = clusters[i]
		classes_count[clusters[i], 1] += 1
	sorted = classes_count[classes_count[:,1].argsort()]

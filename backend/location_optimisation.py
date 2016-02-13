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

	cluster_locations = np.empty(count)
	c = 0
	for j in range(sorted[0].size, sorted[0].size - count, -1):
		cluster_locations[c] = kmeans.cluster_centers_[sorted[j,0]]
		c += 1

	return cluster_locations

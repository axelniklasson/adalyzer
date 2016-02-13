from sklearn import cluster

def find_optimal_locations(data, count = 5, clusters = 10):
	kmeans = cluster.KMeans(clusters, max_iter=300, n_init=10, init='kmeans++', precompute_distances='auto')
	clusters = kmeans.fit_predict(data)
	# TODO find max count clusters
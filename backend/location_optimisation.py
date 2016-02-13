from sklearn import cluster
import numpy as np
import datetime
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt


class Location:

	vehicle_data = None

	@staticmethod
	def get_data(self):
		if self.vehicle_data is not None:
			return self.vehicle_data.tolist()
		else:
			return None

	@staticmethod
	def __preprocess(payload):
		lat_lng = np.empty([len(payload), 2])
		for i in range(0, len(payload)):
			lat_lng[i, 0] = payload[i]['positioning_system']['location']['lat']
			lat_lng[i, 1] = payload[i]['positioning_system']['location']['lng']
		return lat_lng


	@staticmethod
	def set_optimal_locations(data, count=5, no_clusters=10):
		data = Location.__preprocess(data)
		kmeans = cluster.KMeans(no_clusters, max_iter=300, n_init=10, init='k-means++', precompute_distances='auto')
		clusters = kmeans.fit_predict(data)

		classes_count = np.zeros([no_clusters,2])
		for i in range(0, clusters.size):
			classes_count[clusters[i], 0] = clusters[i]
			classes_count[clusters[i], 1] += 1

		sorted = classes_count[classes_count[:,1].argsort()]

		cluster_locations = np.empty([count,2])
		c = 0
		for j in range(sorted[:,0].size-1, sorted[:,0].size - count - 1, -1):
			cluster_locations[c] = kmeans.cluster_centers_[sorted[j,0]]
			c += 1

			# Plot configurations
			#fig = plt.figure()
			#plt.plot(data[:,0], data[:,1], 'gx')
			#plt.plot(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], 'bo')
			#plt.legend(('Data', 'Centroids'), loc='upper left')
			#plt.show()
			#plt.savefig('plt-gen-' + datetime.datetime.now().isoformat() + '.png')
			#plt.close(fig)

		Location.vehicle_data = cluster_locations
from turtle import color
import numpy as np
from fcmeans import FCM
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.metrics import silhouette_score

df = pd.read_csv("UnifiedDataset.csv")
X = df.loc[:,['circuitId','total_time']].values

fcm = FCM(n_clusters=2)
fcm.fit(X)

# outputs
fcm_centers = fcm.centers
fcm_labels = fcm.predict(X)
print(fcm_labels)
score = silhouette_score(X, fcm_labels, metric='euclidean')
#
# Print the score
#
print('Silhouetter Score: %.3f' % score)
plt.scatter(X[:,0], X[:,1], c=X[:,0], cmap="rainbow")
#ax = plt.axes(projection='3d')  
#ax.scatter(X[:,0], X[:,1], X[:,2], c=fcm_labels, linewidth=0.5)
plt.xlabel("Circuit")  # X-axis label
plt.ylabel("Total Time")  # Y-axis label
plt.title("Fuzzy-c-means Clustering")
plt.show()  # showing the plot


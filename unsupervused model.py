import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#data
data = {
    'Name' : ['Aarav', 'priya', 'Rohan', 'Ananya',
              'Vikram', 'Meera', 'rahul', 'Neha'],
    'Income' : [350000, 500000, 420000, 1200000,
                300000, 950000, 400000, 1100000]
}

df = pd.DataFrame(data)

# k-means clustring
model = KMeans(n_clusters=2, random_state=0, n_init=10)
df['cluster'] =model.fit_predict(df[['Income']])

#display cluster
print("cluster 0:")
print(df[df['cluster'] == 0][['Name', 'Income']])

print("\ncluster 1:")
print(df[df['cluster'] == 1][['Name', 'Income']])

#visualization
plt.scatter(df['Name'], df['Income'], c=df['cluster'], cmap='viridis')

plt.xlabel('Name')
plt.ylabel('Income')
plt.title('Income cluster')
plt.show()

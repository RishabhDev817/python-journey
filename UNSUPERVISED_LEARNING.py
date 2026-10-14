# UNSUPERVISED LEARNING PRACTICAL
# K-Means Clustering

# Step 1: Import required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


# =========================================================
# STEP 1: CREATE DATASET
# =========================================================

# Customer data
# Annual Income (in thousands) and Spending Score

data = {
    'Income': [15, 16, 17, 18, 20,
               40, 42, 43, 45, 47,
               70, 72, 75, 78, 80],

    'Spending': [20, 22, 19, 25, 24,
                 50, 52, 48, 55, 53,
                 80, 85, 82, 88, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# =========================================================
# STEP 2: CHECK FOR MISSING VALUES
# =========================================================

print("\nMissing Values:")
print(df.isnull().sum())


# =========================================================
# STEP 3: SELECT FEATURES
# =========================================================

X = df[['Income', 'Spending']]


# =========================================================
# STEP 4: CHOOSE NUMBER OF CLUSTERS
# =========================================================

# We want to divide customers into 3 groups

k = 3

print("\nNumber of Clusters (K):", k)


# =========================================================
# STEP 5: CREATE K-MEANS MODEL
# =========================================================

kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)


# =========================================================
# STEP 6: TRAIN THE MODEL
# =========================================================

kmeans.fit(X)

print("\nK-Means model trained successfully.")


# =========================================================
# STEP 7: ASSIGN CLUSTERS
# =========================================================

df['Cluster'] = kmeans.labels_

print("\nClustered Data:")
print(df)


# =========================================================
# STEP 8: DISPLAY CENTROIDS
# =========================================================

print("\nCluster Centroids:")
print(kmeans.cluster_centers_)


# =========================================================
# STEP 9: PREDICT CLUSTER FOR NEW CUSTOMER
# =========================================================

# New customer:
# Income = 44 thousand
# Spending Score = 51

new_customer = pd.DataFrame({
    'Income': [44],
    'Spending': [51]
})

predicted_cluster = kmeans.predict(new_customer)

print("\nNew Customer:")
print(new_customer)

print(
    "Predicted Cluster:",
    predicted_cluster[0]
)


# =========================================================
# STEP 10: VISUALIZATION
# =========================================================

plt.scatter(
    X['Income'],
    X['Spending'],
    c=df['Cluster']
)

# Plot cluster centroids
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200,
    label='Centroids'
)

plt.xlabel("Annual Income (Thousands)")
plt.ylabel("Spending Score")
plt.title("K-Means Customer Clustering")

plt.legend()
plt.show()

from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
import random

spark = SparkSession.builder.appName("ClusteringExperiment").getOrCreate()

data_points = []
for _ in range(100):
    data_points.append((10 + random.uniform(-2, 2), 10 + random.uniform(-2, 2)))
for _ in range(100):
    data_points.append((50 + random.uniform(-2, 2), 50 + random.uniform(-2, 2)))

df = spark.createDataFrame(data_points, ["feature1", "feature2"])
print("Generated Data:")
df.show(5)

assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
transformed_df = assembler.transform(df)

print("Transformed Data with 'features' column:")
transformed_df.show(5)

kmeans = KMeans(k=2, seed=1)
model = kmeans.fit(transformed_df)
predictions = model.transform(transformed_df)

print("Predictions with 'prediction' (cluster) column:")
predictions.show(5)

cost = model.summary.trainingCost
print(f"Within Set Sum of Squared Errors (WSSSE): {cost}")

centers = model.clusterCenters()
print("Cluster Centers:")
for center in centers:
    print(center)

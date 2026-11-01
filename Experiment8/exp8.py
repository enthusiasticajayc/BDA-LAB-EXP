
import os
import sys
import random

# Configure Python for PySpark
python_path = sys.executable
os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("ClusteringExperiment")
    .master("local[1]")
    .config("spark.pyspark.python", python_path)
    .config("spark.pyspark.driver.python", python_path)
    .config("spark.sql.shuffle.partitions", "4")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

# Generate random data points
data_points = []

# First cluster around (10, 10)
for _ in range(100):
    data_points.append((
        10 + random.uniform(-2, 2),
        10 + random.uniform(-2, 2)
    ))

# Second cluster around (50, 50)
for _ in range(100):
    data_points.append((
        50 + random.uniform(-2, 2),
        50 + random.uniform(-2, 2)
    ))

# Create DataFrame
df = spark.createDataFrame(
    data_points,
    ["feature1", "feature2"]
)

print("Generated Data:")
df.show(5)

# Convert columns into feature vector
assembler = VectorAssembler(
    inputCols=["feature1", "feature2"],
    outputCol="features"
)

transformed_df = assembler.transform(df)

print("Transformed Data with 'features' column:")
transformed_df.show(5)

# Apply K-Means clustering
kmeans = KMeans(
    k=2,
    seed=1,
    initMode="random",
    maxIter=20
)

model = kmeans.fit(transformed_df)

# Predict clusters
predictions = model.transform(transformed_df)

print("Predictions with 'prediction' (cluster) column:")
predictions.show(5)

# Calculate WSSSE
cost = model.summary.trainingCost

print("Within Set Sum of Squared Errors (WSSSE):", cost)

# Display cluster centers
centers = model.clusterCenters()

print("Cluster Centers:")
for center in centers:
    print(center)

# Stop Spark
spark.stop()

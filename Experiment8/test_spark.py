import os
import sys

python_path = sys.executable

os.environ["PYSPARK_PYTHON"] = python_path
os.environ["PYSPARK_DRIVER_PYTHON"] = python_path

from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .master("local[1]")
    .appName("PythonWorkerTest")
    .config("spark.pyspark.python", python_path)
    .config("spark.pyspark.driver.python", python_path)
    .getOrCreate()
)

print("Python:", python_path)

result = spark.sparkContext.parallelize([1, 2, 3], 1).map(
    lambda x: x + 1
).collect()

print("Worker result:", result)

spark.stop()
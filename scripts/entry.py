from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
import os

delta_path = "file://" + os.path.abspath("delta_minimal")

# Spark session with Delta
builder = (
    SparkSession.builder.appName("DeltaMinimalistic")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
)
spark = configure_spark_with_delta_pip(builder).getOrCreate()

# Write version 0
df_v0 = spark.createDataFrame([(1, "alpha"), (2, "beta")], ["id", "value"])
df_v0.write.format("delta").mode("overwrite").save(delta_path)

# Overwrite with version 1 (same schema)
df_v1 = spark.createDataFrame([(3, "gamma"), (4, "delta")], ["id", "value"])
df_v1.write.format("delta").mode("overwrite").option("overwriteSchema", "true").save(
    delta_path
)

# Read latest version
print("\n Latest Version:")
spark.read.format("delta").load(delta_path).show()

# Read previous version
print("\n Time Travel to Version 0:")
spark.read.format("delta").option("versionAsOf", 0).load(delta_path).show()

# Show history
print("\n Delta Table History:")
spark.sql(f"DESCRIBE HISTORY delta.`{delta_path}`").show(truncate=False)

spark.stop()

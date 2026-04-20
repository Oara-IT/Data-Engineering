import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
from pyspark.sql.functions import col
from pyspark.sql.types import DoubleType

credentials_location = "/home/oara-it/Data-Engineering/stunning-ruler-493803-j1-8a2b20987da5.json"

conf = SparkConf() \
    .setMaster('local[*]') \
    .setAppName('data_cleaning') \
    .set("spark.driver.memory", "2g") \
    .set("spark.jars", "/home/oara-it/Data-Engineering/Batch/Spark/.venv/lib/python3.12/site-packages/pyspark/jars/gcs-connector-hadoop3-latest.jar") \
    .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
    .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", credentials_location)

sc = SparkContext(conf=conf)

hadoop_conf = sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.AbstractFileSystem.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")

spark = SparkSession.builder.config(conf=sc.getConf()).getOrCreate()

files = {
    "zaf": "gs://bronze-stunning-ruler-493803-j1/raw/zaf_data.csv",
    "phl": "gs://bronze-stunning-ruler-493803-j1/raw/phl_data.csv",
    "nga": "gs://bronze-stunning-ruler-493803-j1/raw/nga_data.csv",
    "bra": "gs://bronze-stunning-ruler-493803-j1/raw/bra_data.csv"
}

for name, path in files.items():
    print(f"Processing {name}...")
    
    df = spark.read.csv(path, header=True, inferSchema=True)
    
    df_clean = df.dropDuplicates().dropna()
    
    df_clean.repartition(4) \
        .write \
        .mode("overwrite") \
        .parquet(f"gs://silver-stunning-ruler-493803-j1/cleaned/{name}/")
    
    print(f"{name} done!")

print("All done!")
# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using access keys
# MAGIC 1. Set the spark config fs.azure.account.key
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

# MAGIC %md
# MAGIC # Access key

# COMMAND ----------

spark.conf.set(
    "fs.azure.account.key.formula1dlpro2.dfs.core.windows.net",
    "61ndkNz/tm0BhRekIAwUiXm3/XTkbKW3ixXVYMxl2dY0LSwyxhkm08g6fp80qlcoD+vkNvGU/KoG+ASt4SfR1w==")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlpro2.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlpro2.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


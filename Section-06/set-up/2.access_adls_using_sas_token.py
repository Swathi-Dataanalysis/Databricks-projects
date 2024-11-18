# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Data Lake using SAS Token
# MAGIC 1. Set the spark config for SAS Token
# MAGIC 1. List files from demo container
# MAGIC 1. Read data from circuits.csv file

# COMMAND ----------

# MAGIC %md
# MAGIC # SAS token
# MAGIC sp=rl&st=2024-11-17T17:59:06Z&se=2024-11-19T01:59:06Z&spr=https&sv=2022-11-02&sr=c&sig=uKE7d0dLedB21%2FQlFUGRD5oJ0WttrkcAAaeGPFSPszY%3D

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.formula1dlpro2.dfs.core.windows.net", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type.formula1dlpro2.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.sas.FixedSASTokenProvider")
spark.conf.set("fs.azure.sas.fixed.token.formula1dlpro2.dfs.core.windows.net", "sp=rl&st=2024-11-17T17:59:06Z&se=2024-11-19T01:59:06Z&spr=https&sv=2022-11-02&sr=c&sig=uKE7d0dLedB21%2FQlFUGRD5oJ0WttrkcAAaeGPFSPszY%3D")

# COMMAND ----------

display(dbutils.fs.ls("abfss://demo@formula1dlpro2.dfs.core.windows.net"))

# COMMAND ----------

display(spark.read.csv("abfss://demo@formula1dlpro2.dfs.core.windows.net/circuits.csv"))

# COMMAND ----------


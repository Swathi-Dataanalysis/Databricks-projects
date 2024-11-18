# Databricks notebook source
# MAGIC %md
# MAGIC #### Explore the capabilities of the dbutils.secrets utility

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list(scope = 'formula1pro2-scope')

# COMMAND ----------

dbutils.secrets.get(scope = 'formula1pro2-scope', key = 'formula1dlpro2-account-key')

# COMMAND ----------


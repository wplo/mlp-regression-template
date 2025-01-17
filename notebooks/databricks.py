# Databricks notebook source

# MAGIC %md
# MAGIC # MLflow Regression Pipeline Databricks Notebook
# MAGIC This notebook runs the MLflow Regression Pipeline on Databricks and inspects its results.
# MAGIC
# MAGIC For more information about the MLflow Regression Pipeline, including usage examples,
# MAGIC see the [Regression Pipeline overview documentation](https://mlflow.org/docs/latest/pipelines.html#regression-pipeline)
# MAGIC and the [Regression Pipeline API documentation](https://mlflow.org/docs/latest/python_api/mlflow.pipelines.html#module-mlflow.pipelines.regression.v1.pipeline).

# COMMAND ----------

# MAGIC %pip install mlflow[pipelines]
# MAGIC %pip install -r ../requirements.txt

# COMMAND ----------

from mlflow.pipelines import Pipeline

p = Pipeline(profile="databricks")

# COMMAND ----------

p.inspect()

# COMMAND ----------

p.run("ingest")

# COMMAND ----------

p.run("split")

# COMMAND ----------

training_data = p.get_artifact("training_data")
training_data.describe()

# COMMAND ----------

p.run("transform")

# COMMAND ----------

p.run("train")

# COMMAND ----------

trained_model = p.get_artifact("model")
print(trained_model)

# COMMAND ----------

p.run("evaluate")

# COMMAND ----------

p.run("register")

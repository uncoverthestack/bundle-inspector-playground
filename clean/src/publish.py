# Databricks notebook source
rows = dbutils.jobs.taskValues.get(taskKey="ingest", key="row_count")
print(rows)

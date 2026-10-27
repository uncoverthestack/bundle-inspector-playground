# Databricks notebook source
rows = dbutils.jobs.taskValues.get(taskKey="ingest", key="rowcount")
print(rows)

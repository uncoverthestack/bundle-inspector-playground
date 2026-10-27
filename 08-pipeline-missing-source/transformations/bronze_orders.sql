CREATE OR REFRESH STREAMING TABLE bronze_orders AS SELECT * FROM STREAM read_files("/Volumes/main/playground/raw");

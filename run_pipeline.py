import json
from pyspark.sql import SparkSession
from transformer.core import apply_transformations, execute_actions
from transformer.config_loader import load_config, validate_config

if __name__ == "__main__":

    config = load_config("config/sample_config.json")
    validate_config(config)


    spark = SparkSession.builder.appName("DynamicTransformer").getOrCreate()

    # Load sample data
    df = spark.read.option("header", True).csv("data/input_data.csv")

    # Load config
    with open("config/sample_config.json") as f:
        config = json.load(f)

    # Run pipeline
    transformed_df = apply_transformations(df, config["transformations"])
    results = execute_actions(transformed_df, config["actions"])

    spark.stop()
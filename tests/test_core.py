import pytest
from pyspark.sql import SparkSession
from transformer.core import apply_transformations

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local[1]").appName("Test").getOrCreate()

def test_select_columns(spark):
    df = spark.createDataFrame([(1, "Alice", 29)], ["id", "name", "age"])
    config = [{"operation": "select", "args": ["id", "name"]}]
    result_df = apply_transformations(df, config)
    assert result_df.columns == ["id", "name"]
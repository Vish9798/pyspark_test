def transform_df(df, custom_fn, args):
    return custom_fn(df, **args)

# Example custom function
def add_timestamp_column(df, column_name="timestamp"):
    from pyspark.sql.functions import current_timestamp
    return df.withColumn(column_name, current_timestamp())
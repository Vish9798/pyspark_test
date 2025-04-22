TRANSFORMATIONS = {
    "select": lambda df, args: df.select(*args),
    "filter": lambda df, args: df.filter(args),
    "withColumn": lambda df, args: df.withColumn(args["name"], args["expr"]),
    "drop": lambda df, args: df.drop(*args),
    "alias": lambda df, args: df.alias(args),
    "join": lambda df, args: df.join(args["other"], on=args["on"], how=args.get("how", "inner")),
    "groupBy": lambda df, args: df.groupBy(*args["cols"]).agg(args["agg_exprs"]),
    # Add more as needed
}
ACTIONS = {
    "show": lambda df, args: df.show(args.get("n", 20), truncate=args.get("truncate", True)),
    "collect": lambda df, args: df.collect(),
    "count": lambda df, args: df.count(),
    "write_parquet": lambda df, args: df.write.mode(args.get("mode", "overwrite")).parquet(args["path"]),
}
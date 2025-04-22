# Dynamic DataFrame Transformation Framework (PySpark)

A modular, dictionary-driven PySpark framework that allows users to define, chain, and execute complex DataFrame transformations and actions using configuration files (JSON or YAML).

---

## Features

-  **Dynamic Execution**: Drive all transformations and actions via config files.
-  **Modular Design**: Easily add new transformation or action types.
-  **Custom Logic**: Support for user-defined transformation functions.
-  **Declarative Configuration**: Separate ETL logic from code using JSON/YAML.
-  **Supports PySpark Actions**: e.g., `show`, `collect`, `write_parquet`, etc.
-  **Unit-Testable**: Includes test suite with `pytest`.
-  **Logging Support**: Built-in logger for debugging pipelines.

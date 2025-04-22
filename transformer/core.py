from .transformations import TRANSFORMATIONS
from .actions import ACTIONS
from .logger import get_logger

logger = get_logger()

def apply_transformations(df, transformation_config):
    for step in transformation_config:
        op = step["operation"]
        args = step.get("args", {})
        logger.info(f"Applying transformation: {op} with args: {args}")
        if op in TRANSFORMATIONS:
            try:
                df = TRANSFORMATIONS[op](df, args)
            except Exception as e:
                logger.error(f"Error applying transformation '{op}': {e}")
                raise
        else:
            raise KeyError(f"Unknown transformation '{op}'")
    return df

def execute_actions(df, action_config):
    results = []
    for step in action_config:
        act = step["action"]
        args = step.get("args", {})
        logger.info(f"Executing action: {act} with args: {args}")
        if act in ACTIONS:
            try:
                result = ACTIONS[act](df, args)
                results.append(result)
            except Exception as e:
                logger.error(f"Error executing action '{act}': {e}")
                raise
        else:
            raise KeyError(f"Unknown action '{act}'")
    return results
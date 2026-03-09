import os
from typing import Union

from dotenv import load_dotenv

load_dotenv()


# Retrieves env value
def env(name: str, default: Union[str, None] = None) -> str:
    val = os.getenv(name, default)
    if val is None or val == "":
        raise RuntimeError(f"Environment variable {name} not set")
    return val

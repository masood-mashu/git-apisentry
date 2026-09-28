"""
schema_syntax_validator.py - Validates basic structural compliance of OpenAPI path and operation definitions
"""
import sys
import json


def validate_schema_syntax(endpoint_path: str):
    valid_format = endpoint_path.startswith("/") and not endpoint_path.endswith("/")
    has_params = "{" in endpoint_path and "}" in endpoint_path
    return {
        "path": endpoint_path,
        "valid_format": valid_format,
        "parameterized": has_params,
        "status": "VALID_PATH" if valid_format else "INVALID_PATH_FORMAT"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "schema-syntax-validator"}))

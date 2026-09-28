"""
breaking_change_detector.py - Detects removed endpoints and newly required request parameters in OpenAPI schemas
"""
import sys
import json


def detect_breaking_changes(diff_summary_json: str):
    import json
    data = json.loads(diff_summary_json) if isinstance(diff_summary_json, str) else diff_summary_json
    removed = data.get("removed_endpoints", [])
    new_req = data.get("new_required_params", [])
    is_breaking = len(removed) > 0 or len(new_req) > 0
    return {
        "removed_count": len(removed),
        "new_required_count": len(new_req),
        "breaking": is_breaking,
        "recommended_bump": "MAJOR" if is_breaking else "MINOR_OR_PATCH",
        "status": "BREAKING_CHANGES_DETECTED" if is_breaking else "BACKWARD_COMPATIBLE"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "breaking-change-detector"}))

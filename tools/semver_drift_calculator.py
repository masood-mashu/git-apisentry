"""
semver_drift_calculator.py - Verifies that the proposed version increment matches the contract change classification
"""
import sys
import json


def calculate_semver(version_pair_json: str):
    import json
    data = json.loads(version_pair_json) if isinstance(version_pair_json, str) else version_pair_json
    curr = [int(x) for x in data.get("current_version", "1.0.0").split(".")]
    prop = [int(x) for x in data.get("proposed_version", "1.1.0").split(".")]
    c_type = data.get("change_type", "ADDITIVE")
    
    if c_type == "BREAKING":
        valid = prop[0] > curr[0]
    else:
        valid = prop[1] > curr[1] or (prop[0] == curr[0] and prop[2] > curr[2])
    return {
        "current": ".".join(map(str, curr)),
        "proposed": ".".join(map(str, prop)),
        "change_type": c_type,
        "compliant": valid,
        "status": "SEMVER_ALIGNED" if valid else "SEMVER_MISMATCH"
    }


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "semver-drift-calculator"}))

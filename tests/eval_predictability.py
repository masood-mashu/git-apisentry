"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitAPISentry.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.breaking_change_detector import *
from tools.semver_drift_calculator import *
from tools.schema_syntax_validator import *

class TestGitAPISentryPredictability(unittest.TestCase):

    def test_breaking_change_detector(self):
        res = detect_breaking_changes('{"removed_endpoints": ["/v1/orders"], "new_required_params": []}')
        self.assertTrue(res["breaking"])
        self.assertEqual(res["recommended_bump"], "MAJOR")

    def test_semver_drift_calculator(self):
        res = calculate_semver('{"current_version": "1.0.0", "proposed_version": "2.0.0", "change_type": "BREAKING"}')
        self.assertTrue(res["compliant"])
        self.assertEqual(res["status"], "SEMVER_ALIGNED")

    def test_schema_syntax_validator(self):
        res = validate_schema_syntax("/api/v1/customers")
        self.assertTrue(res["valid_format"])
        self.assertEqual(res["status"], "VALID_PATH")


if __name__ == "__main__":
    unittest.main()

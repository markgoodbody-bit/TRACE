import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


MODULE_PATH = Path(__file__).with_name("run_trace_v030_two_family_api_study.py")
SPEC = importlib.util.spec_from_file_location("trace_runner", MODULE_PATH)
runner = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(runner)


class TraceRunnerTests(unittest.TestCase):
    def test_route_allowlist_excludes_qwen_retry_manual_and_external_shapes(self):
        self.assertTrue(runner.admitted_route("/api/connections/gemini/test", "POST"))
        self.assertTrue(runner.admitted_route("/api/connections/kimi/test", "POST"))
        self.assertTrue(runner.admitted_route("/api/diagnostics/preflight", "GET"))
        self.assertTrue(
            runner.admitted_route(
                "/api/sessions/session_1/rounds/round_1/call/gemini", "POST"
            )
        )
        self.assertFalse(runner.admitted_route("/api/connections/qwen/test", "POST"))
        self.assertFalse(
            runner.admitted_route(
                "/api/sessions/session_1/rounds/round_1/call/qwen", "POST"
            )
        )
        self.assertFalse(
            runner.admitted_route(
                "/api/sessions/session_1/rounds/round_1/retry-authorize/gemini",
                "POST",
            )
        )
        self.assertFalse(
            runner.admitted_route(
                "/api/sessions/session_1/rounds/round_1/manual/gemini", "POST"
            )
        )

    def test_exact_estimate_contract_accepts_only_bound_input_and_empty_envelope(self):
        prompt_hash = "a" * 64
        job = {
            "jobId": "job-1",
            "providerId": "gemini",
            "presetId": "gemini-3.6-flash",
            "promptSha256": prompt_hash,
            "visibleAnswerTokens": 8000,
            "maxOutputTokens": 8000,
        }
        response = {
            "estimates": [
                {
                    "modelId": "gemini",
                    "presetId": "gemini-3.6-flash",
                    "transport": "api",
                    "fallbackReason": "",
                    "effectiveInputSha256": prompt_hash,
                    "contextSha256": runner.EMPTY_SHA256,
                    "roleInstructionSha256": runner.EMPTY_SHA256,
                    "visibleAnswerTokens": 8000,
                    "transportMaxOutputTokens": 8000,
                    "billingOutputCeilingTokens": 8000,
                    "dispatchBasis": {"identityRequired": False},
                    "estimate": {
                        "currency": "USD",
                        "maximumEstimatedCost": 0.1,
                    },
                }
            ],
            "budgetPreflight": {"plannedCallCount": 1},
            "budgetConfirmation": {"fingerprint": "b" * 64},
        }
        self.assertEqual(runner.validate_estimate(job, response), (0.1, "b" * 64))
        response["estimates"][0]["identityRequired"] = True
        response["estimates"][0]["dispatchBasis"]["identityRequired"] = True
        with self.assertRaises(ValueError):
            runner.validate_estimate(job, response)

    def test_connection_ceilings_use_effective_server_preflight_not_catalogue_presets(self):
        diagnostic_preflight = {
            "items": [
                {
                    "modelId": "gemini",
                    "configuredModel": "gemini-3.6-flash",
                    "visibleAnswerTokens": 128,
                    "transportMaxOutputTokens": 384,
                    "billingOutputCeilingTokens": 384,
                    "maximumEstimatedCost": {
                        "priceKnown": True,
                        "currency": "USD",
                        "maximumEstimatedCost": 0.003471,
                    },
                },
                {
                    "modelId": "kimi",
                    "configuredModel": "kimi-k3",
                    "visibleAnswerTokens": 128,
                    "transportMaxOutputTokens": 768,
                    "billingOutputCeilingTokens": 768,
                    "maximumEstimatedCost": {
                        "priceKnown": True,
                        "currency": "USD",
                        "maximumEstimatedCost": 0.01155,
                    },
                },
            ]
        }
        self.assertEqual(runner.connection_ceiling(diagnostic_preflight, "gemini"), 0.003471)
        self.assertEqual(runner.connection_ceiling(diagnostic_preflight, "kimi"), 0.01155)
        self.assertLess(
            runner.connection_ceiling(diagnostic_preflight, "gemini")
            + runner.connection_ceiling(diagnostic_preflight, "kimi"),
            0.016,
        )

    def test_actual_usage_replaces_estimate_only_when_currency_is_exact_usd(self):
        self.assertEqual(
            runner.accounted_exposure(
                {"actualCost": {"amount": 0.02, "currency": "USD"}}, 0.1
            ),
            0.02,
        )
        self.assertEqual(
            runner.accounted_exposure(
                {"actualCost": {"amount": 0.02, "currency": "EUR"}}, 0.1
            ),
            0.1,
        )
        self.assertEqual(
            runner.accounted_exposure(
                {"unconfirmedCostCeiling": {"amount": 0.08, "currency": "USD"}},
                0.1,
            ),
            0.08,
        )

    def test_stopped_summary_distinguishes_attempted_from_planned_probe_reserve(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "summary.json"
            runner.write_summary(
                path,
                status="STOPPED_CONNECTION_FAILURE",
                cap=4.0,
                connection_reserve=0.000975,
                planned_connection_reserve=0.012525,
                completed_exposure=0.0,
                jobs=[{"jobId": "one"}] * 32,
                events=[],
                failure={"code": "DIAGNOSTIC_MARKER_MISMATCH"},
            )
            summary = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(summary["connectionReserveUsd"], 0.000975)
            self.assertEqual(summary["plannedConnectionReserveUsd"], 0.012525)
            self.assertEqual(summary["completedOrReservedExposureUsd"], 0.000975)
            self.assertEqual(summary["remainingAuthorizedUsd"], 3.999025)


if __name__ == "__main__":
    unittest.main()

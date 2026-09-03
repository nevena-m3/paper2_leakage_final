"""Unit tests for the standard-library frozen-output verifier."""

from __future__ import annotations

import importlib.util
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "tools" / "verify_frozen_outputs.py"
SPEC = importlib.util.spec_from_file_location("verify_frozen_outputs", SCRIPT)
assert SPEC and SPEC.loader
verifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(verifier)


def test_sha256_bytes_known_vector() -> None:
    assert verifier.sha256_bytes(b"paper2") == (
        "b104319103eb86d87c32c8651b8296065af9ce3c372c797f31fea85861f1bcdc"
    )


def test_zip_path_from_relative_windows_path() -> None:
    assert verifier.zip_path_from_manifest(r"outputs\goal1\DONE.json") == (
        "outputs/goal1/DONE.json"
    )


def test_zip_path_from_absolute_windows_path() -> None:
    source = r"C:\analysis\paper2\outputs\goal3\final\DONE.json"
    assert verifier.zip_path_from_manifest(source) == "outputs/goal3/final/DONE.json"


def test_truthy_values() -> None:
    for value in ("1", "true", "T", "yes", "Y", "pass"):
        assert verifier.truthy(value)
    for value in ("0", "false", "no", "fail", ""):
        assert not verifier.truthy(value)

"""Fast structural checks that do not require governed research data."""

from __future__ import annotations

import json
from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_notebooks_are_valid_json() -> None:
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    assert notebooks, "No notebooks were found"

    for notebook in notebooks:
        payload = json.loads(notebook.read_text(encoding="utf-8"))
        assert payload.get("nbformat") == 4, notebook
        assert isinstance(payload.get("cells"), list), notebook


def test_notebook_names_follow_publication_convention() -> None:
    notebooks = sorted((ROOT / "notebooks").glob("*.ipynb"))
    pattern = re.compile(r"^\d{2}[a-z]?_[a-z0-9]+(?:_[a-z0-9]+)*\.ipynb$")

    invalid = [notebook.name for notebook in notebooks if not pattern.fullmatch(notebook.name)]
    assert not invalid, f"Nonconforming notebook names: {invalid}"
    assert len(notebooks) == 25


def test_yaml_files_parse() -> None:
    yaml_files = sorted(ROOT.glob("*.yml")) + sorted((ROOT / "configs").glob("*.yaml"))
    assert yaml_files, "No YAML configuration files were found"

    for yaml_file in yaml_files:
        assert yaml.safe_load(yaml_file.read_text(encoding="utf-8")) is not None


def test_documented_freeze_commit_is_stable() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "55cba2083327aa71be5ea7771a3185daefa0c979" in readme
    assert "paper2-analysis-freeze-v1.0.0" in readme

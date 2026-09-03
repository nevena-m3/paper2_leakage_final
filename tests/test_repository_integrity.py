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
    assert not [notebook.name for notebook in notebooks if "historical" in notebook.name]


def test_development_and_final_bootstrap_labels_match_saved_runs() -> None:
    expected = {
        "10_goal1_primary_analysis_development_v1_1_300_bootstraps.ipynb": 300,
        "10_goal1_primary_analysis_final_v1_1_2000_bootstraps.ipynb": 2000,
        "20_goal2_primary_inference_development_v1_1_300_bootstraps.ipynb": 300,
        "20_goal2_primary_inference_final_v1_1_2000_bootstraps.ipynb": 2000,
    }

    for filename, replicates in expected.items():
        notebook = ROOT / "notebooks" / filename
        payload = notebook.read_text(encoding="utf-8")
        assert f"Bootstrap replicates: {replicates}\\n" in payload, filename


def test_yaml_files_parse() -> None:
    yaml_files = sorted(ROOT.glob("*.yml")) + sorted((ROOT / "configs").glob("*.yaml"))
    assert yaml_files, "No YAML configuration files were found"

    for yaml_file in yaml_files:
        assert yaml.safe_load(yaml_file.read_text(encoding="utf-8")) is not None


def test_documented_freeze_commit_is_stable() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "55cba2083327aa71be5ea7771a3185daefa0c979" in readme
    assert "paper2-analysis-freeze-v1.0.0" in readme

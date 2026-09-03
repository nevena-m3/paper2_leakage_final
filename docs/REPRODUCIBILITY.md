# Reproducibility guide

This repository is a code-and-provenance release for a frozen analysis. It does
not distribute the governed recordings, participant-level clinical data, or
generated outputs required for a full rerun.

## Reproducibility levels

1. **Public structural validation** verifies Python syntax, notebook structure,
   YAML parsing, and the frozen-output verifier's utility functions. It requires
   no restricted data.
2. **Frozen-output validation** checks the archived analysis products against
   recorded hashes and scientific invariants. It requires the governed
   `outputs.zip` archive but not the raw participant data.
3. **Clean-room reconstruction** reruns the notebooks from governed source data
   and the pinned external Paper-1 implementation. It is available only to
   authorized users with those inputs.

## Public structural validation

Create the supported environment and run the fast checks:

```bash
conda env create -f environment.yml
conda activate paper2-leakage
python -m pytest
python -m compileall -q src tools notebooks
```

The same checks run in GitHub Actions on Python 3.11 and 3.12.

## Frozen-output validation

With the governed archive available locally:

```bash
python tools/verify_frozen_outputs.py /path/to/outputs.zip
```

The verifier checks the exact outer archive size and SHA-256, internal ZIP
integrity, Goal 1–3 completion/freeze records, recorded artifact hashes, Goal-3
Stage-E invariants, and final figure hashes. If an otherwise identical archive
was repacked, use `--allow-different-archive-container` to validate its internal
manifests while explicitly relaxing only the outer-container identity check.

## Authoritative execution order

Do not infer execution order or authority from notebook filenames alone. Follow
the lineage and supersession decisions in [ANALYSIS_LINEAGE.md](ANALYSIS_LINEAGE.md)
and the notebook map in [../notebooks/README.md](../notebooks/README.md).
Legacy notebook names found in frozen records are translated in
[NOTEBOOK_NAMING.md](NOTEBOOK_NAMING.md).

## Environment boundary

- `environment.yml` is the general reconstruction environment.
- `environment-goal3-supported.yml` is the supported Goal-3 reconstruction
  environment for the pinned Paper-1 implementation.
- `requirements-goal3-stageE-historical-critical.txt` records critical package
  versions observed in the historical run; it is not a complete lockfile.
- Historical runtime facts and the Python-version divergence are documented in
  [RUNTIME_PROVENANCE.md](RUNTIME_PROVENANCE.md).

## What a passing check means

A passing public CI run establishes repository structural integrity only. A
passing frozen-output audit additionally establishes consistency with the
recorded frozen artifacts. Neither substitutes for access-controlled
regeneration from raw data, independent statistical review, or journal review.

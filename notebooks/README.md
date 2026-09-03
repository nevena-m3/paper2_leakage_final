# Notebook execution guide

This directory retains final notebooks plus explicitly labeled development,
superseded, and checkpoint-execution variants for auditability. Run only the
authoritative path below unless you are explicitly reconstructing provenance.

## Naming convention

Notebook filenames use lowercase ASCII `snake_case`:

```text
<number>_<goal-or-phase>_[stage]_<purpose>_[authority]_[version].ipynb
```

- `number` preserves the established scientific execution identifier.
- `stage` is included for the staged Goal-3 workflow.
- `development` identifies reduced-bootstrap exploratory executions.
- `final` identifies notebooks in the manuscript-authoritative execution path.
- `superseded` identifies a full-scale run replaced for a reason other than its
  bootstrap count.
- versions use `v1_0`, `v1_0_1`, and similar filename-safe notation.
- `qa` means the joint recording-quality/acoustic representation `Q+A`.
- `qchan` means the channel-related recording-quality component.

The cleanup changed filenames and the internal filename literals required to
keep notebook-to-notebook provenance lookups working. It did not change any
analysis, parameter, model, estimand, result, or stored output. The complete
old-to-new map is in
[`../docs/NOTEBOOK_NAMING.md`](../docs/NOTEBOOK_NAMING.md).

## Authoritative execution order

### Phase 0 — governed data freeze

1. `00_phase0_data_audit_and_freeze_final.ipynb` — audit source data; construct the
   canonical participant and recording ledgers, severity matches, and grouped
   split manifest.
2. `01_phase0_qchan_reference_cache_final.ipynb` — construct the fold-safe QCHAN
   reference cache.

### Goal 1 — information availability in Q

1. `10_goal1_primary_analysis_final_v1_1_2000_bootstraps.ipynb` — final primary
   diagnosis and severity analysis with 2,000 participant bootstraps.
2. `goal1_diagnosis_permutation_corrected_v1_1.py` — corrected participant-level
   diagnosis permutation procedure; regenerate stratification after permutation.
3. `10a_goal1_bootstrap_and_figure_recovery_final.ipynb` — governed recovery and
   post-processing from saved final out-of-fold predictions, when required.
4. `10b_goal1_sensitivity_completion_final_v1_0.ipynb` — prespecified sensitivity
   analyses and computational completion package.
5. `10c_goal1_publication_figures_final_v1_2.ipynb` — final publication figures.
6. `10d_goal1_final_freeze_v1_0.ipynb` — final validation gates and Goal-1 DONE
   seal.

Development notebook:
`10_goal1_primary_analysis_development_v1_1_300_bootstraps.ipynb`. Its saved
execution used 300 bootstraps rather than the final 2,000, so it is retained for
development provenance and is not manuscript authority.

### Goal 2 — consequence for acoustic inference

1. `18_goal2_bamboo_acoustic_feature_extraction_final_v2_1.ipynb` — outcome-blind
   Bamboo Passage acoustic-feature extraction.
2. `19_goal2_bamboo_acoustic_representation_freeze_final_v2_1.ipynb` — freeze the
   clinical acoustic representation A.
3. `20_goal2_primary_inference_final_v1_1_2000_bootstraps.ipynb` — final primary
   inference analysis with 2,000 participant bootstraps.
4. `21_goal2_sensitivity_completion_final_v1_0_1.ipynb` — authoritative
   sensitivity/completion layer, including fold-local residualizer tuning.
5. `22_goal2_publication_figures_and_freeze_final_v1_2.ipynb` — publication figures
   and Goal-2 DONE seal.

Non-authoritative notebooks:

- `20_goal2_primary_inference_development_v1_1_300_bootstraps.ipynb` — reduced
  300-bootstrap development execution.
- `21_goal2_sensitivity_completion_superseded_v1_0_2000_bootstraps.ipynb` — a
  full 2,000-bootstrap run superseded by the fold-local residualizer correction;
  it is not labeled development because its bootstrap count was already final.

They remain development provenance and are not manuscript authority. Final
manuscript-facing results are under
`outputs/goal2/goal2_completion_v1_0/final/` in the governed output package.

### Goal 3 — localization and controlled sensitivity

1. `30_goal3_stage_a_natural_qa_localization_and_freeze_final_v1_1.ipynb` — localize
   natural Q–A coupling and freeze controlled-experiment sources.
2. `31_goal3_stage_b_perturbation_calibration_prepare_final_v1_0.ipynb` — prepare the
   outcome-blind signal-only perturbation candidate grid.
3. `32_goal3_stage_b_perturbation_calibration_execute_final_v1_1.ipynb` — execute
   signal-only calibration.
4. Run `goal3_stageB_v1_2_targeted_revision.py`, then
   `goal3_stageB_v1_3_targeted_revision.py` — targeted outcome-blind revisions
   that lead to the sealed perturbation manifest.
5. `33_goal3_stage_c_qa_measurement_preflight_final_v1_0_2.ipynb` — validate Q+A
   measurement and reproduce the frozen-A implementation before the full run.
6. `34_goal3_stage_d_goal2_model_bundle_bridge_final_v1_0_1.ipynb` — create five
   fold-specific frozen Goal-2 bundles and verify exact out-of-fold reproduction.
7. `35_goal3_stage_e_controlled_perturbation_final_v1_1_1_2000_bootstraps.ipynb`
   — authoritative
   Stage-E completion. It reuses all 14,792 waveform checkpoints from v1.1.0,
   corrects the support-summary reduction, and records prediction-unavailability
   audits without changing estimands or rerunning waveform measurements.
8. `36_goal3_stage_f_robustness_and_completion_final_v1_0.ipynb` — complete robustness
   analyses, including exact frozen HGB reproduction.
9. `37_goal3_stage_f_publication_figures_final_v1_0.ipynb` — create the publication
   figure package for manual approval and final sealing.

Non-authoritative notebooks:

- `33_goal3_stage_gate_audit_superseded.ipynb` — an early gate-presence audit;
  it is not part of the authoritative execution path.
- `35_goal3_stage_e_controlled_perturbation_checkpoint_execution_v1_1_0_2000_bootstraps.ipynb`
  — the full-scale Stage-E execution that created the retained waveform
  checkpoints; it is not a reduced-bootstrap development notebook. The v1.1.1
  completion patch is the release authority.

The final Goal-3 freeze is preserved in the governed outputs as
`GOAL3_FINAL_FREEZE.json` and `DONE.json`. Figure finalization did not rerun
waveform measurements, models, GEE analyses, or bootstrap analyses.

## Before running anything

1. Read [`../docs/ANALYSIS_LINEAGE.md`](../docs/ANALYSIS_LINEAGE.md).
2. Confirm access to the governed inputs described in
   [`../data/README.md`](../data/README.md).
3. Select the environment described in
   [`../docs/REPRODUCIBILITY.md`](../docs/REPRODUCIBILITY.md).
4. Treat existing freeze manifests and outputs as immutable.

For checksum-level release evidence, see
[`../docs/FROZEN_OUTPUT_AUDIT.md`](../docs/FROZEN_OUTPUT_AUDIT.md).

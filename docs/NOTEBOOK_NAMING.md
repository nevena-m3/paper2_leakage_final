# Notebook naming and rename record

## Purpose

Notebook filenames were standardized after the scientific freeze to make the
repository easier to review and execute. Edits inside notebooks were restricted
to filename literals required for notebook-to-notebook discovery and related
explanatory text. No computation, parameter, model, estimand, result, stored
output, or notebook metadata was changed.

The original names remain important because frozen manifests, contemporaneous
records, and external notes may cite them. This table provides the permanent
translation.

## Rename map

| Original filename | Current filename |
| --- | --- |
| `00_phase0_data_audit.ipynb` | `00_phase0_data_audit_and_freeze_final.ipynb` |
| `01_phase0_qchan_reference_cache.ipynb` | `01_phase0_qchan_reference_cache_final.ipynb` |
| `10_goal1_COMPLETE_REBUILT_v1_1.ipynb` | `10_goal1_primary_analysis_development_v1_1_300_bootstraps.ipynb` |
| `10_goal1_COMPLETE_REBUILT_v1_1_final2000BS.ipynb` | `10_goal1_primary_analysis_final_v1_1_2000_bootstraps.ipynb` |
| `10A_goal1_recover_bootstrap_and_figures.ipynb` | `10a_goal1_bootstrap_and_figure_recovery_final.ipynb` |
| `10B_goal1_FINALIZE_sensitivities_figures_v1_0.ipynb` | `10b_goal1_sensitivity_completion_final_v1_0.ipynb` |
| `10C_goal1_PUBLICATION_figures_FINAL_v1_2.ipynb` | `10c_goal1_publication_figures_final_v1_2.ipynb` |
| `10D_goal1_FINAL_FREEZE_v1_0.ipynb` | `10d_goal1_final_freeze_v1_0.ipynb` |
| `18_goal2_BAMBOO_acoustic_extraction_v2_1.ipynb` | `18_goal2_bamboo_acoustic_feature_extraction_final_v2_1.ipynb` |
| `19_goal2_BAMBOO_acoustic_representation_freeze_v2_1.ipynb` | `19_goal2_bamboo_acoustic_representation_freeze_final_v2_1.ipynb` |
| `20_goal2_inference_consequence_PRIMARY_v1_1.ipynb` | `20_goal2_primary_inference_development_v1_1_300_bootstraps.ipynb` |
| `20_goal2_inference_consequence_PRIMARY_v1_1_with2000BS.ipynb` | `20_goal2_primary_inference_final_v1_1_2000_bootstraps.ipynb` |
| `21_goal2_COMPLETION_sensitivities_and_seal_v1_0.ipynb` | `21_goal2_sensitivity_completion_superseded_v1_0_2000_bootstraps.ipynb` |
| `21_goal2_COMPLETION_sensitivities_and_seal_v1_0_1.ipynb` | `21_goal2_sensitivity_completion_final_v1_0_1.ipynb` |
| `22_goal2_final_figures.ipynb` | `22_goal2_publication_figures_and_freeze_final_v1_2.ipynb` |
| `30_goal3_natural_QA_localization_and_experiment_freeze_v1_1.ipynb` | `30_goal3_stage_a_natural_qa_localization_and_freeze_final_v1_1.ipynb` |
| `31_goal3_signal_only_perturbation_calibration_PREP_v1_0.ipynb` | `31_goal3_stage_b_perturbation_calibration_prepare_final_v1_0.ipynb` |
| `32_goal3_signal_only_perturbation_calibration_EXECUTE_v1_1.ipynb` | `32_goal3_stage_b_perturbation_calibration_execute_final_v1_1.ipynb` |
| `33_AUDIT_of_GOAL_3.ipynb` | `33_goal3_stage_gate_audit_superseded.ipynb` |
| `33_goal3_controlled_QA_measurement_PREFLIGHT_v1_0_2.ipynb` | `33_goal3_stage_c_qa_measurement_preflight_final_v1_0_2.ipynb` |
| `34_goal3_Goal2_model_bundle_bridge_FINAL_v1_0_1.ipynb` | `34_goal3_stage_d_goal2_model_bundle_bridge_final_v1_0_1.ipynb` |
| `35_goal3_controlled_perturbation_PRIMARY_FINAL_v1_1_0.ipynb` | `35_goal3_stage_e_controlled_perturbation_checkpoint_execution_v1_1_0_2000_bootstraps.ipynb` |
| `35_goal3_controlled_perturbation_PRIMARY_FINAL_v1_1_1.ipynb` | `35_goal3_stage_e_controlled_perturbation_final_v1_1_1_2000_bootstraps.ipynb` |
| `36_goal3_FINALIZE_robustness_and_completion_v1_0.ipynb` | `36_goal3_stage_f_robustness_and_completion_final_v1_0.ipynb` |
| `37_goal3_PUBLICATION_figures_v1_0.ipynb` | `37_goal3_stage_f_publication_figures_final_v1_0.ipynb` |

## Status vocabulary

- `development`: the recorded execution used fewer bootstrap replicates than
  the final analysis (300 rather than 2,000).
- `final`: part of the manuscript-authoritative execution path.
- `superseded`: non-authoritative for a reason other than reduced bootstrap
  count, such as a later protocol-concordance correction.
- `checkpoint_execution`: a full-scale run that generated retained checkpoints
  consumed by a later final completion patch.

## Integrity rule

The scientific freeze tags remain immutable and continue to expose the original
filenames and original Git blob identities. The publication branch records the
renames and narrowly scoped path-reference updates in a separate commit. Future
notebook changes should receive separate scientific review.

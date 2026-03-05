# Unit TASK: stochastic_process

## Snapshot
- last_updated: 2026-03-06
- overall_progress: 100
- current_focus: maintain list.txt alignment and notebook reproducibility

| id | title | status | progress | updated_at | notes |
| --- | --- | --- | --- | --- | --- |
| STP-001 | Implement one-sequence user input mean + autocorrelation script | done | 100 | 2026-03-06 | added `stochastic_process_sequence_mean_autocorrelation.py` |
| STP-002 | Implement two-sequence user input auto/cross-correlation script | done | 100 | 2026-03-06 | added `stochastic_process_two_sequence_correlation.py` |
| STP-003 | Implement weakly correlated stock pair cross-correlation (2025) | done | 100 | 2026-03-06 | added `stochastic_process_weak_stock_cross_correlation_2025.py` |
| STP-004 | Implement strongly correlated stock pair cross-correlation (2025) | done | 100 | 2026-03-06 | added `stochastic_process_strong_stock_cross_correlation_2025.py` |
| STP-005 | Implement covariance matrix of A,B,C,D (2025) | done | 100 | 2026-03-06 | added `stochastic_process_covariance_matrix_2025.py` |
| STP-006 | Keep existing lecture-demo scripts organized and runnable | cancelled | - | 2026-03-06 | old 4 lecture-demo scripts removed in STP-011; only list.txt-aligned scripts remain |
| STP-007 | Add paired notebook `stochastic_process_walkthrough.ipynb` | done | 100 | 2026-03-06 | rebuilt as integrated five-section executable notebook with charts |
| STP-008 | Add LaTeX formulas and requirement mapping table in spec/notebook | done | 100 | 2026-03-06 | added formulas and mapping table in `SPECS/units/stochastic_process/sdd.md` and notebook |
| STP-009 | Record implementation issues and follow-up tasks | done | 100 | 2026-03-06 | issue log updated with actions and outcomes |
| STP-010 | Stabilize notebook execution environment notes | todo | 0 | 2026-03-06 | document optional Windows event-loop warning handling for nbconvert |
| STP-011 | Remove old lecture-demo scripts not in list.txt | done | 100 | 2026-03-06 | deleted discrete_correlation, covariance_matrix, time_averages, stationarity_demo; cleaned __pycache__; updated SDD |
| STP-012 | Verify notebook formulas match Stochastic_Process.md | done | 100 | 2026-03-06 | all formulas (mean, autocorrelation, cross-correlation, covariance matrix) confirmed consistent with source material; numerical outputs match examples |

## Issue Log
| id | issue | impact | status | action |
| --- | --- | --- | --- | --- |
| I-001 | Existing walkthrough notebook imports `stochastic_process_brief_utils`, which does not exist. | Notebook cannot run end-to-end. | closed | Rebuilt notebook with integrated logic matching the five scripts. |
| I-002 | First notebook generation attempt corrupted markdown due shell escaping. | Formulas rendered incorrectly. | closed | Rebuilt notebook via controlled Python generator and re-executed in virtualenv. |
| I-003 | `nbconvert` run shows Windows zmq event-loop runtime warning. | Notebook still executes successfully; warning may confuse users. | open | Add follow-up task STP-010 to document optional warning mitigation. |

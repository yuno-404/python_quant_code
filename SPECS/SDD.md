# Software Design Document (SDD)

## Core principles
- Each topic must deliver two outputs: one `.py` script and one `.ipynb` notebook.
- Use function-first style.
- Pass parameters explicitly and avoid sample defaults in function definitions.
- Add comments only for key math steps or non-obvious logic.
- Track every task with `status`, `progress`, and `updated_at`.

## Minimum folder structure

```text
scripts/<unit_name>/
notebooks/<unit_name>/
SPECS/units/<unit_name>/spec.md
SPECS/units/<unit_name>/sdd.md
SPECS/units/<unit_name>/task.md
```

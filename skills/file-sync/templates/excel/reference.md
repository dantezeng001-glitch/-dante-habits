# Reference

## Required Project Files

- `tools/excel_sync.py`: scans project Excel files and exports each sheet into `cursor_excel/` as `.md` only, plus `index.md`
- `tools/watch_excel.py`: polls for workbook or config changes and reruns sync
- `excel_sync_config.json`: file patterns, exclude patterns, output directory
- `.cursor/rules/excel-sync.mdc`: tells Cursor to prefer synced artifacts over direct `.xlsx` reads
- `.vscode/tasks.json`: includes `Excel: sync once` and `Excel: watch sync`
- `EXCEL_SYNC_README.md`: explains usage inside the project

## Merge Guidance

### Existing `.vscode/tasks.json`

- Preserve unrelated tasks
- Add or update the two Excel tasks by label:
  - `Excel: sync once`
  - `Excel: watch sync`
- Keep `runOn: folderOpen` for the watcher task

### Existing `.cursor/rules/`

- Add `excel-sync.mdc`
- Do not remove unrelated rules

### Existing `tools/`

- Reuse the folder
- Overwrite only the two Excel sync scripts if the user asked to install or refresh the workflow

## Template Files

Read these files directly and copy their content into the target project when installing:

- [template_excel_sync.py](template_excel_sync.py)
- [template_watch_excel.py](template_watch_excel.py)
- [template_config.json](template_config.json)
- [template_rule.mdc](template_rule.mdc)
- [template_tasks.json](template_tasks.json)
- [template_readme.md](template_readme.md)

## Verification Checklist

- Python is available
- `openpyxl` imports successfully
- `python "tools/excel_sync.py"` exits successfully
- `cursor_excel/index.md` exists
- At least one workbook is listed when Excel files are present
- No new linter errors in the installed Python files

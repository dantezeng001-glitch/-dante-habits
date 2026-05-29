from __future__ import annotations

import argparse
import time
from pathlib import Path

from excel_sync import CONFIG_FILE_NAME, discover_workbooks, load_config, run_sync


def snapshot(project_root: Path) -> dict[str, tuple[int, int]]:
    config = load_config(project_root)
    items: dict[str, tuple[int, int]] = {}

    config_path = project_root / CONFIG_FILE_NAME
    if config_path.exists():
        stat = config_path.stat()
        items[str(config_path.resolve())] = (stat.st_mtime_ns, stat.st_size)

    for workbook_path in discover_workbooks(project_root, config):
        stat = workbook_path.stat()
        items[str(workbook_path.resolve())] = (stat.st_mtime_ns, stat.st_size)

    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Watch Excel files and keep cursor_excel in sync.")
    parser.add_argument(
        "--project-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Project root that contains the Excel files.",
    )
    parser.add_argument(
        "--interval",
        default=5,
        type=int,
        help="Polling interval in seconds.",
    )
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    interval = max(args.interval, 2)

    print(f"Initial sync for: {project_root}")
    manifests = run_sync(project_root)
    print(f"Watching {len(manifests)} workbook(s) every {interval} seconds. Press Ctrl+C to stop.")

    previous = snapshot(project_root)
    try:
        while True:
            time.sleep(interval)
            current = snapshot(project_root)
            if current == previous:
                continue

            print("Detected Excel or config changes. Running sync...")
            manifests = run_sync(project_root)
            print(f"Sync complete. Tracking {len(manifests)} workbook(s).")
            previous = current
    except KeyboardInterrupt:
        print("Excel watcher stopped.")


if __name__ == "__main__":
    main()

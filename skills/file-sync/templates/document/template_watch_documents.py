from __future__ import annotations

import argparse
import time
from pathlib import Path

from document_sync import CONFIG_FILE_NAME, discover_documents, load_config, run_sync


def snapshot(project_root: Path) -> dict[str, tuple[int, int]]:
    config = load_config(project_root)
    items: dict[str, tuple[int, int]] = {}

    config_path = project_root / CONFIG_FILE_NAME
    if config_path.exists():
        stat = config_path.stat()
        items[str(config_path.resolve())] = (stat.st_mtime_ns, stat.st_size)

    for doc_path in discover_documents(project_root, config):
        stat = doc_path.stat()
        items[str(doc_path.resolve())] = (stat.st_mtime_ns, stat.st_size)

    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Watch PDF and presentation files and keep cursor_docs in sync.")
    parser.add_argument(
        "--project-root",
        default=Path(__file__).resolve().parents[1],
        type=Path,
        help="Project root that contains the source documents.",
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
    print(f"Watching {len(manifests)} document(s) every {interval} seconds. Press Ctrl+C to stop.")

    previous = snapshot(project_root)
    try:
        while True:
            time.sleep(interval)
            current = snapshot(project_root)
            if current == previous:
                continue

            print("Detected document or config changes. Running sync...")
            manifests = run_sync(project_root)
            print(f"Sync complete. Tracking {len(manifests)} document(s).")
            previous = current
    except KeyboardInterrupt:
        print("Document watcher stopped.")


if __name__ == "__main__":
    main()

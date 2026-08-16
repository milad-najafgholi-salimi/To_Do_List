from .storage import write_json_file
from .report import generate_report
from pathlib import Path


def save(task_dict: dict, json_file: str, task_list: list | None = None) -> dict:
    if task_list is None:
        task_list = list(task_dict.values())

    task_dict = {
        task["UUID"]: task
        for task in task_list
    }

    write_json_file(json_file, task_list)
    print(f"\nTasks file Saved to: {json_file}\n")

    report_dict = generate_report(task_list)

    path = Path(json_file)

    report_dir = path.parent / "report"

    report_dir.mkdir(exist_ok=True)

    report_file = report_dir / f"{path.stem}_report.json"

    write_json_file(str(report_file), [report_dict])

    print(f"Report file saved to: {report_file}\n")

    return task_dict
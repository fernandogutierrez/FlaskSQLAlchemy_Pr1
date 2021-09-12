from pathlib import Path
import os


def get_project_path():
    current_dir = Path(os.path.abspath(os.path.dirname(__file__)))
    return str(current_dir.parent.parent)


def get_sqlite_path():
    return os.path.join(get_project_path(), 'database', 'db.sqlite')

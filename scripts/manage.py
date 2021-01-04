#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv
from pathlib import Path, PurePath

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_server.settings.base')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    scripts_path = sys.path[0]
    scripts_dirs = scripts_path.split('/')
    scripts_dirs.pop()
    sys.path.append('/'.join(scripts_dirs))

    file_path = Path(__file__).parent.absolute()
    root_path = Path(file_path).parent.absolute()
    dotenv_path = PurePath(root_path, '.env')
    dotenv.read_dotenv(dotenv_path)
    main()

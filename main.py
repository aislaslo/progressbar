from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

import time

progress = Progress(*Progress.get_default_columns(), TimeElapsedColumn(), SpinnerColumn())

with progress:

    task = progress.add_task("Downloading...",total=100)

    while not progress.finished:
    
        progress.update(task, advance=10)

        time.sleep(2)
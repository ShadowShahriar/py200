import calendar
from datetime import datetime
from rich.console import Console
from rich.table import Table

now = datetime.now()
year = now.year
month = now.month
calendar.setfirstweekday(calendar.SUNDAY)


def colorful_calendar(year, mm):
    console = Console()
    table = Table(
        title=f"[bold cyan]{calendar.month_name[mm]} {year}[/bold cyan]",
        show_lines=True,
    )
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    for day in days:
        style = "green"
        if day == "Sat" or day == "Sun":
            style = "red"
        table.add_column(day, justify="center", header_style=style)

    month = calendar.monthcalendar(year, mm)

    for week in month:
        table.add_row(*[str(day) if day != 0 else "" for day in week], style="white")
    console.print(table)


colorful_calendar(year, month)

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        date_gen = ''
        for date_pare in self.dates:
            date_start = date_pare[0]
            date_end = date_pare[1]
            date_delta = date_end - date_start
            date_gen = (date_start + timedelta(days=x) for x in range(1, date_delta.days + 1))

        return date_gen


m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    # (datetime(2020, 1, 15), datetime(2020, 2, 7))
])

for d in m.schedule():
    print(d)

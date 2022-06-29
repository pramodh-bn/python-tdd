from datetime import date
from typing import List

from typeguard import typechecked

@typechecked
class TypeCheckSong:
    def __init__(
        self,
        id: int,
        name: str,
        release: date,
        genres: List[str]
    ) -> None:
        self.id = id
        self.name = name
        self.release = release
        self.genres = genres

song = TypeCheckSong(
    id=101,
    name='Bohemian Rhapsody',
    release=date(1975, 10, 31),
    genres={
        'Hard Rock',
        'Progressive Rock'
    }
)

print(song)

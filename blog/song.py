from datetime import date
from typing import List

from pydantic import BaseModel, validator

class Song(BaseModel):
    id: int
    name: str
    release: date
    genres: List[str]

    @validator('genres', pre=True, always=True)
    def to_lower_case(cls, v):
        return [genre.lower() for genre in v]

    @validator('genres')
    def no_duplicates_in_genre(cls, v):
        if len(set(v)) != len(v):
            raise ValueError(
                'No duplicates allowed in genre.'
            )
        return v


song = Song(
    id=101,
    name='Bohemian Rhapsody',
    release='1975-10-31',
    genres=[
        'Hard Rock',
        'Progressive rock',
        'Progressive Rock'
    ]
)
print(song)

from typing import Tuple, Dict
from typing import List
from typing import Union

def daily_average(temperatures: List[float]) -> float:
    return sum(temperatures)/len(temperatures)

print(daily_average.__annotations__)
average_temperature = daily_average([22.9, 19.6, 25.9])
print(average_temperature)

# type hinting
def sum_xy(x: 'an integer', y: 'another integer') -> int:
    return x+y

print(sum_xy.__annotations__)

def generate_map(points: Tuple[float, float]) -> Dict[str, int]:
    return map(points)

def sum_ab(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a+b

def sort_names(names: list[str]) -> list[str]:
    return sorted(names)

# mypy is a tool for checking at compile time
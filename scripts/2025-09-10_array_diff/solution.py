from typing import List

def array_diff(arr1: List[str], arr2: List[str]) -> List[str]:
    diff = list(set(arr1) ^ set(arr2))
    diff.sort()

    return diff
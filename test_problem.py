import sys

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


def find_closest_elements(elements):
    sort_elements = sorted(elements)
    diff = sys.maxsize
    for i in range(len(sort_elements)):
        j = i + 1
        if j < len(sort_elements):
            tmp_diff = abs(sort_elements[j] - sort_elements[i])
            if tmp_diff < diff:
                diff = tmp_diff

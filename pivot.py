def find_pivot(numbers: list):
    if len(numbers) <= 2:
        return -1

    left = numbers[0]
    right = sum(numbers)
    for i in range(1, len(numbers) - 1):
        left += numbers[i - 1]
        right -= numbers[i]
        if left == right:
            return i

    return -1


def test_find_pivot():
    assert find_pivot([]) == -1
    assert find_pivot([0]) == -1
    assert find_pivot([0, 1]) == -1
    assert find_pivot([0, 1]) == -1
    assert find_pivot([1, 0, 1]) == 1
    assert find_pivot([1, 0, 2]) == -1
    assert find_pivot([2, 0, 1]) == -1
    assert find_pivot([1, 1, 0, 1]) == 1
    assert find_pivot([1, 0, 0, 1]) == 1
    assert find_pivot([1, 0, 1, 1]) == 2
    assert find_pivot([1, 1, 1, 1]) == -1
    assert find_pivot([1, 4, 6, 3, 2]) == 2
    assert find_pivot([1, 4, 6, 3, 11]) == 3
    assert find_pivot([1, 4, 6, 3, 5, 6]) == 3

"""
练习 4：推导式 - 答案
"""


def squares(n):
    """
    返回 1 到 n 的平方列表
    """
    return [x**2 for x in range(1, n + 1)]


def filter_evens(numbers):
    """
    筛选偶数
    """
    return [x for x in numbers if x % 2 == 0]


def create_square_dict(n):
    """
    创建数字到平方的字典
    """
    return {x: x**2 for x in range(1, n + 1)}


def unique_lengths(words):
    """
    返回单词长度的集合
    """
    return {len(w) for w in words}


# ============ 测试代码 ============

def test_squares():
    assert squares(5) == [1, 4, 9, 16, 25]
    assert squares(3) == [1, 4, 9]
    assert squares(1) == [1]

def test_filter_evens():
    assert filter_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert filter_evens([1, 3, 5]) == []
    assert filter_evens([2, 4, 6]) == [2, 4, 6]

def test_create_square_dict():
    assert create_square_dict(3) == {1: 1, 2: 4, 3: 9}
    assert create_square_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def test_unique_lengths():
    assert unique_lengths(["hi", "hello", "go"]) == {2, 5}
    assert unique_lengths(["a", "bb", "ccc"]) == {1, 2, 3}
    assert unique_lengths(["same", "size"]) == {4}


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

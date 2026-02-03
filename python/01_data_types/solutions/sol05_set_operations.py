"""
练习 5：集合运算 - 答案
"""


def union(a, b):
    """
    并集
    """
    return a | b


def intersection(a, b):
    """
    交集
    """
    return a & b


def difference(a, b):
    """
    差集
    """
    return a - b


def symmetric_difference(a, b):
    """
    对称差集
    """
    return a ^ b


def remove_duplicates(lst):
    """
    去重
    """
    return list(set(lst))


# ============ 测试代码 ============

def test_union():
    assert union({1, 2, 3}, {3, 4, 5}) == {1, 2, 3, 4, 5}
    assert union({1, 2}, {3, 4}) == {1, 2, 3, 4}

def test_intersection():
    assert intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}
    assert intersection({1, 2}, {3, 4}) == set()

def test_difference():
    assert difference({1, 2, 3, 4}, {3, 4, 5}) == {1, 2}
    assert difference({1, 2}, {1, 2}) == set()

def test_symmetric_difference():
    assert symmetric_difference({1, 2, 3}, {3, 4, 5}) == {1, 2, 4, 5}

def test_remove_duplicates():
    result = remove_duplicates([1, 2, 2, 3, 3, 3])
    assert set(result) == {1, 2, 3}
    assert len(result) == 3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

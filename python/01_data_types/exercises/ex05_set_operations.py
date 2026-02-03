"""
练习 5：集合运算

运行测试：python -m pytest ex05_set_operations.py -v
"""


def union(a, b):
    """
    返回两个集合的并集
    """
    # TODO: 实现此函数
    pass


def intersection(a, b):
    """
    返回两个集合的交集
    """
    # TODO: 实现此函数
    pass


def difference(a, b):
    """
    返回 a 中有但 b 中没有的元素（差集）
    """
    # TODO: 实现此函数
    pass


def symmetric_difference(a, b):
    """
    返回只在一个集合中出现的元素（对称差集）
    """
    # TODO: 实现此函数
    pass


def remove_duplicates(lst):
    """
    去除列表中的重复元素，返回新列表
    注意：不要求保持顺序
    """
    # TODO: 实现此函数
    pass


# ============ 测试代码（不要修改）============

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

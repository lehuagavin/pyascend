"""
练习 4：推导式

运行测试：python -m pytest ex04_comprehension.py -v
"""


def squares(n):
    """
    返回 1 到 n 的平方列表
    使用列表推导式实现
    
    示例：squares(5) -> [1, 4, 9, 16, 25]
    """
    # TODO: 实现此函数
    pass


def filter_evens(numbers):
    """
    从列表中筛选出偶数
    使用列表推导式实现
    
    示例：filter_evens([1,2,3,4,5]) -> [2, 4]
    """
    # TODO: 实现此函数
    pass


def create_square_dict(n):
    """
    创建数字到其平方的字典
    使用字典推导式实现
    
    示例：create_square_dict(3) -> {1: 1, 2: 4, 3: 9}
    """
    # TODO: 实现此函数
    pass


def unique_lengths(words):
    """
    返回单词长度的集合（去重）
    使用集合推导式实现
    
    示例：unique_lengths(["hi", "hello", "go"]) -> {2, 5}
    """
    # TODO: 实现此函数
    pass


# ============ 测试代码（不要修改）============

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

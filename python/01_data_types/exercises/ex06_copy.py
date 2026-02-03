"""
练习 6：浅拷贝与深拷贝

运行测试：python -m pytest ex06_copy.py -v
"""

import copy


def shallow_copy(obj):
    """
    返回对象的浅拷贝
    """
    # TODO: 实现此函数
    pass


def deep_copy(obj):
    """
    返回对象的深拷贝
    """
    # TODO: 实现此函数
    pass


def is_shallow_copy_affected(original, copied):
    """
    判断：修改 copied 的内部列表后，original 是否会受影响
    
    参数：original 和 copied 都是包含列表的字典
    返回：True 如果会受影响，False 如果不会
    
    提示：这个函数用于理解浅拷贝的特性
    """
    # TODO: 实现此函数
    # 修改 copied 中的内部列表，检查 original 是否变化
    pass


# ============ 测试代码（不要修改）============

def test_shallow_copy_creates_new_object():
    original = [1, 2, 3]
    copied = shallow_copy(original)
    assert copied == original
    assert copied is not original

def test_shallow_copy_inner_same():
    original = [[1, 2], [3, 4]]
    copied = shallow_copy(original)
    # 内部列表是同一个对象
    assert copied[0] is original[0]

def test_deep_copy_creates_new_object():
    original = [[1, 2], [3, 4]]
    copied = deep_copy(original)
    assert copied == original
    assert copied is not original

def test_deep_copy_inner_different():
    original = [[1, 2], [3, 4]]
    copied = deep_copy(original)
    # 内部列表也是不同对象
    assert copied[0] is not original[0]

def test_shallow_copy_affected():
    original = {"data": [1, 2, 3]}
    copied = shallow_copy(original)
    assert is_shallow_copy_affected(original, copied) == True

def test_deep_copy_not_affected():
    original = {"data": [1, 2, 3]}
    copied = deep_copy(original)
    # 深拷贝不会互相影响
    copied["data"].append(99)
    assert original["data"] == [1, 2, 3]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

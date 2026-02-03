"""
练习 6：浅拷贝与深拷贝 - 答案
"""

import copy


def shallow_copy(obj):
    """
    浅拷贝
    """
    return copy.copy(obj)


def deep_copy(obj):
    """
    深拷贝
    """
    return copy.deepcopy(obj)


def is_shallow_copy_affected(original, copied):
    """
    浅拷贝时，修改内部对象会影响原对象
    """
    # 获取原始值
    original_value = original["data"].copy()
    
    # 修改 copied 的内部列表
    copied["data"].append(999)
    
    # 检查 original 是否被影响
    affected = original["data"] != original_value
    
    return affected


# ============ 测试代码 ============

def test_shallow_copy_creates_new_object():
    original = [1, 2, 3]
    copied = shallow_copy(original)
    assert copied == original
    assert copied is not original

def test_shallow_copy_inner_same():
    original = [[1, 2], [3, 4]]
    copied = shallow_copy(original)
    assert copied[0] is original[0]

def test_deep_copy_creates_new_object():
    original = [[1, 2], [3, 4]]
    copied = deep_copy(original)
    assert copied == original
    assert copied is not original

def test_deep_copy_inner_different():
    original = [[1, 2], [3, 4]]
    copied = deep_copy(original)
    assert copied[0] is not original[0]

def test_shallow_copy_affected():
    original = {"data": [1, 2, 3]}
    copied = shallow_copy(original)
    assert is_shallow_copy_affected(original, copied) == True

def test_deep_copy_not_affected():
    original = {"data": [1, 2, 3]}
    copied = deep_copy(original)
    copied["data"].append(99)
    assert original["data"] == [1, 2, 3]


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

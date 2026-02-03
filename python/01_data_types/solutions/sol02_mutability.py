"""
练习 2：可变性理解 - 答案
"""


def append_to_list(lst, value):
    """
    向列表追加元素，返回修改后的列表
    """
    lst.append(value)
    return lst


def modify_tuple(t):
    """
    返回新元组（元组不可变，必须创建新的）
    """
    return t + (99,)


def check_same_object(a, b):
    """
    检查是否是同一个对象
    """
    return a is b


# ============ 测试代码 ============

def test_append_to_list():
    lst = [1, 2, 3]
    original_id = id(lst)
    result = append_to_list(lst, 4)
    assert result == [1, 2, 3, 4]
    assert id(result) == original_id

def test_modify_tuple():
    t = (1, 2, 3)
    result = modify_tuple(t)
    assert result == (1, 2, 3, 99)
    assert t == (1, 2, 3)

def test_check_same_object_true():
    a = [1, 2, 3]
    b = a
    assert check_same_object(a, b) == True

def test_check_same_object_false():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert check_same_object(a, b) == False


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

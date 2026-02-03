"""
练习 2：可变性理解

运行测试：python -m pytest ex02_mutability.py -v
"""


def append_to_list(lst, value):
    """
    向列表追加元素，返回修改后的列表
    要求：原地修改，不创建新列表
    """
    # TODO: 实现此函数
    lst.append(value)
    return lst


def modify_tuple(t):
    """
    尝试修改元组，返回新元组（在原元组基础上追加元素 99）
    
    示例：(1, 2, 3) -> (1, 2, 3, 99)
    """
    # TODO: 实现此函数
    return(t + (99,))


def check_same_object(a, b):
    """
    检查 a 和 b 是否是同一个对象（使用 is）
    返回 True 或 False
    """
    # TODO: 实现此函数
    return a is b


# ============ 测试代码（不要修改）============

def test_append_to_list():
    lst = [1, 2, 3]
    original_id = id(lst)
    result = append_to_list(lst, 4)
    assert result == [1, 2, 3, 4]
    assert id(result) == original_id  # 必须是同一个对象

def test_modify_tuple():
    t = (1, 2, 3)
    result = modify_tuple(t)
    assert result == (1, 2, 3, 99)
    assert t == (1, 2, 3)  # 原元组不变

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

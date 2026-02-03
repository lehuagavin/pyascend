"""
练习 1：类型判断

运行测试：python -m pytest ex01_type_check.py -v
"""


def get_type_name(value):
    """
    返回值的类型名称（字符串）
    
    示例：
        get_type_name(42) -> "int"
        get_type_name([1,2]) -> "list"
    """
    # TODO: 实现此函数
    return(type(value).__name__)


# ============ 测试代码（不要修改）============

def test_int():
    assert get_type_name(1) == "int"

def test_float():
    assert get_type_name(1.0) == "float"

def test_str():
    assert get_type_name("hello") == "str"

def test_list():
    assert get_type_name([1, 2, 3]) == "list"

def test_tuple():
    assert get_type_name((1,)) == "tuple"

def test_set():
    assert get_type_name({1, 2}) == "set"

def test_dict():
    assert get_type_name({"a": 1}) == "dict"

def test_none():
    assert get_type_name(None) == "NoneType"


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

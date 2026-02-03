"""
练习 3：is 和 == 的区别

运行测试：python -m pytest ex03_is_vs_equal.py -v
"""


def compare_values(a, b):
    """
    比较两个值是否相等（使用 ==）
    """
    # TODO: 实现此函数
    pass


def compare_identity(a, b):
    """
    比较两个变量是否指向同一个对象（使用 is）
    """
    # TODO: 实现此函数
    pass


def is_none(value):
    """
    检查值是否为 None（使用推荐的方式）
    """
    # TODO: 实现此函数
    pass


# ============ 测试代码（不要修改）============

def test_compare_values_equal():
    assert compare_values([1, 2], [1, 2]) == True
    assert compare_values("hello", "hello") == True
    assert compare_values(42, 42) == True

def test_compare_values_not_equal():
    assert compare_values([1, 2], [1, 3]) == False
    assert compare_values("hello", "world") == False

def test_compare_identity_same():
    a = [1, 2, 3]
    b = a
    assert compare_identity(a, b) == True

def test_compare_identity_different():
    a = [1, 2, 3]
    b = [1, 2, 3]
    assert compare_identity(a, b) == False

def test_is_none_true():
    assert is_none(None) == True

def test_is_none_false():
    assert is_none(0) == False
    assert is_none("") == False
    assert is_none([]) == False


if __name__ == "__main__":
    import pytest
    pytest.main([__file__, "-v"])

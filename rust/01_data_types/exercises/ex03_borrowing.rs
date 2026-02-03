// 练习 3：借用与引用
//
// 运行测试：rustc --test ex03_borrowing.rs && ./ex03_borrowing

/// 通过不可变引用获取第一个元素
fn first_element(v: &Vec<i32>) -> Option<i32> {
    // TODO: 实现此函数
    // 返回第一个元素的拷贝，如果为空返回 None
    todo!()
}

/// 通过可变引用追加元素
fn push_element(v: &mut Vec<i32>, elem: i32) {
    // TODO: 实现此函数
    todo!()
}

/// 通过可变引用将所有元素翻倍
fn double_all(v: &mut Vec<i32>) {
    // TODO: 实现此函数
    todo!()
}

// ============ 测试代码（不要修改）============

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_element_some() {
        let v = vec![1, 2, 3];
        assert_eq!(first_element(&v), Some(1));
        // v 仍然有效
        assert_eq!(v.len(), 3);
    }

    #[test]
    fn test_first_element_none() {
        let v: Vec<i32> = vec![];
        assert_eq!(first_element(&v), None);
    }

    #[test]
    fn test_push_element() {
        let mut v = vec![1, 2, 3];
        push_element(&mut v, 4);
        assert_eq!(v, vec![1, 2, 3, 4]);
    }

    #[test]
    fn test_double_all() {
        let mut v = vec![1, 2, 3];
        double_all(&mut v);
        assert_eq!(v, vec![2, 4, 6]);
    }
}

fn main() {
    println!("运行测试来验证答案");
}

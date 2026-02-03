// 练习 4：集合类型
//
// 运行测试：rustc --test ex04_collections.rs && ./ex04_collections

use std::collections::HashMap;

/// 计算向量元素之和
fn sum_vec(v: &Vec<i32>) -> i32 {
    // TODO: 实现此函数
    todo!()
}

/// 返回向量中的最大值
fn max_vec(v: &Vec<i32>) -> Option<i32> {
    // TODO: 实现此函数
    // 如果为空返回 None
    todo!()
}

/// 统计字符串中每个字符出现的次数
fn char_count(s: &str) -> HashMap<char, i32> {
    // TODO: 实现此函数
    todo!()
}

/// 合并两个向量
fn merge_vecs(v1: Vec<i32>, v2: Vec<i32>) -> Vec<i32> {
    // TODO: 实现此函数
    todo!()
}

// ============ 测试代码（不要修改）============

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sum_vec() {
        assert_eq!(sum_vec(&vec![1, 2, 3, 4, 5]), 15);
        assert_eq!(sum_vec(&vec![]), 0);
    }

    #[test]
    fn test_max_vec() {
        assert_eq!(max_vec(&vec![1, 5, 3, 9, 2]), Some(9));
        assert_eq!(max_vec(&vec![]), None);
    }

    #[test]
    fn test_char_count() {
        let result = char_count("hello");
        assert_eq!(result.get(&'l'), Some(&2));
        assert_eq!(result.get(&'h'), Some(&1));
        assert_eq!(result.get(&'x'), None);
    }

    #[test]
    fn test_merge_vecs() {
        let v1 = vec![1, 2, 3];
        let v2 = vec![4, 5, 6];
        assert_eq!(merge_vecs(v1, v2), vec![1, 2, 3, 4, 5, 6]);
    }
}

fn main() {
    println!("运行测试来验证答案");
}

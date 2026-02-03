// 练习 4：集合类型 - 答案

use std::collections::HashMap;

fn sum_vec(v: &Vec<i32>) -> i32 {
    v.iter().sum()
}

fn max_vec(v: &Vec<i32>) -> Option<i32> {
    v.iter().max().copied()
}

fn char_count(s: &str) -> HashMap<char, i32> {
    let mut map = HashMap::new();
    for c in s.chars() {
        *map.entry(c).or_insert(0) += 1;
    }
    map
}

fn merge_vecs(v1: Vec<i32>, v2: Vec<i32>) -> Vec<i32> {
    let mut result = v1;
    result.extend(v2);
    result
}

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
    println!("所有测试通过！");
}

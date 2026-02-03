// 练习 3：借用与引用 - 答案

fn first_element(v: &Vec<i32>) -> Option<i32> {
    v.first().copied()
    // 或者：v.get(0).copied()
}

fn push_element(v: &mut Vec<i32>, elem: i32) {
    v.push(elem);
}

fn double_all(v: &mut Vec<i32>) {
    for x in v.iter_mut() {
        *x *= 2;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_first_element_some() {
        let v = vec![1, 2, 3];
        assert_eq!(first_element(&v), Some(1));
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
    println!("所有测试通过！");
}

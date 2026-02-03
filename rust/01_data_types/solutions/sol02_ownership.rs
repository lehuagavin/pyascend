// 练习 2：所有权 - 答案

fn get_length(s: &String) -> usize {
    s.len()
}

fn clone_and_append(s: &String, suffix: &str) -> String {
    let mut result = s.clone();
    result.push_str(suffix);
    result
}

fn take_and_modify(mut s: String) -> String {
    s.push('!');
    s
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_length() {
        let s = String::from("hello");
        assert_eq!(get_length(&s), 5);
        assert_eq!(s, "hello");
    }

    #[test]
    fn test_clone_and_append() {
        let s = String::from("hello");
        let result = clone_and_append(&s, " world");
        assert_eq!(result, "hello world");
        assert_eq!(s, "hello");
    }

    #[test]
    fn test_take_and_modify() {
        let s = String::from("hello");
        let result = take_and_modify(s);
        assert_eq!(result, "hello!");
    }
}

fn main() {
    println!("所有测试通过！");
}

// 练习 5：字符串 - 答案

fn concat_strings(s1: &str, s2: &str) -> String {
    format!("{}{}", s1, s2)
    // 或者：String::from(s1) + s2
}

fn to_uppercase(s: &str) -> String {
    s.to_uppercase()
}

fn char_count(s: &str) -> usize {
    s.chars().count()
}

fn first_char(s: &str) -> Option<char> {
    s.chars().next()
}

fn contains_substr(s: &str, sub: &str) -> bool {
    s.contains(sub)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_concat_strings() {
        assert_eq!(concat_strings("hello", " world"), "hello world");
        assert_eq!(concat_strings("", "test"), "test");
    }

    #[test]
    fn test_to_uppercase() {
        assert_eq!(to_uppercase("hello"), "HELLO");
        assert_eq!(to_uppercase("Rust"), "RUST");
    }

    #[test]
    fn test_char_count() {
        assert_eq!(char_count("hello"), 5);
        assert_eq!(char_count("你好"), 2);
    }

    #[test]
    fn test_first_char() {
        assert_eq!(first_char("hello"), Some('h'));
        assert_eq!(first_char(""), None);
        assert_eq!(first_char("你好"), Some('你'));
    }

    #[test]
    fn test_contains_substr() {
        assert_eq!(contains_substr("hello world", "world"), true);
        assert_eq!(contains_substr("hello", "xyz"), false);
    }
}

fn main() {
    println!("所有测试通过！");
}

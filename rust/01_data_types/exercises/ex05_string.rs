// 练习 5：字符串
//
// 运行测试：rustc --test ex05_string.rs && ./ex05_string

/// 连接两个字符串
fn concat_strings(s1: &str, s2: &str) -> String {
    // TODO: 实现此函数
    todo!()
}

/// 将字符串转为大写
fn to_uppercase(s: &str) -> String {
    // TODO: 实现此函数
    todo!()
}

/// 统计字符串中的字符数（不是字节数）
fn char_count(s: &str) -> usize {
    // TODO: 实现此函数
    // 提示：使用 .chars().count()
    todo!()
}

/// 获取字符串的第一个字符
fn first_char(s: &str) -> Option<char> {
    // TODO: 实现此函数
    todo!()
}

/// 检查字符串是否包含子串
fn contains_substr(s: &str, sub: &str) -> bool {
    // TODO: 实现此函数
    todo!()
}

// ============ 测试代码（不要修改）============

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
        assert_eq!(char_count("你好"), 2);  // 2 个字符，6 个字节
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
    println!("运行测试来验证答案");
}

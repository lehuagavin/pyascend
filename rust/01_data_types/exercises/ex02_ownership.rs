// 练习 2：所有权
//
// 运行测试：rustc --test ex02_ownership.rs && ./ex02_ownership

/// 获取字符串的长度，不获取所有权
fn get_length(s: &String) -> usize {
    // TODO: 实现此函数
    todo!()
}

/// 克隆字符串并追加内容
fn clone_and_append(s: &String, suffix: &str) -> String {
    // TODO: 实现此函数
    // 提示：先克隆 s，然后追加 suffix
    todo!()
}

/// 获取所有权并返回修改后的字符串
fn take_and_modify(mut s: String) -> String {
    // TODO: 实现此函数
    // 追加 "!" 后返回
    todo!()
}

// ============ 测试代码（不要修改）============

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_length() {
        let s = String::from("hello");
        assert_eq!(get_length(&s), 5);
        // s 仍然有效
        assert_eq!(s, "hello");
    }

    #[test]
    fn test_clone_and_append() {
        let s = String::from("hello");
        let result = clone_and_append(&s, " world");
        assert_eq!(result, "hello world");
        // 原字符串不变
        assert_eq!(s, "hello");
    }

    #[test]
    fn test_take_and_modify() {
        let s = String::from("hello");
        let result = take_and_modify(s);
        assert_eq!(result, "hello!");
        // s 已被移动，不能再使用
    }
}

fn main() {
    println!("运行测试来验证答案");
}

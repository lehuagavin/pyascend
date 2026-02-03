// 练习 1：基本类型
//
// 运行测试：cargo test --bin ex01_basic_types
// 或直接：rustc --test ex01_basic_types.rs && ./ex01_basic_types

/// 返回整数的平方
fn square(x: i32) -> i32 {
    // TODO: 实现此函数
    todo!()
}

/// 将整数转换为浮点数
fn to_float(x: i32) -> f64 {
    // TODO: 实现此函数
    todo!()
}

/// 判断是否为偶数
fn is_even(x: i32) -> bool {
    // TODO: 实现此函数
    todo!()
}

/// 返回字符的 ASCII 码（假设输入是 ASCII 字符）
fn char_to_code(c: char) -> u32 {
    // TODO: 实现此函数
    todo!()
}

// ============ 测试代码（不要修改）============

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_square() {
        assert_eq!(square(5), 25);
        assert_eq!(square(-3), 9);
        assert_eq!(square(0), 0);
    }

    #[test]
    fn test_to_float() {
        assert_eq!(to_float(42), 42.0);
        assert_eq!(to_float(-10), -10.0);
    }

    #[test]
    fn test_is_even() {
        assert_eq!(is_even(4), true);
        assert_eq!(is_even(7), false);
        assert_eq!(is_even(0), true);
    }

    #[test]
    fn test_char_to_code() {
        assert_eq!(char_to_code('A'), 65);
        assert_eq!(char_to_code('a'), 97);
        assert_eq!(char_to_code('0'), 48);
    }
}

fn main() {
    println!("运行 `cargo test` 或 `rustc --test` 来测试");
}

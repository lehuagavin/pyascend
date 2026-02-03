// 练习 1：基本类型 - 答案

fn square(x: i32) -> i32 {
    x * x
}

fn to_float(x: i32) -> f64 {
    x as f64
}

fn is_even(x: i32) -> bool {
    x % 2 == 0
}

fn char_to_code(c: char) -> u32 {
    c as u32
}

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
    println!("所有测试通过！");
}

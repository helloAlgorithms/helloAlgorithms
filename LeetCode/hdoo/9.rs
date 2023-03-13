struct Solution {}

impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        if x < 0 {
            return false;
        }
        let mut digit: u32 = 0;

        while (x / 10i32.pow(digit)) > 9 {
            digit = digit + 1;
        }
        if digit == 0 {
            return true;
        }
        digit = digit + 1;

        let mut curr: u32 = 1;

        while curr <= digit / 2 {
            if (x / 10i32.pow(digit - curr)) % 10 != (x % 10i32.pow(curr)) / 10i32.pow(curr - 1) {
                return false;
            }
            curr = curr + 1;
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        assert_eq!(true, Solution::is_palindrome(1234321));
        assert_eq!(true, Solution::is_palindrome(1));
        assert_eq!(true, Solution::is_palindrome(11));
        assert_eq!(true, Solution::is_palindrome(123321));
        assert_eq!(true, Solution::is_palindrome(2112332112));
        assert_eq!(true, Solution::is_palindrome(1237321));
        assert_eq!(false, Solution::is_palindrome(1233721));
        assert_eq!(false, Solution::is_palindrome(100));
        assert_eq!(false, Solution::is_palindrome(200000));
    }
}

fn main() {
    println!("true: {}", Solution::is_palindrome(1234321));
    println!("true: {}", Solution::is_palindrome(1));
    println!("true: {}", Solution::is_palindrome(11));
    println!("true: {}", Solution::is_palindrome(123321));
    println!("true: {}", Solution::is_palindrome(2112332112));
    println!("true: {}", Solution::is_palindrome(1237321));
    println!("false:{}", Solution::is_palindrome(1233721));
    println!("false:{}", Solution::is_palindrome(100));
    println!("false:{}", Solution::is_palindrome(200000));
}

#![allow(unused)]
use std::io::{self, BufRead};

macro_rules! scan {
    ( $string:expr, $sep:expr, $( $x:ty ),+ ) => {{
        let mut iter = $string.split($sep);
        ($(iter.next().and_then(|word| word.parse::<$x>().ok()),)*)
    }}
}

fn main() {
    let mut input_line = String::new();
    io::stdin()
        .read_line(&mut input_line)
        .expect("Failed to read line");
    let output = scan!(input_line, char::is_whitespace, i32, i32);
    println!(
        "{:?}",
        match output.0 {
            Some(a) => a,
            None => 0,
        } + match output.1 {
            Some(b) => b,
            None => 0,
        }
    );
}

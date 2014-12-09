/*
    Hex to 8x8 Bitmap
    Create a 8x8 picture that represents the value you read in
    example link: http://www.reddit.com/r/dailyprogrammer/comments/2ao99p/7142014_challenge_171_easy_hex_to_8x8_bitmap/
*/

use std::io::File;
use std::io::BufferedReader;

fn hex_to_bin(c: &str) -> &str{
  match c {
    "0" => "    ",
    "1" => "   x",
    "2" => "  x ",
    "3" => "  xx",
    "4" => " x  ",
    "5" => " x x",
    "6" => " xx ",
    "7" => " xxx",
    "8" => "x   ",
    "9" => "x  x",
    "A" => "x x ",
    "B" => "x xx",
    "C" => "xx  ",
    "D" => "xx x",
    "E" => "xxx ",
    "F" => "xxxx",
    _   => "ERROR"
  }
}

fn convert_to_binary_string(tup: &(&str,&str) ) -> String{
  let &(x, y) = tup;
  let mut res = hex_to_bin(x).to_string();
  res.push_str(hex_to_bin(y));
  return res;
}

fn main() {
  let path = Path::new("input.dat");
  let mut file = BufferedReader::new(File::open(&path));
  let lines: Vec<String> = file.lines().map(|x|
    x.unwrap()).collect();

  let mut bitmap_point: Vec<(&str,&str)> = vec![];

  //loop through each word in each line
  for line in lines.iter() {
      for com in line.as_slice().words() {
        bitmap_point.push(
          (com.slice(0,1),
          com.slice(1,2))
        );
      }
  }

  for command in bitmap_point.iter() {
    let res = convert_to_binary_string( command );
    println!("{}", res);
  }

}

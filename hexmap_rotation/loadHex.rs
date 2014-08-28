use std::io::File;
use std::io::BufferedReader;

pub fn hex_to_bin(c: char) -> String{
  String::from_str(
    match c {
    '0' => "    ",
    '1' => "   x",
    '2' => "  x ",
    '3' => "  xx",
    '4' => " x  ",
    '5' => " x x",
    '6' => " xx ",
    '7' => " xxx",
    '8' => "x   ",
    '9' => "x  x",
    'A' => "x x ",
    'B' => "x xx",
    'C' => "xx  ",
    'D' => "xx x",
    'E' => "xxx ",
    'F' => "xxxx",
    _   => "ERROR"
  })
}

pub fn convert_to_binary_string(ss: &String ) -> String{
  let mut result: String = String::from_str("");
  //loop through each word in the string
  for word in ss.as_slice().words() {
    //loop through each character in each word
    for ch in word.chars() {
      result.push_str(hex_to_bin(ch).as_slice());
    }
  }
  result
}

pub fn read_file(filename: &str) -> Vec<String> {
  let path = Path::new(filename);
  let mut file = BufferedReader::new(File::open(&path));
  let lines: Vec<String> = file.lines().map(|x|
    x.unwrap()).collect();

  let mut bitmap_point: Vec<String> = vec![];

  //loop through each word in each line
  for line in lines.iter() {
    for com in line.as_slice().words() {
        bitmap_point.push(
          String::from_str(com)
        );
      }
  }

  return bitmap_point;

}

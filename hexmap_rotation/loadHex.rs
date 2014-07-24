use std::io::File;
use std::io::BufferedReader;

pub fn hex_to_bin(c: &str) -> &str{
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

pub fn hex_to_dec(c: String) -> uint{
  let dat = c.into_ascii().get(0).to_char();
  return dat.to_digit(16).unwrap();
}

pub fn convert_to_binary_string(tup: &(String,String) ) -> String{
  let &(ref x, ref y) = tup;
  hex_to_bin(x.as_slice()).to_string().append(hex_to_bin(y.as_slice()))
}

pub fn read_file(filename: &str) -> Vec<(String, String)> {
  let path = Path::new(filename);
  let mut file = BufferedReader::new(File::open(&path));
  let lines: Vec<String> = file.lines().map(|x|
    x.unwrap()).collect();

  let mut bitmap_point: Vec<(String,String)> = vec![];

  //loop through each word in each line
  for line in lines.iter() {
      for com in line.as_slice().words() {
        bitmap_point.push(
          (String::from_str(com.slice(0,1)),
          String::from_str(com.slice(1,2)))
        );
      }
  }

  return bitmap_point;

}

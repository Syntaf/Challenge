/*
  this program is a build off of the previous bitmap_ascii challenge. but to the next
  level. We can read in an 8x8 picture from hex values. Once we have that image we can
  start manipulating it

  Zoom - zoom in or out of the image
  Rotate - turn the image 90 degrees clockwise or counter clockwise
  Invert - What was On is Off and what is Off becomes On. It inverts the image

  reference: http://www.reddit.com/r/dailyprogrammer/comments/2avd5i/7162014_challenge_171_intermediate_zoom_rotate/
*/

use std::num;

mod loadHex;

//bitmap image struct
struct bitmap_image {
  bitmap_picture: Vec<String>,
  invert: bool,
  zoom: uint
}

impl bitmap_image {
  fn load_bitmap(&mut self, file: &str) {
    self.bitmap_picture = loadHex::read_file(file);
  }

  fn invert_hexmap(&mut self) {
    self.invert = !self.invert;
  }
}

//zoom hex picture, used in the print_bitmap function when the user
//  specifies a zoom
fn zoom_ascii_hex_string(bmp: &mut bitmap_image, zoom_dg: uint) {
  bmp.zoom = zoom_dg;
  for line in bmp.bitmap_picture.mut_iter() {
    let mut dec_num = 0;
    let mut incr = 0;
    for ch in line.as_slice().chars().rev() {
      dec_num += loadHex::hex_to_dec(ch) * num::pow(16u,incr);
      incr += 1;
    }
    *line = loadHex::dec_to_hex_str(dec_num);
  }
}

//rotate hex picture, this is used in the print_bitmap function when the
//  user specifies a rotate.
fn rotate_hex(bmp: &mut bitmap_image) {

}

//invert hex picture, this is used in the print_bitmap function
//  to save space and break apart one large code base.
fn invert_ascii_hex_string(line: &mut [std::ascii::Ascii]) {
  for c in line.mut_iter() {
    *c = match c.to_char() {
      'x' => ' ',
       _  => 'x'
    }.to_ascii();
  }
}

//print out bitmap, our struct only stores the commands, so this function
//  will do most of the work. It will convert each command into a binary
//  string, then parse any invert/zoom/rotate functions on the string before
//  displaying it.
fn print_bitmap(bmp: &bitmap_image) {
  //print hex tuple
  for command in bmp.bitmap_picture.iter() {
    let mut res = loadHex::convert_to_binary_string( command ).into_ascii();

    //if picture is inverted, invert now
    if bmp.invert {
        invert_ascii_hex_string(res.as_mut_slice());
    }

    println!("{}", res.as_slice().as_str_ascii());
  }
}

fn main() {
  let mut hex_bitmap =
    bitmap_image { bitmap_picture: vec![], invert: false, zoom: 1 };

  hex_bitmap.load_bitmap("input.dat");

  //hex_bitmap.invert_hexmap();
  zoom_ascii_hex_string(&mut hex_bitmap, 2);

  print_bitmap(&hex_bitmap);
}

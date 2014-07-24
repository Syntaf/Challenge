/*
  this program is a build off of the previous bitmap_ascii challenge. but to the next
  level. We can read in an 8x8 picture from hex values. Once we have that image we can
  start manipulating it

  Zoom - zoom in or out of the image
  Rotate - turn the image 90 degrees clockwise or counter clockwise
  Invert - What was On is Off and what is Off becomes On. It inverts the image

  reference: http://www.reddit.com/r/dailyprogrammer/comments/2avd5i/7162014_challenge_171_intermediate_zoom_rotate/
*/

mod loadHex;

//bitmap image struct
struct bitmap_image {
  bitmap_picture: Vec<(String,String)>,
  invert: bool,
  zoom: int
}

impl bitmap_image {
  fn load_bitmap(&mut self, file: &str) {
    self.bitmap_picture = loadHex::read_file(file);
  }

  fn invert_hexmap(&mut self) {
    self.invert = !self.invert;
  }

  fn zoom_hexmap(&mut self, zoom_val: int) {
    self.zoom = zoom_val;
  }
}

//zoom hex picture, used in the print_bitmap function when the user
//  specifies a zoom
fn zoom_ascii_hex_string(bmp: &mut bitmap_image) {
  for &(ref mut x, ref mut y) in bmp.bitmap_picture.mut_iter() {
    let dec_num = (loadHex::hex_to_dec(x.clone()) * 16 +
      loadHex::hex_to_dec(y.clone())) * 2;
    println!("{}", dec_num);
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

  zoom_ascii_hex_string(&mut hex_bitmap);

  //print_bitmap(&hex_bitmap);
}

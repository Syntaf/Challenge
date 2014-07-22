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

struct bitmap_image {
  bitmap_picture: Vec<(String,String)>,
  invert: bool
}

impl bitmap_image {
  fn load_bitmap(&mut self, file: &str) {
    self.bitmap_picture = loadHex::read_file(file);
  }
}

//zoom hex picture
fn zoom_hex(bmp: &mut bitmap_image) {

}

//rotate hex picture
fn rotate_hex(bmp: &mut bitmap_image) {

}

//invert hex picture
fn invert_hex(bmp: &mut bitmap_image) {
  bmp.invert = !bmp.invert;
}

fn print_bitmap(bmp: bitmap_image) {
  //print hex tuple
  for command in bmp.bitmap_picture.iter() {
    let mut res = loadHex::convert_to_binary_string( command ).into_ascii();

    //if picture is inverted, invert now
    if bmp.invert {

      for c in res.mut_iter() {
        *c = match c.to_char() {
          'x' => ' ',
           _  => 'x'
        }.to_ascii();
      }

    }

    println!("{}", res.as_slice().as_str_ascii());
  }
}

fn main() {
  let mut hex_bitmap = bitmap_image { bitmap_picture: vec![], invert: false };

  hex_bitmap.load_bitmap("input.dat");

  invert_hex(&mut hex_bitmap);

  print_bitmap(hex_bitmap);
}

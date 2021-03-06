/*
  this program is a build off of the previous bitmap_ascii challenge. but to the next
  level. We can read in an 8x8 picture from hex values. Once we have that image we can
  start manipulating it

  Zoom - zoom in or out of the image
  Rotate - turn the image 90 degrees clockwise or counter clockwise
  Invert - What was On is Off and what is Off becomes On. It inverts the image

  reference: http://www.reddit.com/r/dailyprogrammer/comments/2avd5i/7162014_challenge_171_intermediate_zoom_rotate/
*/

use std::io;

mod loadHex;
mod manipHex;

//bitmap image struct
struct BitmapImage {
  bitmap_picture: Vec<String>,
  invert: bool,
  zoom: uint
}

impl BitmapImage {
  fn load_bitmap(&mut self, file: &str) {
    self.bitmap_picture = loadHex::read_file(file);
  }

  fn invert_hexmap(&mut self) {
    self.invert = !self.invert;
  }

  fn zoom_hexmap(&mut self, zoom_dg: uint) {
    self.zoom = zoom_dg;
  }
}

//print out bitmap, our struct only stores the commands, so this function
//  will do most of the work. It will convert each command into a binary
//  string, then parse any invert/zoom/rotate functions on the string before
//  displaying it.
fn print_bitmap(bmp: &BitmapImage) {
  //print hex tuple
  for command in bmp.bitmap_picture.iter() {
    let mut res = loadHex::convert_to_binary_string( command ).into_ascii();

    //if picture is inverted, invert now
    if bmp.invert {
      manipHex::invert_ascii_hex_string(res.as_mut_slice());
    }

    //if zoom is not normal
    if bmp.zoom != 1 {
      manipHex::zoom_ascii_hex_string(res.as_mut_slice(), bmp.zoom);
    } else {
      println!("{}", res.as_slice().as_str_ascii());
    }
  }
}

fn main() {

  let mut hex_bitmap =
    BitmapImage {
      bitmap_picture: vec![],
      invert: false,
      zoom: 1
    };


  //load from file
  hex_bitmap.load_bitmap("input.dat");

  loop {
    print!("[1] - print map\n[2] - invert map\n[3] - zoom x\n[4] - exit\ninput: ");

    // read line from user to execute commands
    let input_num: int = match from_str(
      match io::stdin().read_line() {
        Ok(txt) => txt,
        Err(e)  => { println!("{}", e.detail.unwrap()); String::from_str("error")}
      }.as_slice().trim()) {
        Some(i) => i,
        None    => -1
      };

    match input_num {
      1 =>  print_bitmap(&hex_bitmap),
      2 =>  {hex_bitmap.invert_hexmap(); print_bitmap(&hex_bitmap);},
      3 =>  {
              print!("Zoom by(integer): ");
              let zoom_val: uint =
                from_str(io::stdin().read_line().unwrap().as_slice().trim()).unwrap();
              hex_bitmap.zoom_hexmap(zoom_val);
              print_bitmap(&hex_bitmap);
            },
      4 =>  break,
      _ => println!("Invalid choice ... re-enter ")
    };
  }
}

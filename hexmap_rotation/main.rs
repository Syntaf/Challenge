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

//zoom hex picture
fn zoom_hex(tup: &(String, String)) {

}

//rotate hex picture
fn rotate_hex(tup: &(String, String)) {

}

//invert hex picture
fn invert_hex(tup: &(String, String)) {

}

fn main() {
  let bitmap_picture = loadHex::read_file("input.dat");


  //print hex tuple
  for command in bitmap_picture.iter() {
    let res = loadHex::convert_to_binary_string( command );
    println!("{}", res);
  }

}

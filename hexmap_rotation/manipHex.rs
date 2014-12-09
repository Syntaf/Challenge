use std;
//zoom hex picture, used in the print_bitmap function when the user
//  specifies a zoom
pub fn zoom_ascii_hex_string(line: &mut [std::ascii::Ascii], zoom_dg: uint) {
    let mut rr = String::from_str("");
    //copy every character in place ZOOM_DG times
    for ch in line.as_mut_slice().as_str_ascii().chars(){
      for i in range(0u,zoom_dg) {
        rr.push_str(ch.to_string().as_slice());
      }
    }
    for i in range(0u,zoom_dg) {
      println!("{}", rr);
    }
}

//invert hex picture, this is used in the print_bitmap function
//  to save space and break apart one large code base.
pub fn invert_ascii_hex_string(line: &mut [std::ascii::Ascii]) {
  for c in line.iter() {
    *c = match c.to_char() {
      'x' => ' ',
       _  => 'x'
    }.to_ascii();
  }
}

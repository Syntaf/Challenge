/*
 *  main.rs
 *  Grant Mercer
 *  compute the sad cycle given an input range and a sad 
 *  cycle base
*/

extern crate getopts;

use getopts::Options;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    let program = &args[0];
    

    let mut options = Options::new();
    options.optopt("b", "base", "set the base for sad cycle", "VALUE");
    options.reqopt("n", "num" , "set the value to compute sad cycle for",
                   "VALUE");
    
    if args.len() == 1 {
        let brief = format!("Usage: {} [options]", program);
        print!("{}", options.usage(&brief));
        return;
    }
    
    let matches = match options.parse(&args[1..]) {
        Ok(m) => { m },
        Err(f) => { panic!(f.to_string()) }
    };


    let base: u32 = 
        if matches.opt_present("b") {
            match matches.opt_str("b").unwrap().parse::<u32>() {
                Ok(y) => { y },
                Err(h) => { panic!(h.to_string()) }
            }
        } else {
            2u32
        };

    println!("{}", base);
    println!("{}", program)  

}

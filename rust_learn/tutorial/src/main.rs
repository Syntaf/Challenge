fn main() {
    let num = 5;
    let owns_num = move |x: i32| x + num;
    println!("{}", owns_num(5));
    println!("{}", num);
}


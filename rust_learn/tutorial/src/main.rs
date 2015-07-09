fn get_names(v: Vec<(String, usize)>) -> Vec<String> {
    v.iter().cloned()
        .map(|(name, _value)| name)
        .collect()
}

fn main() {
    let v = vec!(("Herman".to_string(), 5));
    println!("running");
    let names = get_names(v);

    assert_eq!(names, ["Herman"]);
    println!("{:?}", v);
}

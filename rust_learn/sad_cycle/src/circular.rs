pub mod circular {
    pub struct Vector<T> {
        raw: Vec<T>,
        val: T
    }

    impl<T> Vector<T> {
        pub fn new(t_raw: Vec<T>, t_val: T) -> Vector<T> {
            println!("Creating new");
            return Vector { raw: t_raw, val: t_val };
        }
    }
}

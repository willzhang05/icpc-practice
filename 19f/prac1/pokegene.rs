use std::io::{self, BufRead};


/*fn insert(char: value, genome: &Vec<char>) {
    let k = 1;
    while (genome[k] != '*') {
        
    }

}*/

fn main() {
    let stdin = io::stdin();
    let mut stdin_it = stdin.lock().lines();
    let nq = stdin_it.next().unwrap().unwrap();
    let nq_split = nq.split(" ").collect::<Vec<&str>>();
    let n = nq_split[0].parse::<usize>().expect("not an int");
    let q = nq_split[1].parse::<usize>().expect("not an int");
    println!("n: {}, q: {}", n, q);
    //let genome: Vec<char> = vec!['*', n**2];
    let mut genome: Vec<String> = vec![];
    for i in 0..n {
        genome.push(stdin_it.next().unwrap().unwrap());
    }

    for i in 0..q {
        let kl = stdin_it.next().unwrap().unwrap();
        let kl_split = kl.split(" ").collect::<Vec<&str>>();
        let k = kl_split[0].parse::<usize>().expect("not an int");
        let l = kl_split[1].parse::<usize>().expect("not an int");

        let pk = stdin_it.next().unwrap().unwrap();
        let pk_split = pk.split(" ").collect::<Vec<&str>>();
        let mut pk_owned: Vec<String> = vec![];
        for p in pk_split {
            let x = p.parse::<usize>().expect("not an int");
            pk_owned.push(genome[x].clone());
        }
        
    }
    /*
    for i in 0..n {
        println!("{}", genome[i]);
    }
    */

}

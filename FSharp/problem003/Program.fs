// 600851475143

let primes n =
    match n with
    | [] -> []
    | first :: tail -> first ::Lazy.CreateFromValue(tail).Value |> List.filter (fun p -> p%first <> 0L)

let rec sieve = function 
    | (p::xs) -> p :: sieve [ for x in xs do if x % p > 0L then yield x ] 
    | []      -> [] 



[<EntryPoint>]
let main args = 
   [2L..900000L] |> sieve |> List.iter( fun p -> System.Console.WriteLine(p) )
   System.Console.ReadLine();
   0
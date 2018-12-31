// Learn more about F# at http://fsharp.net

//let fibonacci = Seq.unfold 

let seq1 = Seq.unfold (fun g -> Some(g, g + 1)) 0

let lst = seq1 |> Seq.take 40

let fib = Seq.unfold (fun state -> Some(fst state + snd state, (snd state, (fst state + snd state)))) (1I,1I)

let result value = 
    fib 
    |> Seq.filter (fun i -> i % 2I = 0I )
    |> Seq.takeWhile (fun i -> i < value)
    |> Seq.sum

let result2 value = 
    fib 
    |> Seq.takeWhile (fun i -> i < value)
    |> Seq.filter (fun i -> i%2I = 0I)
    |> Seq.sum

let rec pow a b = if b = 0I then 1I else a * pow a (b-1I)

let heelveel = pow 99999999999I 1200I
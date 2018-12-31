// Learn more about F# at http://fsharp.net

let divisors n =
    [1..n-1] |> List.filter(fun x -> n%x=0)

let divisorsList n =
    [1..n] |> List.map( fun x -> (x, divisors(x)) )

let divisorsListSum n =
    n |> divisorsList |> List.map( fun (x,y) -> (x, y |> List.sum))

let friends n =
    n |> divisorsListSum |> List.filter(fun (x,y) -> y=x)

// Learn more about F# at http://fsharp.net


let result (max ) = 
    [1I..max] 
    |> List.filter(fun n -> n%3I=0I || n%5I=0I) 
    |> List.sum


 
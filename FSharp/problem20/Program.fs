// Learn more about F# at http://fsharp.net

let rec Factorial n =
    if n = 0I then
        1I
    else
        n * Factorial(n-1I)

let rec digitSum n =
    if n < 10I then
        n
    else
        n % 10I + digitSum(n / 10I)


let Fact100 = Factorial 100I
let DigitSumFact100 = digitSum Fact100

let WaaromWel = 
    let fact = Factorial 100I
    let sum = digitSum fact
    sum

open System

[<EntryPoint>]
let main args =
    let fact = Factorial 100I
    let sum = digitSum fact
    System.Console.WriteLine sum
    0
main =  do
    let numbers = [3,6..999] ++ [5,10..999]
    let a = unique numbers

    print (sum a)

unique (x : []) = [x]
unique (x : xs) 
    | find x xs = unique xs
    | otherwise = x : unique xs

find n [] = False
find n (x : xs)
   | n == x    = True
   | otherwise = find n xs
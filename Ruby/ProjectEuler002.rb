# ProjectEuler Problem 2
# http://projecteuler.net/problem=2
# jorgvisch.nl
# 20120807

# first two elements
fib_range = [1] 

new = 2 # should be 1, but the problem defines fibonacci as [1,2]
# make range
begin
	fib_range.push( new )
	new = fib_range.last(2).reduce(:+)
end until new >= 4000000

result = fib_range.find_all { |i| i%2==0 } .reduce(:+)

puts "Euler problem 2 result is: #{result}"

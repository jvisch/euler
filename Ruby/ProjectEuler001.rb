# ProjectEuler Problem 1
# http://projecteuler.net/problem=1
# jorgvisch.nl
# 20120807

result = (1..999).find_all { |i| i%3==0 or i%5==0 } .reduce(:+)

puts "Euler problem 1 result is: #{result}"

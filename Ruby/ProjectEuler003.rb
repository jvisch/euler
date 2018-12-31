# ProjectEuler Problem 3
# http://projecteuler.net/problem=3
# jorgvisch.nl
# 20120808

class Primes
	attr_reader :values
	
	def initialize
		
	end
	
	def next
		if @values.nil? then
			@values = [2]
			2
		else
			valueToCheck = @values.last + 1
			until @values.find { |i| valueToCheck%i==0 }.nil?
				valueToCheck = valueToCheck.next
			end
			@values << valueToCheck
			valueToCheck
		end
	end
	
	#very slow
	def primeFactors1 value
		maxValue = value/2 +1
		if @values.nil? then
			self.next
		end
		while @values.last <= maxValue
			self.next
		end
		@values.find_all { |i| value % i == 0 }
	end	
	
	#very fast
	def primeFactors2 value
		retval = []
		if not @values.nil? then
			@values.each do |i|
				if value == 1 then
					break
				end
				if(value%i==0) then
					retval << i
					while value%i==0
						value = value / i
					end
				end
			end
		end
		if value>1 then
			while value > 1 
				i = self.next
				if value%i==0 then
					retval<<i
					while value%i==0
						value = value / i
					end
				end
			end
		end
		
		retval
	end
end

#result  = Primes.new.primeFactors2(600851475143).max

#puts "Euler problem 3 result is: #{result}"

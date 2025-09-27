# https://en.wikipedia.org/wiki/Heap's_algorithm
# procedure generate(n : integer, A : array of any):
# if n = 1 then
# output(A)
# else
# for i := 0; i < n - 1; i += 1 do
# generate(n - 1, A)
# if n is even then
# swap(A[i], A[n-1])
# else
# swap(A[0], A[n-1])
# end if
# end for
# generate(n - 1, A)
# end if

aantalDigits = 10

print("start")
result = []


def generate(n, a):
    if n == 1:
        result.append(a.copy())
    else:
        for i in range(n-1):
            generate(n-1, a)
            if n % 2 == 0:
                a[i], a[n-1] = a[n-1], a[i]  # swap
            else:
                a[0], a[n-1] = a[n-1], a[0]  # swap
        generate(n - 1, a)


digits = [i for i in range(aantalDigits)]

print("start generate")
generate(aantalDigits, digits)

print("start sorting")
result.sort()

print("done")

value = result[pow(10, 6)-1]

theResult = ""
for v in value:
    theResult += str(v)

print(theResult)

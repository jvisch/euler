def all_sides(total):
    for a in range(1, total):
        for b in range(a, total - a):
            c = total - a - b
            if a**2 + b**2 == c**2:
                yield a, b, c

def result(max):
    s = ((total, list(all_sides(total))) for total in range(1,max))
    s = ((total, sides) for total, sides in s if len(sides))
    return s

if __name__ == '__main__':
    results =  list(result(1000))
    max_length = max( (len(s) for _, s in results) )

    final_results = ( (total, r) for total, r in results if len(r) == max_length )

    for r in final_results:
        print(r)
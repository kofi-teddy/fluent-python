# Iteration
# Uisng next() and iter

r = range(1, 10, 2)

it=iter(r)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

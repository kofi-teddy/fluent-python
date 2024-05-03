def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    max_divisor = int(n ** 0.5) + 1
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True
    

def count_special_triplets(arr):
    """
    given the array of A of n integers in the range of [3, 1000]. 
    you need to find the number of special triplets . a triplet(i, j, k) 
    is called special based on the following conditions are not
    1.  0 < = i < j <  k n
    2. A[ i ] < A[ j ] < A[k]
    3. A[ i ] and A[ k ] are prime numbers but A[ j ] is not prime number. 

    Assume that all numbers are in the range of [2, 10exponent 6] and 
    the array has no repeated numbers 
    """

    count = 0
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] < arr[j] < arr[k]:
                    if is_prime(arr[i] and not is_prime(arr[j]) and is_prime(arr[k])):
                        count += 1

    return count
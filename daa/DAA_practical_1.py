def recFibonacci(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return recFibonacci(n-1) + recFibonacci(n-2)

def iterFibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        res = 0
        first = 1
        second = 1
        for i in range(n-2):    
            res = first+second
            second = res
            first = res-first
    return res
        
print(iterFibonacci(9)) # O(n)
print(recFibonacci(9))  # O(2^n)



def counting_sort(A, k = None):
	n = len(A)

	if k is None: k = max(A) + 1
	else: k = k + 1

	B = [0] * len(A)
	C = [0] * (k)

	for j in range(n):
		C[A[j]] += 1

	for i in range(1, k):
		C[i] += C[i - 1]

	for j in reversed(range(n)):
		B[C[A[j]] - 1] = A[j]
		C[A[j]] -= 1 
	return B



A = [6, 4, 3, 9, 1, 2, 2, 5]
B = counting_sort(A)
print (B)
"""
Given a list of N coins, their values (V1, V2, … , VN), and the total sum S. Find the minimum 
number of coins the sum of which is S (we can use as many coins of one type as we want), or 
report that it’s not possible to select coins in such a way that they sum up to S.
"""

MAX = float('inf')

def coin_change(S, values):
	values.sort()
	n = len(values)
	table = [MAX] * (S + 1)
	table[0] = 0

	for i in range(1, S + 1):
		for j in range(n):			
			if values[j] <= i and table[i - values[j]] < table[i]:
				table[i] = table[i - values[j]] + 1

	return table[S]


sol = coin_change(11, [1, 5, 10, 25])
print (sol)
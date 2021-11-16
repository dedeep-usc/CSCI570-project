import efficient as eff

import inefficient as in_eff


P = []

# print(eff.find_min_cost("ACGT", "TGCA"))
# print(in_eff.find_min_cost("ACGT", "TGCA"))

def div_conq_alignment(X, Y):
	# print("----------------------c
	m = len(X)
	n = len(Y)

	if m <= 2 or n <= 2:
		return in_eff.find_min_cost(X, Y)

	first_half_dp = eff.find_min_cost(X, Y[:n//2])

	second_half_dp = eff.find_min_cost(X[::-1], Y[n//2:][::-1])

	# print("first")

	# for i in first_half_dp:
	# 	print(i)

	# print("second")

	# for j in second_half_dp:
	# 	print(j)

	q = 0
	for i in range(1, m+1):
		actual_min_cost = first_half_dp[q][0] + second_half_dp[m-q][0]
		cur_cost = first_half_dp[i][0] + second_half_dp[m-i][0]

		if cur_cost <= actual_min_cost:
			q = i

	# print("q: {}".format(q))

	return div_conq_alignment(X[:q], Y[:n//2]) + div_conq_alignment(X[q:], Y[n//2:]) 
 

# print(div_conq_alignment("AGGCGCTATATAT", "TCGCGAGAGAGACTC"))


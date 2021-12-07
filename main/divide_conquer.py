class DivideConquerSeqAlignment():
	def __init__(self, eff, ineff):
		self.eff = eff
		self.ineff = ineff
	def div_conq_alignment(self, X, Y):
		m = len(X)
		n = len(Y)

		if m < 2 or n < 2:
			return self.ineff.find_min_cost(X, Y)

		first_half_dp = self.eff.find_min_cost(X, Y[:n//2])

		second_half_dp = self.eff.find_min_cost(X[::-1], Y[n//2:][::-1])

		q = 0
		for i in range(0, m+1):
			actual_min_cost = first_half_dp[q][0] + second_half_dp[m-q][0]
			cur_cost = first_half_dp[i][0] + second_half_dp[m-i][0]

			if cur_cost < actual_min_cost:
				q = i

		partition = []
		first_half_dp = []
		second_half_dp = []
		left = self.div_conq_alignment(X[:q], Y[:n//2])
		right = self.div_conq_alignment(X[q:], Y[n//2:])
		return [left[r] + right[r] for r in range(3)]

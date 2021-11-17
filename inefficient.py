alpha_index_mapper = {
	"A": 0,
	"C": 1,
	"G": 2,
	"T": 3
}

alpha_list = [
	[0, 110, 48, 94],
	[110, 0, 118, 48],
	[48, 118, 0, 110],
	[94, 48, 110, 0]
]


class InefficientSeqAlignment():
	def __init__(self, delta_val=30, alpha_list=alpha_list, alpha_index_mapper=alpha_index_mapper):
		self.delta_val = delta_val
		self.alpha_list = alpha_list
		self.alpha_index_mapper = alpha_index_mapper

	def find_min_cost(self, str1, str2):

		dp = [[float("inf") for i in range(len(str2)+1)] for j in range(len(str1)+1)]
		m = len(dp)
		n = len(dp[0])
		
		# Base cases
		for i in range(n):
			dp[0][i] = i * self.delta_val

		for i in range(m):
			dp[i][0] = i * self.delta_val

		for i in range(1, m):
			for j in range(1, n):
				dp[i][j] = min(
						dp[i-1][j-1] + self.alpha_list[self.alpha_index_mapper[str1[i-1]]][self.alpha_index_mapper[str2[j-1]]],
						dp[i-1][j] + self.delta_val,
						dp[i][j-1] + self.delta_val
					)

		# for i in dp:
		# 	print(i)

		seqs = self.form_strings(dp, str1, str2)
		return seqs[0], seqs[1], dp[m-1][n-1]

	def form_strings(self, dp, str1, str2):
		m = len(dp)-1
		n = len(dp[0])-1

		i = m
		j = n

		new_str1 = ""
		new_str2 = ""

		while j > 0 and i > 0:
			cur_val = dp[i][j]
			# if dp[i-1][j-1] + alphas[str1[i-1]][str2[j-1]] == cur_val:
			if dp[i-1][j-1] + self.alpha_list[self.alpha_index_mapper[str1[i-1]]][self.alpha_index_mapper[str2[j-1]]] == cur_val:
				new_str1 += str1[i-1]
				new_str2 += str2[j-1]
				i -= 1
				j -= 1

			elif dp[i-1][j] + self.delta_val == cur_val:
				new_str1 += str1[i-1]
				new_str2 += "_"
				i -= 1

			elif dp[i][j-1] + self.delta_val == cur_val:
				new_str1 += "_"
				new_str2 += str2[j-1]
				j -= 1

		while j > 0:
			new_str1 += "_"
			new_str2 += str2[j-1]
			j -= 1

		while i > 0:
			new_str1 += str1[i-1]
			new_str2 += "_"
			i -= 1

		return new_str1[::-1], new_str2[::-1]
		return new_str1[::-1]
		return new_str2[::-1]


alpha_list = [
	[0, 110, 48, 94],
	[110, 0, 118, 48],
	[48, 118, 0, 110],
	[94, 48, 110, 0]
]

alpha_index_mapper = {
	"A": 0,
	"C": 1,
	"G": 2,
	"T": 3
}

class EfficientSeqAlignment():
	def __init__(self, delta_val=30, alpha_list=alpha_list, alpha_index_mapper=alpha_index_mapper):
		self.delta_val = delta_val
		self.alpha_list = alpha_list
		self.alpha_index_mapper = alpha_index_mapper

	def find_min_cost(self, str1, str2, return_cost=False):
		dp = [[float("inf") for i in range(2)] for j in range(len(str1)+1)]

		m = len(dp)
		n = len(dp[0])

		# Base case
		for i in range(m):
			dp[i][0] = i * self.delta_val


		for j in range(1, len(str2)+1):
			dp[0][1] = j * self.delta_val
			for i in range(1, len(str1)+1):
				dp[i][1] = min(
						dp[i-1][0] + self.alpha_list[self.alpha_index_mapper[str1[i-1]]][self.alpha_index_mapper[str2[j-1]]],
						dp[i-1][1] + self.delta_val,
						dp[i][0] + self.delta_val
					)

			dp = self.move_col(dp)
		return dp if not return_cost else dp[-1][0]


	def move_col(self, dp):
		for i in range(len(dp)):
			dp[i][0], dp[i][1] = dp[i][1], 0

		return dp







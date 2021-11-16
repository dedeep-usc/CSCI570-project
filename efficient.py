delta_val = 30
alphas = {
	"A": {
		"A": 0,
		"C": 110,
		"G": 48,
		"T": 94 
	},

	"C": {
		"A": 110,
		"C": 0,
		"G": 118,
		"T": 48 
	},

	"G": {
		"A": 48,
		"C": 118,
		"G": 0,
		"T": 110 
	},

	"T": {
		"A": 94,
		"C": 48,
		"G": 110,
		"T": 0 
	}
}

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

def find_min_cost(str1, str2):
	dp = [[float("inf") for i in range(len(str2)+1)] for j in range(len(str1)+1)]
	
	dp = [[float("inf") for i in range(2)] for j in range(len(str1)+1)]

	m = len(dp)
	n = len(dp[0])
	
	# Base cases
	# for i in range(n):
	# 	dp[0][i] = i * delta_val

	for i in range(m):
		dp[i][0] = i * delta_val

	for j in range(1, len(str2)+1):
		dp[0][1] = j * delta_val
		for i in range(1, len(str1)+1):
			dp[i][1] = min(
					dp[i-1][0] + alpha_list[alpha_index_mapper[str1[i-1]]][alpha_index_mapper[str2[j-1]]],
					dp[i-1][1] + delta_val,
					dp[i][0] + delta_val
				)

		dp = move_col(dp)


	# return dp[-1][0]
	# print(dp[-1][0])
	return dp

def move_col(dp):
	for i in range(len(dp)):
		dp[i][0], dp[i][1] = dp[i][1], 0

	return dp





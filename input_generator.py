import argparse
import csv  

parser = argparse.ArgumentParser() 
parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()


def input_generator(filename):
	strs = []
	str_count = 0

	str_indices = {'0':[], '1':[]}

	with open(filename) as inputfile:
		reader = csv.reader(inputfile, delimiter='\n')
		for row in reader:
			if not str.isdigit(row[0]):
				strs.append(row[0])
				index = str(str_count)
				str_count+=1
			else:
				str_indices[index].append(int(row[0]))
				

	def str_validate(original_string, generated_string, i):

		return len(generated_string) == pow(2, i)*len(original_string) 

	def generate(s, indices):
		prev_str = s
		for i in indices:
			
			new_str = prev_str[:i+1] + prev_str + prev_str[i+1:]
			prev_str = new_str
		return prev_str

	str1 = generate(strs[0], str_indices['0'])
	str2 = generate(strs[1], str_indices['1'])

	if str_validate(strs[1], str1, len(str_indices['1'])) and str_validate(strs[0], str1, len(str_indices['0'])):
		return (str1, str2)
		

print(input_generator(args.file))


		
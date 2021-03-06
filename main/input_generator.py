def input_generator(filename):
	strs = []
	str_count = 0

	str_indices = {'0':[], '1':[]}

	with open(filename) as inputfile:
		contents = inputfile.readlines()
		
		for line in contents:
			stripped_line = line.strip()
			
			if stripped_line.isdigit():
				str_indices[index].append(int(stripped_line))
				
			else:
				if stripped_line != '':
					strs.append(stripped_line)
					index = str(str_count)
					str_count+=1
			
				

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

	if str_validate(strs[1], str2, len(str_indices['1'])) and str_validate(strs[0], str1, len(str_indices['0'])):
		return (str1, str2)
	else:
		raise Exception('Strings are not of length 2^i*Str.length')
		




		
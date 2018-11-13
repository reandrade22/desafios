import textwrap
import itertools
import argparse

def split_and_justify_text(text, max_chars):
	'''
	This functions splits the text into lines and justifies it

	Args
		param 1 (string) - Text to split and justify
		param 2 (int) - Maximum number of characters per line

	Returns
		list: List where each element is a line in the output file
	'''

	paragraphs = text.split("\n")
	
	split_paragraphs = []
	for p in paragraphs:
		split_paragraphs.append(textwrap.wrap(p, width=max_chars, replace_whitespace=False))

	
	for lines in split_paragraphs:  
		if lines:
			for position, l in enumerate(lines):
				valid_chars = len(l) - l.count(' ')
				chars_left = max_chars - valid_chars
				num_words = len(l.split())
						
				if num_words > 1:
					full_spaces, leftover_spaces = divmod(chars_left, num_words-1)
				else:
					continue
						
				spaces = []
				leftover_filled = 0
				for x in range(0, num_words-1):
						
					if leftover_filled < leftover_spaces:
						spaces.append(" " * full_spaces + " ")
						leftover_filled += 1
					else:
						spaces.append(" " * full_spaces)
						   
				lines[position] = ''. join([a + b for a, b in itertools.zip_longest(l.split(), 
																					spaces, fillvalue='')])

	return split_paragraphs


if __name__ == "__main__":

	######################################### Required Arguments #################################### 
	################################################################################################# 
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--chars", help="Numero maximo de caracteres por linha", type=str, required=True)
	parser.add_argument("-i", "--input", help="Path para arquivo de input", type=str, required=True)
	parser.add_argument("-o", "--output", help="Arquivo de output", type=str, required=True)
	parser.add_argument("-j", "--justify", help="Define se o texto deve estar justificado", type=str)
	args = parser.parse_args()
	#################################################################################################

	#Try to open input file
	try:

		input_path = args.input
		with open(input_path, "r") as input_file:
			input_text = input_file.read()

	except:
		print("Error ao abrir arquivo de input!")
		raise

	word_list = input_text.split()
	longest_word = max([len(word) for word in word_list])
	max_chars = int(args.chars)

	#Verify if longest word is smaller than maximun chars per line
	if longest_word<max_chars:

		#Create split and justified text
		justified_text = split_and_justify_text(input_text, max_chars)
		ouput_path = args.output

		#Try to write text to file
		try:
			with open(ouput_path, "w") as f:
				for lines in justified_text:  
					if lines:
						for l in lines:
							f.write(l)
							f.write("\n")
					else:
						f.write("\n")
		except:
			print("Erro ao salvar arquivo de output!")
			raise

	else:
		print("Minimo de caracters necessarios por linha, para este texto: %s!" % str(longest_word))
	





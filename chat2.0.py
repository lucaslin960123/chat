def read_file(filename):
	lines = []
	with open(filename,'r') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0

	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == 'Sticker':
				allen_sticker_count += 1
			elif s[2] == 'Image':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)


		elif name == 'Viki':
			if s[2] == 'Sticker':
				viki_sticker_count += 1
			elif s[2] == 'Image':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)

	print('Allen said',allen_word_count,'words','and sent',allen_sticker_count,'stickers and',allen_image_count,'pictures')
	print('Viki said', viki_word_count,'words','and sent',viki_sticker_count,'stickers and',viki_image_count,'pictures')
	


def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('line.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main()

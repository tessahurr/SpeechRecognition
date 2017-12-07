import re
import os
import num2words
import string
import codecs

"""Given an int32 number, print it in English."""
def int_to_en(num):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= num)

    if (num < 20):
        return d[num]

    if (num < 100):
        if num % 10 == 0: return d[num]
        else: return d[num // 10 * 10] + ' ' + d[num % 10]

    if (num < k):
        if num % 100 == 0: return d[num // 100] + ' hundred'
        else: return d[num // 100] + ' hundred and ' + int_to_en(num % 100)

    if (num < m):
        if num % k == 0: return int_to_en(num // k) + ' thousand'
        else: return int_to_en(num // k) + ' thousand, ' + int_to_en(num % k)

    if (num < b):
        if (num % m) == 0: return int_to_en(num // m) + ' million'
        else: return int_to_en(num // m) + ' million, ' + int_to_en(num % m)

    if (num < t):
        if (num % b) == 0: return int_to_en(num // b) + ' billion'
        else: return int_to_en(num // b) + ' billion, ' + int_to_en(num % b)

    if (num % t == 0): return int_to_en(num // t) + ' trillion'
    else: return int_to_en(num // t) + ' trillion, ' + int_to_en(num % t)

    raise AssertionError('num is too large: %s' % str(num))

def preprocess(filename):

#removes single quotes
#os.system("awk -f preprocess.awk thisFile.txt > otherFile.txt")

	#opened in read and write mode
	#file_path = "./Gutenberg/txt/"+filename
	f_in = open ("./Gutenberg/txt3/"+filename, 'r+', encoding="ISO-8859-1")
	#f_in = open("thisFile.txt", 'r+')
	#opened in append mode
	f_out = open("thatFile.txt", 'a')

	for line in f_in:



		#print(line[0])
		#print(line[len(line)-1])

		# if line[0] in num_list:
		# #if isinstance(line, int) == True:
		# 	print(line[0])
		# 	if line[len(line)-1] in float_list:
		# 		line = line[0, -1]
		# 		#line = int_to_en(float(line))

		# 	line = int_to_en(int(line))
		# 	print(line)
		
		for char in line:
			#line = re.sub('[@#$:";,(\[)\]-_--]', ' ', line)
			# replace hyphens with spaces
			# kill apostrophe's unless the word before it is alpha numeric
			# if you have a period, find the next non space character, if it's a period kill it, otherwise continue
			# if you find any char that's not within ascii, then replace it with

			line = re.sub("[^a-zA-Z0-9.!?']", ' ', line)
			line = line.replace(" .", ".")
			line = line.replace(" ?", "?")
			line = line.replace(" !", "!")

			#line = re.sub(, ' ', line)
		#TODO: add in a num2word function
		f_out.write(line)

	f_in.close()
	f_out.close()

	f2_in = open("thatFile.txt", 'r+', encoding="ISO-8859-1")
	f2_out = open("numberConversion.txt", 'a')

	for line in f2_in:

		num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
		float_list = [".", ",", ":", ";", "'", ";", '"', "?"]
		ordinal_list = ["rd", "th", "nd", "st"]

		for word in line.split():
			#print(word[-2:])
			
			# if the number is only numeric, then it goes through and converts it
			# if it's an ordinal remove it for now
			# if float, 34.5 "thirty four point 5", or just remove what comes after the point at the end
			# if it doesn't match the previous contraints, then you throw it out

			if word[0] not in num_list:
				f2_out.write(word)
			elif word[0] in num_list and word[-1] in float_list:	
				word = int_to_en(int(word[0:-1]))
				print(word)
			elif word[0] in num_list and word[-2:] in ordinal_list:
				word = int_to_en(int(word[0:-2]))
				print(word)
			elif word[0] in num_list:
				int_to_en(int(word))
				print(word)

		f2_out.write(word)

# def preprocess(filename):
# 	#opened in read and write mode
# 	f_in = open (filename, 'r+')
# 	#opened in append mode
# 	f_out = open('new_'+filename, 'a')

# 	for line in f_in:
# 		for char in line:
# 			line = re.sub("[@#$:;,(\[)\]-_--']", ' ', line)
# 		#TODO: add in a num2word function
# 		f_out.write(line)

	# #creates a new directory within the directory in this path
	# newpath = "./gutenberg_clean"
	# os.makedirs(newpath)

	# #saves to a different directory
	# newpath = "./gutenberg_clean/new_"+filename
	# oldpath = "new_"+filename
	# os.rename(oldpath, newpath)

	# f_in.close()
	# f_out.close()

#takes in all the files in the directory


for f in os.listdir("./Gutenberg/txt3/"):
	#s_f = str(f)
	#print(s_f)
	print(f)
	#new_f = os.fsencode(f).decode("utf-8")
	preprocess(f)

#preprocess("thisFile.txt")
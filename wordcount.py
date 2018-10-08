# This code block is before the further study-collections.counter
# from sys import argv

# # put your code here.
# def word_count(filename):
# 	with open(filename) as file:
# 		word_count = {}

# 		for line in file:
# 			words = line.split(" ")

# 			for i in words:
# 				i = i.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c').lower()
# 				word_count[i] = word_count.get(i, 0) + 1

# 		for word in word_count:
# 			print(word, word_count[word])

# word_count(argv[1])

# This code block is for the further study-collections.counter
from sys import argv
from collections import Counter

# put your code here.
def word_count(filename):
	with open(filename) as file:
		words_lst = []

		for line in file:
			words = line.split(" ")
			words_lst.extend(words)

		clean_words_lst = []
		for i in words_lst:
			i = i.strip('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c').lower()
			clean_words_lst.append(i)

		word_counter = Counter(clean_words_lst)

		for word in word_counter:
			print(word, word_counter[word])

word_count(argv[1])
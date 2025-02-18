""" a= 951 
b= 942
c = a**2 + b**2
print(c)

 """

#Comentar con shit + alt + A

#STRING AND LISTS
#A string s of length at most 200 letters and four integers a, b, c and d


""" s = 'pto1pYvymGn6xgMXpUxKObNMUztH24XMDWdPgnQ6isdnN0EOkDR7fL9VBTWlokYnrDBPachydactylusMPlf2OGsbylQwnuXxzukiUup9JEmirabiliszElcJcwr7E4PyQvcAZWBgK34QNfGiXUlpNhSSyk8OyU'


a = 67
b = 79
c = 107 
d = 115

print((s[a:b + 1]) + ' ' + (s[c:d+1]))
 """

# CONDITIONS AND LOOPS
#Given: Two positive integers a and b (a<b<10000)
#Return: The sum of all odd integers from a through b, inclusively.

""" a = 4535
b = 9534
c = 10000

list = []
for i in range (a,b):
    if i % 2 != 0:
        list.append(i)
print(sum(list))
 """

# READING AND WRITTING
# Given a file containing at most 1000 lines, return a file containing
#all the even-numered lines from the original file. Assume
# 1- based numbering of lines
""" 
f = open('rosalind_ini5 (1).txt')
i = 1
for line in f.readlines():
    if i % 2 ==0:
        print(line)
    i +=1 """


# DICTIONARIES
#Given a string s of length at most 10000 leters, return the number of ocurrences of each word in s, where 
# words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

#We need to count the words of the given string, then create a dictionary with the frequencies of them.

#Create a variable with the string given

""" string = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

words_counted = {}

split_str = string.split(' ')

for word in split_str:
    if word in words_counted:
        words_counted[word] += 1
    else:
        words_counted [word] = 1

for word,frequency in words_counted.items():
    print(word,frequency) """
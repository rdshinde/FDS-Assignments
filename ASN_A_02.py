#1 Function to find the longest word in sentence.
   
def search(sentence):
    lst = sentence.split()
    index = 0
    long = 0
    while index< len(lst):
        lenth = len(lst[index])
        if lenth>long:
            long = lenth
        index+=1
    for word in lst:
        if len(word) == long:
            return word
#print(search('We are SE Computer students'))

'''def longest_world(sentence):
    longest = max(sentence.split(), key=len)
    return longest'''
#print(longest_world('I am Rishikesh Shinde'))


















#2 Function to find the frequency of occurance of perticalar character in string.

def freq_character(string,charct):
    lst1 = []
    for char in string:
        lst1.append(char)
    #return lst1
    dict = {}
    for char in lst1:
        if char in dict:
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
    
    return dict[charct]

#print(freq_character("JJJJLLGGTTTUUU",'G'))
'''def freq_character(string,charct):
    lst1 = []
    for char in string:
        lst1.append(char)
    #return lst1
    dict = {}
    for char in lst1:
        dict[char]=dict.get(char,0) + 1
    return dict[charct] '''   
#print(freq_character("aaabbc",'a'))










#3 Function to check whether the string is palindrome or not.

def check_palindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

#print(check_palindrome('advhdg'))











#4 Function to display index of first appearance of the substring.

def find_index(string,substring):
    index = string.find(substring)
    return index

#print(find_index('I am Rishikesh Shinde.','kesh'))















#5 Function to count the occurance of each word in the given string.

def occurance(string):
    lst = string.split()
    dict = {}
    for word in lst:
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    return dict 
#print(occurance(' Indian Cricket Team Team Cricket'))

'''def occurance(string):
    lst = string.split()
    dict = {}
    for word in lst:
        dict[word]=dict.get(word,0)+1
    return dict '''

#print(occurance('This is Rishikesh Shinde'))

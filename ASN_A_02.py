# Function to find the longest word in sentence.

def longest_world(sentence):
    longest = max(sentence.split(), key=len)
    return longest

#print(longest_world('I am Rishikesh Shinde'))   

# Function to find the frequency of occurance of perticalar character in string.

def freq_character(string,charct):
    lst1 = []
    for char in string:
        lst1.append(char)
    #return lst1
    dict = {}
    for char in lst1:
        dict[char]=dict.get(char,0)+1
    return dict[charct]
    

#print(freq_character("aaabbc",'a'))


# Function to check whether the string is palindrome or not.

def check_palindrome(string):
    if string[::-1] == string:
        return True

#print(check_palindrome('ababa'))

# Function to display index of first appearance of the substring.

def find_index(string,substring):
    index = string.find(substring)
    return index

#print(find_index('I am Rishikesh Shinde.','kesh'))

# Function to count the occurance of each word in the given string.

def occurance(string):
    lst = string.split()
    dict = {}
    for word in lst:
        dict[word]=dict.get(word,0)+1
    return dict 

#print(occurance('This is Rishikesh Shinde'))
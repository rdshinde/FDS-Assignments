# Function for calculating intersection of two sets.
def intersection(set1,set2):
    intersect=[]
    if len(set1)>=len(set2):
        for element in set1:
            if element in set2:
                intersect.append(element)
    else:
        for element in set2:
            if element in set1:
                intersect.append(element)
    return set(intersect)

#print(intersection([2,4],[1,2,5]))

# Function for calculating either in set1 on in set2 but not in both.
def either_of_two(set1,set2):
    either=[]        
    for element in set1:
        if element not in set2:
            either.append(element)
    for element in set2:
        if element not in set1:
            either.append(element)
    return set(either)

#print(either_of_two([1,2,3,4],[1,2,6,7,8,9]))

# Funcion to calculate elements in neither of two sets but in universal sets.
def neither_of_two(set1,set2,universal_set):
    #universal_set=[1,2,3,4,5,6,7,8,9]
    union = set1 + set2
    neither=[]
    for element in universal_set:
        if element not in union:
            neither.append(element)
    return(set(neither))

#print(neither_of_two([1,2,3],[2,3,4,5,6]))

# Function to calculate elements in set1 and set2 but not in set3.
def not_in_third(set1,set2,set3):
    not_third = []
    intersect_A_B = intersection(set1,set2)
    for element in intersect_A_B:
        if element not in set3:
            not_third.append(element)
    return set(not_third)
 

#print(not_in_third([1,2,3,12,13,14,45],[3,4,12,13,14,5,6],[2,4,6,7,8,9,0]))            

universal_set = list(map(int,input('Enter roll numbers of students in class seperated with space: ').split()))
cricket = list(map(int,input('Enter roll numbers of students who plays cricket seperated with space: ').split()))
badminton = list(map(int,input('Enter roll numbers of students who plays badminton seperated with space: ').split()))
football = list(map(int,input('Enter roll numbers of students who plays football seperated with space: ').split()))
 
cricket_badminton = intersection(cricket,badminton)
print('Students who play both cricket and badminton: ',cricket_badminton)

cricket_or_badmint = either_of_two(cricket,badminton)
print('Students who play either cricket or badminton but not both: ',cricket_or_badmint)

cricket_nor_badmint = neither_of_two(cricket,badminton,universal_set)
print('Students who play neither cricket nor badminton: ',cricket_nor_badmint)

crick_football_not_badmint = not_in_third(cricket,football,badminton)
print('Stuudent who play cricket and football but not badminton: ',crick_football_not_badmint) 

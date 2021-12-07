import time

# S_n is the set of all perms for a list of notes
def listPermsnTo0(n):
    if(n == 0):
        return [[0]]
    else:
        S_n = []
        X = listPermsnTo0(n-1)
        for perm in X:
            S_n = joinPermLists(S_n, insertEverywhere(n, perm))
        return S_n

def listPerms0TOn(n_start, n_current):
    if(n_current == n_start):
        return [[n_start]]
    else:
        S_n = []
        X = listPerms0TOn(n_start, n_current+1)
        for perm in X:
            S_n = joinPermLists(S_n, insertEverywhere(n_current, perm))
        return S_n

def insertEverywhere(note, perm):
    inserted_everywhere = []
    for i in range(len(perm)+1):
        perm_copy = perm.copy()
        perm_copy.insert(i,note)
        inserted_everywhere.append(perm_copy)
    return inserted_everywhere

def joinPermLists(S_n, perms):
    for perm in perms:
        S_n.append(perm)
    return S_n

# Counts the number of perms for a given "n"
def countPerm(n):
    if(n == 1):
        return 1
    else:
        return n*countPerm(n-1)

def writeByLine(l):
        f = open("output.txt", "a")
        f.write(str(l))


while True:
    user_input = input("Enter a number, or q to quit: \n")
    if user_input.lower() == 'q':
        break
    selection = input('"0" for 0 to n traversal \n"n" for n to 0 traversal \n"c" for number of permutations \n')
    if selection == '0':
        print('Permutations:')
        start = time.time()
        print(listPermsnTo0(int(user_input)))
        end = time.time()
        time_to_run = end - start
        print('It took %f seconds to run this permutation' % (time_to_run))
    elif selection == 'n':
        print('Permutations:')
        start = time.time()
        print(listPerms0TOn(int(user_input),0))
        end = time.time()
        time_to_run = end - start
        print('It took %f seconds to run this permutation' % (time_to_run))
    elif selection == 'c':
        print('Number of permutations:')
        print(countPerm(int(user_input)))

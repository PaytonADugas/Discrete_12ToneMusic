import time

# N is the number of notes or elements we want in our permutations
# S_n is the list of all permutations up to whatever n is in the current recursive state
# X is the list of perms for (n-1) elements which is then recursively added to S_n
# This recursive function starts at n = n and finishes at n = 0
def listPerms_nTo0(n):
    if(n == 0):
        return [[0]]
    else:
        S_n = []
        X = listPerms_nTo0(n-1)
        # takes the perms in x that are up to n-1 and adds whatever n is to make a list of perms to n
        for perm in X:
            S_n = joinPermLists(S_n, insertEverywhere(n, perm))
        return S_n

# This is the same as the function listPerms_nTo0 but it starts at 0 and finishes at n
def listPerms_0TOn(n_start, n_current):
    if(n_current == n_start):
        return [[n_start]]
    else:
        S_n = []
        X = listPerms_0TOn(n_start, n_current+1)
        for perm in X:
            S_n = joinPermLists(S_n, insertEverywhere(n_current, perm))
        return S_n

# Takes a perm [1,2] and adds a 'n' everywehre in that perm => {[n,1,2],[1,n,2],[1,2,n]}
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

# Counts the number of perms for a given number "n"
def countPerm(n):
    if(n == 0 ):
        return 1
    else:
        return n*countPerm(n-1)

# We're supposed to write the perms to a file for some reason and then count them
# but it doesn't make a whole lot of sense, so this is just here to satisfy that requirement
def writeByLine(l):
        f = open("output.txt", "a")
        f.write(str(l))

# This runs through all perms until n = 9, [0,1,2,3,4,5,6,7,8,9] which is the max my computer can handle,
# and prints out stats about running them
def runTest():
    for i in range(10):
        print('Running permutations for n = ' + str(i))
        start = time.time()
        listPerms_nTo0(i)
        end = time.time()
        time_to_run = end - start
        print('Finished running permutations in: '+str(time_to_run)+' seconds')
        print('There are '+str(countPerm(i+1))+' permutations for n = '+str(i))
    print('Max permutations reached was n = 9')


# This is unimportant for the paper. It just handles user input
while True:
    user_input = input("Enter a number, t for a full test, or q to quit: \n")
    if user_input.lower() == 't':
        runTest()
    if user_input.lower() == 'q':
        break
    selection = input('"0" for 0 to n traversal \n"n" for n to 0 traversal \n"c" for number of permutations \n')
    if selection == '0':
        print('Permutations:')
        start = time.time()
        print(listPerms_nTo0(int(user_input)))
        end = time.time()
        time_to_run = end - start
        print('It took %f seconds to run this permutation' % (time_to_run))
    elif selection == 'n':
        print('Permutations:')
        start = time.time()
        print(listPerms_0TOn(int(user_input),0))
        end = time.time()
        time_to_run = end - start
        print('It took %f seconds to run this permutation' % (time_to_run))
    elif selection == 'c':
        print('Number of permutations:')
        print(countPerm(int(user_input)))

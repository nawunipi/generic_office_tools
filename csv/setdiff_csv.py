import csv

def csvtoset(filepath):
    with open(filepath, 'r') as file:
        csvread = csv.reader(file)
        rawlist = list(csvread)
        mylist = [(a[0]) for a in rawlist]
    myset = set(mylist)
    return(myset)

def opAminusB(a, b):
    c = a-b
    print('member diff:')
    print(c)
    print('len diff: ' + str(len(c)))
    
A_path = ''
B_path = ''

A = csvtoset(A_path)
B = csvtoset(B_path)

print('//////////// A-B: ///////////')
opAminusB(A, B)
print('//////////// B-A: ////////////')
opAminusB(B, A)

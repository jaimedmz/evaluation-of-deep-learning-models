import csv

def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))

#varia='2'
data=[]
def findClass(varia):
    with open("Test.csv") as csvfile: 
        reader = csv.reader (csvfile)
        for row in reader: 
            data.append(row) 

    col = [x[6] for x in data]
    #print(col)
    if varia in col: 
        for x in range(0,len(data)): 
            if varia == data[x][6]: 
                print(data[x])
    else: print("No está el archivo")
#findClass(varia)


#nom='Test/00000.png'
data=[]
def findExpectedClass(nom):
    with open("Test.csv") as csvfile: 
        reader = csv.reader (csvfile)
        for row in reader: 
            data.append(row) 

    col = [x[7] for x in data]
    #print(col)
    if nom in col: 
        for x in range(0,len(data)): 
            if nom == data[x][7]: 
                print(data[x][6])
                return (data[x][6])
    else: print("No está el archivo")
    #print(nom)   
#findExpectedClass('Test/00009.png')


data=[]
def sumClassesFinded(nom):
    with open("Test.csv") as csvfile: 
        reader = csv.reader (csvfile)
        for row in reader: 
            data.append(row) 

    col = [x[7] for x in data]
    #print(col)
    if nom in col: 
        for x in range(0,len(data)): 
            if nom == data[x][7]: 
                return 1
    else: 
        return -1
    #print(nom)   
#findExpectedClass('Test/00009.png')
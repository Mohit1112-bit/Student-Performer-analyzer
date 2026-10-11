import csv
import numpy as np 
def all_data():
    id = []
    name = []
    data = []
    with open('test.csv') as f :
        reader = csv.reader(f)

        header = next(reader)
        for row in reader :
            id.append(int(row[0]))
            name.append(row[1])
            data.append(list(map(float,row[2:])))
        return id , name , data 


def array_converter(a):
    return np.array(a)



if __name__=='__main__':
    print(all_data())
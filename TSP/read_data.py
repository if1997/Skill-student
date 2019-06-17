import numpy as np 

class read_data():
    def __init__(self,PATH):
        self.path=PATH

    def data(self):
        try:
            with open(self.path,'r') as FILE:
                address=[]
                for i in FILE.readlines():
                    add=i.split(',')
                    #address.append([add[0],np.array([float(add[1]),float(add[2])])])
                    address.append([add[0],float(add[1]),float(add[2])])
                return address
        except:
            return 'read file error'
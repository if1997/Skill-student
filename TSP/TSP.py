from GA import GA
from GA import City
import math
class TSP():
    #city城市列表,init_city初始城市的序号,count次数
    def __init__(self,city,init_city,count):
        self.CITY=city
        self.INITCITY=init_city
        self.Count=count
        self.ga=GA(cross_rate=0.7,variation_rate=0.02,city_num=len(self.CITY),
        population_count=self.Count,adaptabilty=self.adaptabilty())


    
    #欧氏
    def distance(self,order):
        distance=0
        for i in range(self.INITCITY,self.INITCITY-len(order),-1):
            #distance+=np.linalg.norm(self.CITY[order[i]][1]-self.CITY[order[i-1]][1])
            distance+=math.sqrt((self.CITY[order[i]][1]-self.CITY[order[i-1]][1])**2+(self.CITY[order[i]][2]-self.CITY[order[i-1]][2])**2)
        return distance

    #适应度为1/距离
    def adaptabilty(self):
        return lambda life:1.0/self.distance(life.gene)


    def run(self,n=0):
        while n>0:
            self.ga.next()
            distance=self.distance(self.ga.best.gene)
            if n%100==0:
                print("{}:{}".format(self.ga.generation,distance))
            n-=1
            
        print("经过%d次迭代，最优解距离为：%f"%(self.ga.generation,distance))
        return self.ga.best.gene
        
"""
def main():
    City=read_data("../人工智能与大数据实验/data.txt").data()
    print(City)
    tsp=TSP(city=City,init_city=3,count=100)
    tsp.run(1000)

if __name__=='__main__':
    main()

"""
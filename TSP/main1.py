import matplotlib.pyplot as plt
from TSP import TSP
from read_data import read_data


City=read_data("../人工智能与大数据实验/data.txt").data()
print(City)

tsp=TSP(city=City,init_city=3,count=1000)
tsp.run(10000)

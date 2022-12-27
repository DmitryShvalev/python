from functools import reduce
import csv

with open("polnyy_perechen_sportivnyh_obek_0.csv", "r") as file:
   keys = file.readline()
   reader = csv.reader(file, delimiter=";")
   dataset = [x for x in reader]
keys = list(keys.split(","))
city = list(map(lambda x: x[12] == 'Chita', dataset))
print(city.count(True))
'''"""'#data = []

#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv

#with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))"""

data = pandas.read_csv("weather_data.csv")
avg_temp = data['temp'].sum()/len(data['temp'])

max_temp = data.temp.max()

print(max_temp)

print(data.temp[0] * 1.8 + 32)'''
import pandas
import csv

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_num = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_num = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_num = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_num, cinnamon_num, black_num]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


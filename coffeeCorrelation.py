import plotly.express as px
import csv
#used for finding correlation
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="sleep in hours",y="Coffee in ml")
      fig.show()

def getDataSource(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        #appending every row value with that heading to respective list
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))

    return{"x":sleep,"y":coffee}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    # 0 = x, 1 = y
    print(correlation[0,1])

def setUp():
    data_path= "coffee.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setUp()
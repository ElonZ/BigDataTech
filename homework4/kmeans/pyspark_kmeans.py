import re
import sys
from pyspark import SparkConf, SparkContext
import numpy as np
from operator import add
import pandas as pd



conf = SparkConf()
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")
MAX_ITER = 100

def pyspark_kmeans(data_txt, centroid_txt):
    # Load the data
    data = sc.textFile(data_txt).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()

    # Load the initial centroids
    centroids1 = pd.read_csv(centroid_txt, sep=" ", header=None)

    def compute_distance(line):
        distance = []
        for center in range(10):
            sum = 0
            for i in range(len(line)):
                sum += (line[i] - centroids1.loc[center, i]) ** 2
            distance.append(sum)
        # print("The distance is {}".format(distance))
        my_min = min(distance)
        belongs_to = [i for i, j in enumerate(distance) if j == my_min]
        return belongs_to[0]

    for i in range(MAX_ITER):
        print("Currently in iteration {}".format(i))
        # Assign an index
        group = data.map(lambda line: compute_distance(line))
        data_with_index = group.zip(data)

        aTuple = (0, 0)  # As of Python3, you can't pass a literal sequence to a function.
        agg_data = data_with_index.aggregateByKey(aTuple, lambda a, b: (a[0] + b, a[1] + 1),
                                       lambda a, b: (a[0] + b[0], a[1] + b[1]))

        avg_result = agg_data.mapValues(lambda v: v[0] / v[1]).sortByKey()

        substitute = pd.DataFrame()
        for i,j in avg_result.collect():
            substitute = substitute.append(pd.Series(j),ignore_index= True)

        centroids1 = substitute

    centroids1.to_csv(r'centroids_output.txt', header=None, index=None, sep=' ', mode='a')



if __name__ == '__main__':
    pyspark_kmeans('data.txt', 'c1.txt')
    sc.stop()


from pyspark import SparkContext


def matrix_multiplication(matrix_file, vector_file):

    matrix = sc.textFile(matrix_file).map(lambda x: x.split(',')[1:]).map(lambda value: [float(x) for x in value]).cache()
    vector = sc.textFile(vector_file).map(lambda x: x.split(',')).map(lambda value: [float(x) for x in value]).cache()


    matrix_ind = matrix.zipWithIndex()

    matrix_flat = matrix_ind.map(lambda line:(line[1], [(line[0][i], i) for i in range(len(line[0]))])).flatMap(lambda line: [(i[1], (line[0], i[0])) for i in line[1]])

    vector_flat = vector.flatMap(lambda line: [(i, line[i]) for i in range(len(line))])

    matrix_join = matrix_flat.join(vector_flat)
    matrix_join = matrix_join.map(lambda line:(line[1][0][0], line[1][0][1] * line[1][1])).reduceByKey(lambda a, b: a + b).map(lambda line: line[1])

    calc_res = matrix_join.collect()

    file = open("output.txt", "w")
    for num in calc_res:
        file.write(str(num) + ', ')
        file.write('\n')
    file.close()
    sc.stop()
    return matrix_join

if __name__ ==  "__main__":
    sc = SparkContext('local[4]', 'hw4')
    res = matrix_multiplication('A.txt','B.txt')


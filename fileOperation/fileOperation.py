FILE_PATH = "C:/repos/travelingSalesmanProblemWithGeneticAlgorithm/ch150.tsp"

def tspValueCatcher():
    CitiesCoordinates = []
    with open(FILE_PATH, 'r') as file:
        inFile = file.readlines()
        i = 1
        index = 0
        for row in inFile:
            x = row.split(" ")
            if x[0] == str(i):
                y = x[2].split('\n')
                coordinates = {"id": index, "x": round(float(x[1])), "y": round(float(y[0]))}
                CitiesCoordinates.append(coordinates)
                i = i + 1
                index = index + 1
    return CitiesCoordinates
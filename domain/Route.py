import random

class Route:
    def __init__(self, routeManager, tour=None):
        self.routeManager = routeManager
        self.tour = []
        self.fitness = 0.0
        self.distance = 0
        if tour is not None:
            self.tour = tour
        else:
            for i in range(0, self.routeManager.numberOfCities()):
                self.tour.append(None)

    def __len__(self):
        return len(self.tour)

    def __getitem__(self, index):
        return self.tour[index]

    def __setitem__(self, key, value):
        self.tour[key] = value

    def __repr__(self):
        geneString = "|"
        for i in range(0, self.tourSize()):
            geneString += str(self.getCities(i)) + "|"
        return geneString

    def crateRouteManager(self):
        for CitiesIndex in range(0, self.routeManager.numberOfCities()):
            self.setCities(CitiesIndex, self.routeManager.getCities(CitiesIndex))
        random.shuffle(self.tour)

    def getCities(self, tourPosition):
        return self.tour[tourPosition]

    def setCities(self, tourPosition, Cities):
        self.tour[tourPosition] = Cities
        self.fitness = 0.0
        self.distance = 0

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.getDistance())
        return self.fitness

    def getDistance(self):
        if self.distance == 0:
            tourDistance = 0
            for CitiesIndex in range(0, self.tourSize()):
                fromCities = self.getCities(CitiesIndex)
                destinationCities = None
                if CitiesIndex + 1 < self.tourSize():
                    destinationCities = self.getCities(CitiesIndex + 1)
                else:
                    destinationCities = self.getCities(0)
                tourDistance += fromCities.toDistance(destinationCities)
            self.distance = tourDistance
        return self.distance

    def tourSize(self):
        return len(self.tour)

    def containsCities(self, Cities):
        return Cities in self.tour
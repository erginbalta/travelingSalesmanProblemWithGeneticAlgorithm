import domain.Route as rt

class Population:
    def __init__(self, routeManager, populationSize, initialise):
        self.routes = []
        for i in range(0, populationSize):
            self.routes.append(None)

        if initialise:
            for i in range(0, populationSize):
                newRoute = rt.Route(routeManager)
                newRoute.crateRouteManager()
                self.saveRoute(i, newRoute)

    def __setitem__(self, key, value):
        self.routes[key] = value

    def __getitem__(self, index):
        return self.routes[index]

    def saveRoute(self, index, tour):
        self.routes[index] = tour

    def getRoute(self, index):
        return self.routes[index]

    def getFittest(self):
        fittest = self.routes[0]
        for i in range(0, self.populationSize()):
            if fittest.getFitness() <= self.getRoute(i).getFitness():
                fittest = self.getRoute(i)
        return fittest

    def populationSize(self):
        return len(self.routes)

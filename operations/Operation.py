import random
import domain.Route as rt
import domain.Population as pp

class Operations:
    def __init__(self, routeManager):
        self.routeManager = routeManager
        self.mutationRate = 0.01
        self.tournamentSize = 20
        self.elitism = True

    def createPopulation(self, pop):
        newPopulation = pp.Population(self.routeManager, pop.populationSize(), False)
        elitismOffset = 0
        if self.elitism:
            newPopulation.saveRoute(0, pop.getFittest())
            elitismOffset = 1

        for i in range(elitismOffset, newPopulation.populationSize()):
            parent1 = self.tournamentSelection(pop)
            parent2 = self.tournamentSelection(pop)
            child = self.crossover(parent1, parent2)
            newPopulation.saveRoute(i, child)

        for i in range(elitismOffset, newPopulation.populationSize()):
            self.mutate(newPopulation.getRoute(i))

        return newPopulation

    def crossover(self, parent1, parent2):
        child = rt.Route(self.routeManager)

        startPos = int(random.random() * parent1.tourSize())
        endPos = int(random.random() * parent1.tourSize())

        for i in range(0, child.tourSize()):
            if startPos < endPos and i > startPos and i < endPos:
                child.setCities(i, parent1.getCities(i))
            elif startPos > endPos:
                if not (i < startPos and i > endPos):
                    child.setCities(i, parent1.getCities(i))

        for i in range(0, parent2.tourSize()):
            if not child.containsCities(parent2.getCities(i)):
                for ii in range(0, child.tourSize()):
                    if child.getCities(ii) == None:
                        child.setCities(ii, parent2.getCities(i))
                        break

        return child

    def mutate(self, tour):
        for tourPos1 in range(0, tour.tourSize()):
            if random.random() < self.mutationRate:
                tourPos2 = int(tour.tourSize() * random.random())

                cities1 = tour.getCities(tourPos1)
                cities2 = tour.getCities(tourPos2)

                tour.setCities(tourPos2, cities1)
                tour.setCities(tourPos1, cities2)

    def tournamentSelection(self, pop):
        tournament = pp.Population(self.routeManager, self.tournamentSize, False)
        for i in range(0, self.tournamentSize):
            randomId = int(random.random() * pop.populationSize())
            tournament.saveRoute(i, pop.getRoute(randomId))
        fittest = tournament.getFittest()
        return fittest


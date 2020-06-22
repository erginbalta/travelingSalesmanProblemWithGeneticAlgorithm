import fileOperation.fileOperation as fl
import domain.Cities as ct
import domain.RouteManager as rm
import domain.Population as pp
import operations.Operation as op

def main():
    routeManager = rm.RouteManager()
    citiesList = fl.tspValueCatcher()
    for i in citiesList:
        city = ct.Cities(i["x"], i["y"])
        routeManager.addCity(city)

    pop = pp.Population(routeManager, 100, True)

    initialDistance = str(round(pop.getFittest().getDistance(),2))
    print("Initial distance: " +str(initialDistance))

    ga = op.Operations(routeManager)
    pop = ga.createPopulation(pop)

    for i in range(0, 100):
        pop = ga.createPopulation(pop)

    finalDistance = str(round(pop.getFittest().getDistance(),2))
    print("Final distance: " +finalDistance)

if __name__ == '__main__':
    main()


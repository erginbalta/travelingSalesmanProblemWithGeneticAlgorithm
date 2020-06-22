class RouteManager:
    destination = []

    def addCity(self, Cities):
        self.destination.append(Cities)

    def getCities(self, index):
        return self.destination[index]

    def numberOfCities(self):
        return len(self.destination)


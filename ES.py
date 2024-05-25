import random
class Simulation():
    '''A class to control simulation and help facilitate the spread of disease'''
    def _init_(self):
        self.dayNumber=1
        print("To proceed with simulation we must know Population Size")
        self.populationSize = int(input("Enter the Population Size: "))
        print("\nEpidemic starts with infecting a portion of population")
        self.infectionPercentage = float(input("Enter the Percentage of population to initially infect: "))
        self.infectionPercentage /= 100
        print("To proceed with simulation we must know the risk a person has to contract the disease when exposed")
        self.infectionProbability = float(input("Enter the probability(0-100) that a person gets infected when exposed to the disease: "))
        print("To proceed with simulation we must know how long the infection will Last when Exposed")
        self.dayNumber=int(input("Enter the duration in days of the Infection: "))
        print("To proceed with simulation we must know mortality rate of infected people")
        self.mortalityRate = float(input("Enter the mortality rate of Infected People: "))
        print("To proceed with simulation we must know how long to run the simulation")
        self.simulationDays = int(input("Enter the number of days to simulate: "))
class Person():
    '''Class to represent an individual from the Population'''
    def _init_(self):
        self.isInfected=False  #person will not be infected initially
        self.isDead=False      #person will not be dead initially 
        self.daysInfected=0    #to track the days a person is infected for
        
    def infect(self,simulation):
        #generate a random value that is the probability of the individual to get infected
        if random.randint(0,100)<simulation.infectionProbability:
            self.isInfected=True
    
    def heal(self):
        self.isInfected=False
        self.daysInfected=0
        
    def die(self):
        self.isDead=True
        
    def update(self,simulation):
        #update individual
        #check if person is not dead
      if not self.isDead:
              #if person is infected
              if self.isInfected:
                  self.daysInfected +=1
                  #generate a random number and check with mortality
                  if random.randint(0,100)<simulation.mortalityRate:
                      self.die()
                  elif  self.daysInfected==simulation.dayNumber:
                      self.heal()
class Population():
    '''to handle whole population'''
    def _init_(self,simulation):
        self.population = []
        for i in range (simulation.populationSize):
            person = Person()
            self.population.append(person)
    
    def initialInfection(self,simulation):
        infectedCount=int(round(simulation.infectionPercentage * simulation.populationSize,0))
        
        #infect exact no. of people 
        for i in range(infectedCount):
            self.population[i].isInfected=True
            self.population[i].daysInfected=1
            
            random.shuffle(self.population)
    def spreadInfection(self,simulation):
        #spread to nearby people
        for i in range(len(self.population)):
            if self.population[i].isDead== False:
                # for 1st person in the list,(i+1)
                if i ==0:
                    if self.population[i+1].isInfected:
                        self.population[i].infect(simulation)
                        
                #person in middle, check left and right
                elif i<len(self.population)-1:
                    if self.population[i-1].isInfected or self.population[i+1].isInfected:
                        self.population[i].infect(simulation)
                        
                #for the last person in list
                elif i<len(self.population)-1:
                    if self.population[i-1].isInfected:
                        self.population[i].infect(simulation)
                        
    def Update(self,simulation):
        simulation.dayNumber+=1
        #to update each number
        for person in self.population:
            person.update(simulation)
    def showStatistics(self,simulation):
        totalInfectedCount=0
        totalDeathCount=0
        for person in self.population:
            if person.isInfected:
                totalInfectedCount+=1
            if person.isDead:
                totalDeathCount+=1
                
        #percentage of population infected & dead
        infectedPercent = round(100*(totalInfectedCount/simulation.populationSize),4)
        deathPercent = round(100*(totalDeathCount/simulation.populationSize),4)
        
        #summary 
        print("\n Day Number: " + str(simulation.dayNumber))
        print("Percentage of Population Infected: " + str(infectedPercent)+"%")
        print("Percentage of Population Dead : " + str(deathPercent)+"%")
        print("Total People Infected: " + str(totalInfectedCount)+"%" + str(simulation.populationSize))
        print("Total Deaths: " + str(totalDeathCount) + "/" + str(simulation.populationSize))
    def graphics(self):
        status=[]
        for person in self.population:
            if person.isDead:
                char='X'
            else:
                if person.isInfected:
                    char='I'
                else:
                    char='O'
            status.append(char)
        for letter in status:
            print(letter,end='-')
        '''Main Code'''
#simulation object
    sim = Simulation()

#Population Object
    pop = Population(sim)
#Set the initial Infection Condition
    op.initialInfection(sim)
#display Statistics
    pop.showStatistics(sim)
#show graphics
    pop.graphics()
    input("\nPress Enter to begin the Simulation")
#Run the Simulation
    for i in range(1,sim.simulationDays):
        pop.spreadInfection(sim)
        pop.Update(sim)
        pop.showStatistics(sim)
        pop.graphics()

        if i!=sim.simulationDays - 1:
            input("Press Enter to Continue the Simulation")
import numpy as np
import simpy
import collections as col

# shortcuts for some NumPy functions
rint = np.random.randint
choice = np.random.choice

# simulation parameters
SIM_TIME = 1000
LAND = (300,300)
GRASS_COVERAGE = 0.5

# initial number of animals
INITIAL_SHEEP = 6000
INITIAL_WOLF = 200

# how much energy a sheep gets from eating a grass
ENERGY_FROM_GRASS = 5

# random energy parameter for animals when born
ENERGY_AT_BIRTH = [10, 20]

# probabilities of reproducing
SHEEP_REPRODUCE = 0.04
WOLF_REPRODUCE = 0.006

class Animal(object):
    '''
        Animal class
    '''
    def __init__(self, i, env, energy, pos, plane):
        '''
            Default constructor
        '''
        # attributes
        self.energy = energy
        self.pos = pos          # current position

        # is the animal still alive
        self.alive = True
        self.causeOfDeath = None

        # when did the animal ate the last
        self.lastTimeEaten = 0

        # range of movements
        self.movements = [i for i in range(-50,51)]

        # pointer to environment and the plane
        self.env = env
        self.plane = plane
        self.id = i

    def move(self):
        '''
            Changing the animal's position
        '''
        # determining the horizontal and vertical moves
        h = choice(self.movements)
        v = choice(self.movements)

        # adjusting the position
        self.pos[0] += h
        self.pos[1] += v

        # making sure we do not go outside the predefined land
        self.pos[0] = np.min(
            [np.max([0, self.pos[0] - 1]), LAND[0] - 1]
        )

        self.pos[1] = np.min(
            [np.max([0, self.pos[1] - 1]), LAND[1] - 1]
        )

        # and subtracting the energy due to move
        self.energy -= (h+v) / 4

    def getPosition(self):
        '''
            Method to return the position of the animal
        '''
        return self.pos

    def die(self, cause):
        '''
            Method to reflect the death of the animal
        '''
        self.alive = False
        self.causeOfDeath = cause

    def isAlive(self):
        '''
            Method to check whether the animal is still alive
        '''
        return self.alive

    def getCauseOfDeath(self):
        '''
            What killed the animal
        '''
        return self.causeOfDeath

    def getEnergy(self):
        '''
            Get the energy of the animal
        '''
        return self.energy

class Sheep(Animal):
    '''
        Sheep class derived from Animal
    '''
    def __init__(self, i, env, energy, pos, plane):
        '''
            Default constructor (invokes the constructor of
            Animal)
        '''
        Animal.__init__(self, i, env, energy, pos, plane)

    def eatGrass(self):
        '''
            Sheep eat grass
        '''
        if self.plane.hasGrass(self.pos):
            # get the energy from grass 
            self.energy += ENERGY_FROM_GRASS
            if self.energy > 200:
                self.energy = 200
            self.lastTimeEaten = self.env.now

            # and flag that the grass has been eaten
            self.plane.grassEaten(self.pos)

class Wolf(Animal):
    '''
        Wolf class derived from Animal
    '''
    def __init__(self, i, env, energy, pos, plane):
        '''
            Default constructor
        '''
        Animal.__init__(self, i, env, energy, pos, plane)

    def eatSheep(self):
        '''
            Wolves eat sheep
        '''
        # get the sheep at the particular position on the 
        # plane
        sheep = self.plane.getSheep(self.pos)
        
        # decide how many will be eaten
        howMany = np.random.randint(1, 
            np.max([len(sheep), 2]))

        # and feast
        for i, s in enumerate(sheep):
            # we're checking if the sheep is still alive
            # as the removal of sheep that died happens later
            if s.isAlive() and i < howMany:
                self.energy += s.getEnergy() / 20
                if self.energy > 200:
                    self.energy = 200
                s.die('eaten') 

        # update the time of the last meal
        self.lastTimeEaten = self.env.now

class Plane(object):
    '''
        Plane class
    '''
    def __init__(self, env, bounds, grassCoverage, 
        sheep, wolves):
        '''
            Default constructor
        '''        
        # pointer to the environment
        self.env = env

        # bounds of the plane
        self.bounds = bounds

        # grass
        self.grassCoverage = grassCoverage
        self.grass = [
            [0  for _ in range(self.bounds[0])] 
                for _ in range(self.bounds[1])
        ]

        # we keep track of eaten grass
        self.grassEatenIndices = col.defaultdict(list)

        # create the animals
        self.noOfSheep  = sheep
        self.noOfWolves = wolves

        self.sheep = []
        self.wolves = []

        # keep track of counts
        self.counts = {
            'sheep': {
                'count': 0,
                'died': {
                    'energy': 0,
                    'eaten': 0,
                    'age': 0,
                },
                'born': 0
            },
            'wolves': {
                'count': 0,
                'died': {
                    'energy': 0,
                    'age': 0,
                },
                'born': 0
            } 
        }

        # generate the grass and animals
        self.generateGrass()
        self.generateSheep()
        self.generateWolves()

        # and start monitoring and simulation processes
        self.monitor = self.env.process(
            self.monitorPopulation())
        self.action = self.env.process(self.run())

    def run(self):
        '''
            Main loop of the simulation
        '''
        while True:
            # first, move the animals on the plane
            self.updatePositions()

            # and let them eat
            self.eat()

            # then let's see how many of them will reproduce
            self.reproduceAnimals()

            # and keep track of the grass regrowth
            self.env.process(self.regrowGrass())

            # finally, print the telemetry to the screen
            toPrint = '{tm}\t{sheep_alive}\t{sheep_born}'
            toPrint += '\t{sheep_died_energy}'
            toPrint += '\t{sheep_died_eaten}'
            toPrint += '\t{wolves_alive}\t{wolves_born}'
            toPrint += '\t{wolves_died_energy}'


            print(toPrint.format(
                tm=int(self.env.now), 
                sheep_alive=int(len(self.sheep)), 
                sheep_born=self.counts['sheep']['born'],
                sheep_died_energy= \
                   self.counts['sheep']['died']['energy'],
                sheep_died_eaten= \
                    self.counts['sheep']['died']['eaten'],
                sheep_died_age= \
                    self.counts['sheep']['died']['age'],
                wolves_alive=int(len(self.wolves)), 
                wolves_born=self.counts['wolves']['born'],
                wolves_died_energy= \
                    self.counts['wolves']['died']['energy'],
                wolves_died_age= \
                    self.counts['wolves']['died']['age'])
            )

            # and wait for another iteration
            yield self.env.timeout(1)

    def generateGrass(self):
        '''
            Method to populate the plane with grass
        '''
        # number of tiles on the plane
        totalSize = self.bounds[0] * self.bounds[1]

        # how many of them will have grass
        totalGrass = int(totalSize * self.grassCoverage)

        # randomly spread the grass on the plane
        grassIndices = sorted(
            choice(totalSize, totalGrass, replace=False))

        for index in grassIndices:
            row = int(index / self.bounds[0])
            col = index - (self.bounds[1] * row)

            self.grass[row][col] = 1

    def hasGrass(self, pos):
        '''
            Method to check if the tile has grass
        '''
        if self.grass[pos[0]][pos[1]] == 1:
            return True
        else:
            return False

    def grassEaten(self, pos):
        '''
            Update eaten patches of the grass
        '''
        self.grass[pos[0]][pos[1]] = 0
        self.grassEatenIndices[self.env.now].append(pos)

    def regrowGrass(self):
        '''
            Regrow the grass
        '''
        # time to regrow the grass
        regrowTime = 2
        yield self.env.timeout(regrowTime)
        
        # then we make the grass available at the position
        for pos in self.grassEatenIndices[
            self.env.now - regrowTime]:
            self.grass[pos[0]][pos[1]] = 1

    def generateSheep(self):
        '''
            Method to populate the plane with sheep
        '''
        # place the sheep randomly on the plane
        for _ in range(self.noOfSheep):
            pos_x = rint(0, LAND[0])
            pos_y = rint(0, LAND[1])
            energy = rint(*ENERGY_AT_BIRTH)

            self.sheep.append(
                Sheep(
                    self.counts['sheep']['count'], 
                    self.env, energy, [pos_x, pos_y], self)
                )
            self.counts['sheep']['count'] += 1

    def generateWolves(self):
        '''
            Method to populate the plane with wolves
        '''
        # place the wolves randomly on the plane
        for _ in range(self.noOfWolves):
            pos_x = rint(0, LAND[0])
            pos_y = rint(0, LAND[1])
            energy = rint(*ENERGY_AT_BIRTH)

            self.wolves.append(
                Wolf(
                    self.counts['wolves']['count'], 
                    self.env, energy, [pos_x, pos_y], self)
                )

            self.counts['wolves']['count'] += 1

    def updatePositions(self):
        '''
            Method to update the positions of animals
        '''
        for s in self.sheep:
            s.move()

        for w in self.wolves:
            w.move()
            
    def eat(self):
        '''
            Method to feed animals
        '''
        for s in self.sheep:
            s.eatGrass()

        for w in self.wolves:
            w.eatSheep()

    def getSheep(self, pos):
        '''
            Method to return a list of sheep at the specified
            position
        '''
        return [s for s in self.sheep 
            if s.getPosition() == pos]

    def reproduceAnimals(self):
        '''
            Method to reproduce animals
        '''
        # counting the number of births
        births = {'sheep': 0, 'wolves': 0}

        # reproduce sheep
        for s in self.sheep:
            # determine if the animal will reproduce
            willReproduce = np.random.rand() < \
                (SHEEP_REPRODUCE * 3 / \
                    (self.env.now - s.lastTimeEaten + 1))

            # if will reproduce and is still alive --
            # give birth at the same position as the mother
            if willReproduce and s.isAlive():
                energy = rint(*ENERGY_AT_BIRTH)
                self.sheep.append(
                    Sheep(self.counts['sheep']['count'], 
                        self.env, energy, 
                        s.getPosition(), self))

                # increase the overall count of sheep
                self.counts['sheep']['count'] += 1

                # and the birth counter
                births['sheep'] += 1

        # reproduce wolves
        for w in self.wolves:
            # determine if the animal will reproduce
            willReproduce = np.random.rand() < \
                ( WOLF_REPRODUCE / \
                    (self.env.now - w.lastTimeEaten  + 1))
            # if will reproduce and is still alive --
            # give birth at the same position as the mother
            if willReproduce and w.isAlive():
                energy = rint(*ENERGY_AT_BIRTH)
                self.wolves.append(
                    Wolf(self.counts['wolves']['count'], 
                        self.env, energy, 
                        w.getPosition(), self))
                
                # increase the overall count of wolves
                self.counts['wolves']['count'] += 1

                # and the birth counter
                births['wolves'] += 1

        # update the counts variable
        for animal in births:
            self.counts[animal]['born'] = births[animal]

    def monitorPopulation(self):
        '''
            Process to monitor the population
        '''
        # the process checks for animals that run out of
        # energy and removes them from simulation
        while True:
            for s in self.sheep:
                if s.energy < 0:
                    s.die('energy')

            for w in self.wolves:
                if w.energy < 0:
                    w.die('energy')
            
            # clean up method
            self.removeAnimalsThatDied()
                
            yield self.env.timeout(1)

    def removeAnimalsThatDied(self):
        '''
            Clean up method for removing dead animals
        '''
        # get all animals that are still alive and those
        # that died
        sheepDied = []
        wolvesDied = []

        sheepAlive = []
        wolvesAlive = []

        for s in self.sheep:
            if s.isAlive():
                sheepAlive.append(s)
            else:
                sheepDied.append(s)

        for w in self.wolves:
            if w.isAlive():
                wolvesAlive.append(w)
            else:
                wolvesDied.append(w)

        # keep only those that are still alive
        self.sheep = sheepAlive
        self.wolves = wolvesAlive
        
        # while for those that died -- update why they died
        cod = {'energy': 0, 'eaten': 0, 'age': 0}
        for s in sheepDied:
            cod[s.getCauseOfDeath()] += 1

        for cause in cod:
            self.counts['sheep']['died'][cause] = cod[cause]

        cod = {'energy': 0, 'age': 0}
        for w in wolvesDied:
            cod[w.getCauseOfDeath()] += 1

        for cause in cod:
            self.counts['wolves']['died'][cause] = cod[cause]
 
        # and finally -- release the memory by deleting the
        # animal objects
        for s in sheepDied:
            del s

        for w in wolvesDied:
            del w
        
if __name__ == '__main__':
    # create the environment
    env = simpy.Environment()

    # create the plane
    plane = Plane(env, LAND, GRASS_COVERAGE, 
        INITIAL_SHEEP, INITIAL_WOLF)

    # print the header
    print('\tSheep\t\tDied\t\tWolves\t\tDied\t')
    print('Time\tAlive\tBorn\tEnergy\tEaten\tAlive\tBorn\tEnergy')

    # and run the simulation
    env.run(until = SIM_TIME)
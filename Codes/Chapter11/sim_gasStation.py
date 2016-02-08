import numpy as np
import simpy
import itertools
# import collections as col

class FuelPump(object):
    '''
        Fuel pump class.
    '''
    def __init__(self, env, count):
        '''
            The main constructor of the class

            @param env   -- environment object
            @param count -- how many pumps for a certain
                            fuel type to instantiate
        '''
        # create the pump resource in the environment
        self.resource = simpy.Resource(env, count)

    def request(self):
        '''
            Wrapper method to create a request for an 
            available pump
        '''
        return self.resource.request()

class GasStation(object):
    '''
        Gas station class. 
    '''
    def __init__(self, env):
        '''
            The main constructor of the class

            @param env -- environment object
        '''
        # keep a pointer to the environment in the class
        self.env = env

        # fuel capacity (gallons) and reservoirs 
        # to track level
        self.CAPACITY = {'PETROL': 8000, 'DIESEL': 3000}
        self.RESERVOIRS = {}
        self.generateReservoirs(self.env, self.CAPACITY)

        # number of pumps for each fuel type
        self.PUMPS_COUNT = {'PETROL': 3, 'DIESEL': 1}
        self.PUMPS = {}
        self.generatePumps(self.env, self.CAPACITY, 
            self.PUMPS_COUNT)

        # how quickly they pump the fuel
        self.SPEED_REFUEL = 0.3 # 0.3 gal/s

        # set the minimum amount of fuel left before 
        # replenishing
        self.MINIMUM_FUEL = {'PETROL': 300, 'DIESEL': 100}

        # how long does it take for the track to get 
        # to the station after placing the call        
        self.TRUCK_TIME = 200
        self.SPEED_REPLENISH = 5

        # add the process to control the levels of fuel
        # available for sale
        self.control = self.env.process(self.controlLevels())

        print('Gas station generated...')

    def generateReservoirs(self, env, levels):
        '''
            Helper method to generate reservoirs
        '''
        for fuel in levels:
            self.RESERVOIRS[fuel] = simpy.Container(
                env, levels[fuel], init=levels[fuel])

    def generatePumps(self, env, fuelTypes, noOfPumps):
        '''
            Helper method to generate pumps
        '''
        for fuelType in fuelTypes:
                self.PUMPS[fuelType] = FuelPump(
                    env, noOfPumps[fuelType])

    def controlLevels(self):
        '''
            A method to check the levels of fuel (every 5s)
            and replenish when necessary
        '''
        while True:
            # loop through all the reservoirs
            for fuelType in self.RESERVOIRS:

                # and if the level is below the minimum
                if self.RESERVOIRS[fuelType].level \
                    < self.MINIMUM_FUEL[fuelType]:

                    # replenishes
                    yield env.process(
                        self.replenish(fuelType))
                # wait 5s before checking again
                yield env.timeout(5)

    def replenish(self, fuelType):
        '''
            A method to replenish the fuel
        '''
        # print nicely so we can distinguish when the truck
        # was called
        print('-' * 62)
        print('CALLING TRUCK AT {0:4.0f}s.' \
            .format(self.env.now))
        print('-' * 62)

        # waiting for the truck to come (lead time)
        yield self.env.timeout(self.TRUCK_TIME)

        # let us know when the truck arrived
        print('-' * 62)
        print('TRUCK ARRIVING AT {0:4.0f}s' \
            .format(self.env.now))

        # how much we need to replenish
        toReplenish = self.RESERVOIRS[fuelType].capacity - \
            self.RESERVOIRS[fuelType].level

        print('TO REPLENISH {0:4.0f} GALLONS OF {1}' \
            .format(toReplenish, fuelType))
        print('-' * 62)

        # wait for the truck to dump the fuel into 
        # the reservoirs
        yield self.env.timeout(toReplenish \
            / self.SPEED_REPLENISH)

        # and then add the fuel to the available one
        yield self.RESERVOIRS[fuelType].put(toReplenish)

        print('-' * 62)
        print('FINISHED REPLENISHING AT {0:4.0f}s.' \
            .format(self.env.now))
        print('-' * 62)

    def getPump(self, fuelType):
        '''
            Return a pump object
        '''
        return self.PUMPS[fuelType]

    def getReservoir(self, fuelType):
        '''
            Return a reservoir object
        '''
        return self.RESERVOIRS[fuelType]

    def getRefuelSpeed(self):
        '''
            Get how quickly the pumps work
        '''
        return self.SPEED_REFUEL

class Car(object):
    '''
        Car class.
    '''
    def __init__(self, i, env, gasStation):
        '''
            The main constructor of the class

            @param i          -- consecutive car id
            @param env        -- environment object
            @param gasStation -- gasStation object
        '''
        # pointers to the environment and gasStation objects
        self.env = env
        self.gasStation = gasStation

        # fuel type required by the car
        self.FUEL_TYPE = np.random.choice(
            ['PETROL', 'DIESEL'], p=[0.7, 0.3])

        # details about the car
        self.TANK_CAPACITY = np.random.randint(12, 23) # gal
        
        # how much fuel left
        self.FUEL_LEFT = self.TANK_CAPACITY \
            * np.random.randint(10, 40) / 100

        # car id
        self.CAR_ID = i

        # start the refueling process
        self.action = env.process(self.refuel())

    def refuel(self):
        '''
            Refueling method
        '''
        # what's the fuel type so we request the right pump
        fuelType = self.FUEL_TYPE

        # let's get the pumps object
        pump = gasStation.getPump(fuelType) 

        # and request a free pump
        with pump.request() as req:
            # time of arrival at the gas station
            arrive = self.env.now

            # wait for the pump
            yield req

            # how much fuel does the car need
            required = self.TANK_CAPACITY - self.FUEL_LEFT
            
            # time of starting refueling
            start = self.env.now
            yield self.gasStation.getReservoir(fuelType)\
                .get(required)

            # record the fuel levels
            petrolLevel = self.gasStation\
                        .getReservoir('PETROL').level
            dieselLevel = self.gasStation\
                        .getReservoir('DIESEL').level

            # and wait for it to finish
            yield env.timeout(required / gasStation \
                .getRefuelSpeed())

            # finally, print the details to the screen
            refuellingDetails = '{car}\t{tm}\t{start}'
            refuellingDetails += '\t{fin}\t{gal:2.2f}\t{fuel}'
            refuellingDetails += '\t{petrol}\t{diesel}'

            print(refuellingDetails \
                .format(
                    car=self.CAR_ID, 
                    tm=arrive, 
                    start=int(start), 
                    fin=int(self.env.now), 
                    gal=required, fuel=fuelType, 
                    petrol=int(petrolLevel), 
                    diesel=int(dieselLevel)
                )
            )

    @staticmethod
    def generate(env, gasStation):
        '''
            A static method to generate cars
        '''
        # generate as many cars as possible during the 
        # simulation run
        for i in itertools.count():
            # simulate that a new car arrives between 5s 
            # and 45s
            yield env.timeout(np.random.randint(5, 45))
            
            # create a new car
            Car(i, env, gasStation)

if __name__ == '__main__':
    # what is the simulation horizon (in seconds)
    SIM_TIME = 10 * 60 * 60 # 10 hours

    # create the environment
    env = simpy.Environment()

    # create the gas station
    gasStation = GasStation(env)

    # print the header
    print('\t\t\t\t\t\t     Left')
    header =  'CarID\tArrive\tStart\tFinish\tGal'
    header += '\tType\tPetrol\tDiesel'
    print(header)
    print('-' * 62)

    # create the process of generating cars
    env.process(Car.generate(env, gasStation))

    # and run the simulation
    env.run(until = SIM_TIME)
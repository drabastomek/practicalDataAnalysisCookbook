import numpy as np
import simpy

class RechargeStation(object):
    '''
        Recharge station class. 
    '''
    def __init__(self, env, loc):
        '''
            The main constructor of the class

            @param env -- environment object
            @param loc -- location of the station
        '''
        self.env = env
        self.LOCATION = loc

        # recharge speed assumed at 1% of the battery 
        # per minute
        self.RECHARGE_SPEED = 0.01 

    @staticmethod
    def generateRechargeStations(simTime):
        '''
            A static method to create gas stations along 
            the route. Gas stations are located every 
            80 - 140 miles

            @param simTime -- time of the simulation
        '''
        # we assume an average speed of 35MPH to calculate
        # a maximum distance that might be covered during 
        # the simulation timespan
        maxDistance = simTime / 60 * 35 * 2

        # generate the recharge stations
        distCovered = 0
        rechargeStations = [RechargeStation(env, 0)]

        while(distCovered < maxDistance):
            nextStation = np.random.randint(80, 140)

            distCovered += nextStation
            rechargeStations.append(
                RechargeStation(env, distCovered))
        
        return rechargeStations


class Car(object):
    '''
        Car class.
    '''
    def __init__(self, env, driver, rechargeStations):
        '''
            The main constructor of the class

            @param env              -- environment object
            @param driver           -- driver id
            @param rechargeStations -- list of recharge 
                                       stations
        '''
        # pointers to the environment and recharge stations 
        self.env = env
        self.rechargeStations = rechargeStations
        self.driver = driver

        # car parameters
        self.BATTERY_CAPACITY = np.random.choice([70, 85], 
            p=[0.5, 0.5])
        self.BATTERY_LEVEL = np.random.randint(80, 100) / 100 
        self.AVG_SPEED = np.random.randint(364, 492) / 10

        # average economy in kWh per mile
        # the below translates to ~89MPGe
        self.AVG_ECONOMY = np.random.randint(34, 38) / 100 

        # we start at the beginning of the road
        self.LOCATION = 0 

        # and let's drive
        self.action = self.env.process(self.driving())

    def driving(self):
        # updates every 15 minutes
        interval = 15

        # assuming constant speed -- how far the car travels
        # in each 15 minutes
        distanceTraveled = self.AVG_SPEED / 60 * interval

        # how much battery used to travel that distance
        batteryUsed = distanceTraveled * self.AVG_ECONOMY

        while True: 
            # update the location of the car
            self.LOCATION += distanceTraveled

            # how much battery power left
            batteryLeft = self.BATTERY_LEVEL \
                * self.BATTERY_CAPACITY - batteryUsed
            
            # update the level of the battery
            self.BATTERY_LEVEL = batteryLeft \
                / self.BATTERY_CAPACITY
            
            # if we run out of power -- stop
            if self.BATTERY_LEVEL <= 0.0:
                print()
                print('!~' * 15)
                print('RUN OUT OF JUICE...')
                print('!~' * 15)
                print()
                break

            # along the way -- check the distance to 
            # the next two recharge stations
            nearestRechargeStations = \
                [gs for gs in self.rechargeStations 
                    if gs.LOCATION > self.LOCATION][0:2]

            distanceToNearest = [rs.LOCATION \
                - self.LOCATION 
                for rs in nearestRechargeStations]

            # are we currently passing a recharging station?
            passingRechargeStation = self.LOCATION \
                + distanceTraveled > \
                    nearestRechargeStations[0].LOCATION

            # will we get to the next one on the charge left?
            willGetToNextOne = self.check(
                batteryLeft, 
                nearestRechargeStations[-1].LOCATION)

            # if we're passing the recharge station and 
            # we won't get to the next one -- let's recharge
            if passingRechargeStation \
                and not willGetToNextOne:

                # the charging can be interrupted by the 
                # driver
                try:
                    # how long will it take to fully recharge?
                    timeToFullRecharge = \
                        (1 - self.BATTERY_LEVEL) \
                        / nearestRechargeStations[0] \
                          .RECHARGE_SPEED

                    # start charging
                    charging = self.env.process(
                        self.charging(timeToFullRecharge, 
                            nearestRechargeStations[0] \
                            .RECHARGE_SPEED))

                    # and see if the driver will drive off 
                    # earlier than the car is fully recharged
                    yield self.env.process(self.driver \
                        .drive(self, timeToFullRecharge))

                # if the he/she does -- interrupt charging
                except simpy.Interrupt:

                    print('Charging interrupted at {0}' \
                        .format(int(self.env.now)))
                    print('-' * 30)

                    charging.interrupt()

            # update the progress of the car along the way
            toPrint = '{time}\t{level:2.2f}\t{loc:4.1f}'
            print(toPrint.format(time=int(self.env.now), 
                level=self.BATTERY_LEVEL, loc=self.LOCATION))
            
            # and wait for the next update
            yield self.env.timeout(interval)


    def check(self, batteryLeft, nextRechargeStation):
        '''
            Method to check if we are going to get to the
            next station
        '''
        distanceToNext = nextRechargeStation - self.LOCATION
        batteryToNext = distanceToNext / self.AVG_ECONOMY

        return batteryLeft > batteryToNext

    def charging(self, timeToFullRecharge, rechargeSpeed):
        '''
            Method to recharge the car
        '''
        # we are starting the recharge process
        try:
            # let's print out to the screen when this
            # happens
            print('-' * 30)
            print('Charging at {0}'.format(self.env.now))

            # and keep charging (every minute)
            for _ in range(int(timeToFullRecharge)):
                self.BATTERY_LEVEL += rechargeSpeed
                yield self.env.timeout(1)

            # if the recharge process is not interrupted
            print('Fully charged...')
            print('-' * 30)

        # else -- just finish then
        except simpy.Interrupt:
            pass

class Driver(object):
    '''
        Driver class
    '''
    def __init__(self, env):
        '''
            The main constructor of the class
        '''
        self.env = env

    def drive(self, car, timeToFullRecharge):
        '''
            Method to control how long the recharging
            is allow to last

            @param car -- pointer to the car
            @timeToFullRecharge -- minutes needed to full
                                   recharge
        '''
        # decide how long to allow the car to recharge
        interruptTime = np.random.randint(50, 120)

        # if more than the time needed to full recharge
        # wait till the full recharge, otherwise interrupt
        # the recharge process earlier
        yield self.env.timeout(int(np.min(
            [interruptTime, timeToFullRecharge])))

        if interruptTime < timeToFullRecharge:
            car.action.interrupt()


if __name__ == '__main__':
    # what is the simulation horizon (in minutes)
    SIM_TIME = 10 * 60 * 60 # 10 hours

    # create the environment
    env = simpy.Environment()

    # create recharge stations
    rechargeStations = RechargeStation \
        .generateRechargeStations(SIM_TIME)

    # create the driver and the car
    driver = Driver(env)
    car = Car(env, driver, rechargeStations)

    # print the header
    print()
    print('-' * 30)
    print('Time\tBatt.\tDist.')
    print('-' * 30)

    # and run the simulation
    env.run(until = SIM_TIME)
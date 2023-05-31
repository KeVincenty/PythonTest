# Design an Underground System !!

# Suppose you are a software engineer in a world-wide software developing company and currently you are developing a software for underground railway systems in the major cities around the world (e.g. Tokyo Metro, Shanghai Metro). This software aims to keep track of the time that passengers spend between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

# According to the requirement of metro companies, this software need to have three basic functions:

#   1) checkIn(id: int, stationName: str, t: int), this function takes `id` (int), `stationName` (str), and `t` (int) as inputs, and it marks that a passenger with an ID equal to `id` checks in at the station `stationName` at time `t`. e.g when checkIn(23, 'Tokyo', 10) is called, it means that a passenger whose id is 23 checked in at "Tokyo" station at time 10. Note that a passenger can only check into one station at a time.

#   2) checkOut(id: int, stationName: str, t: int), this function takes `id` (int), `stationName` (str), and `t` (int) as inputs, and it marks that a passenger with an ID equal to `id` checks out at the station `stationName` at time `t`. e.g when checkIn(33, 'Shibuya', 19) is called, it means that a passenger whose id is 33 checked out at "Shibuya" station at time 19. Note that a passenger can only check out after he has checked in somewhere before.

#   3) getAverageTime(startStation: str, endStation: str), this function takes `startStation` (str), `endStation` (str) as inputs, and it should return the average time it takes to travel from `startStation` to `endStation`. The average time is computed from all the previous traveling time from `startStation` to `endStation` that happened directly, meaning a check in at `startStation` followed by a check out from `endStation`. The time it takes to travel from `startStation` to `endStation` may be different from the time it takes to travel from `endStation` to `startStation`. You may assume that there will be at least one passenger that has traveled from `startStation` to `endStation` before getAverageTime(startStation, endStation) is called.

# To help you better understand these functions, below is an example of calling these functions in order:

# checkIn(45, "Ikebukuro", 3); // Passenger 45 checks in at "Ikebukuro" at time 3
# checkIn(32, "Ueno", 8); // Passenger 32 checks in at "Ueno" at time 8
# checkIn(27, "Ikebukuro", 10); // Passenger 27 checks in at "Ikebukuro" at time 10
# checkOut(45, "Shibuya", 15); // Passenger 45 checks out at "Shibuya" at time 15. Because he checked in at "Ikebukuro" at time 3, so the time this trip "Ikebukuro" -> "Shibuya" costs equals to 15-3 = 12.
# checkOut(27, "Shibuya", 20); // Passenger 27 checks out at "Shibuya" at time 20. Similar to the above, the trip "Ikebukuro" -> "Shibuya" costs 20-10 = 10
# checkOut(32, "Shinjuku", 22); // Passenger 32 checks out at "Shinjuku" at time 22. "Ueno" -> "Shinjuku" in 22-8 = 14
# getAverageTime("Ueno", "Shinjuku"); // this should return 14.00000. There has been only one trip "Ueno" -> "Shinjuku", (14) / 1 = 14
# getAverageTime("Ikebukuro", "Shibuya"); // this should return 11.00000. There have been two trips "Ikebukuro" -> "Shibuya", (10 + 12) / 2 = 11
# checkIn(10, "Ikebukuro", 24); // Passenger 10 checks in at "Ikebukuro" at time 24
# getAverageTime("Ikebukuro", "Shibuya"); // return 11.00000, no new trip is made
# checkOut(10, "Shibuya", 38);  // Passenger 10 checks out at "Shibuya" at time 38. "Ikebukuro" -> "Shibuya" in 38-24 = 14
# getAverageTime("Ikebukuro", "Shibuya"); // return 12.00000. Now there are three trips "Ikebukuro" -> "Shibuya", (10 + 12 + 14) / 3 = 12

# To implement this software, the best practice is to create a class with these three functions (methods). Below is a structure of the class for this task, follow the instruction and try to implement it step by step!

class UndergroundSystem:
    def __init__(self):
        # Here you need to initiate some class attributes based on the variables you need to use afterwards
        # Think about what kind of data structures (list? dictionary? tuple? set? ...) you should use to keep records of passengers' id, their check-in/check-out stations and time and the time of trips from one station to another.
        # Here I would recommend you using dictionary. Because the passengers' id, station names, etc., are all discrete values instead of continuous values. So a list whose indexing are continous numbers can not meet our needs. Besides, you may want to use nested dictionary because there are more than one kinds of keys (passengers' id and station names)

        pass # delete this line after you complete the codes

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # This function marks that a passenger with an ID equal to `id` checks in at the station `stationName` at time `t`. Basically, this means that you should record these new information into the data structures you initiate in __init__ .

        pass # delete this line after you complete the codes

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # This function marks that a passenger with an ID equal to `id` checks out at the station `stationName` at time `t`. Similarly, you should record these new information into the data structures you initiate in __init__ . Addtionally, when a passenger checks out at a station, it means that you can already calculate the time of the trip he has completed. And you may also want to record the time of the trip into a data structure so that you can recall them once you want to calculte the average time.
        
        pass # delete this line after you complete the codes

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # This function should return the average time it takes to travel from `startStation` to `endStation`. 

        # Digress from the topic at hand, This kind of action is usually called a "query", which it aims to search or ask for some information instead of adding to or editing the existing information in this class. Once the function gets a "query" (here the "query" is (startStation, endStation) ), it will try to find "key"s in its data structures, and extract/calculate the corresponding "value" (here the "value" is the average time between startStation and endStation). You will meet "query", "key", "value" (or "q, k, v" in abbreviation) in the famous Transformer paper (https://arxiv.org/abs/1706.03762). Although they are used very differently, they actually share the same thoughts behind: you find the right "key" based on the "query", and then you extract/compute the "value" corresponding to the "key".

        pass # delete this line after you complete the codes


# Below are some unit test codes, do not mind them. Just run the python file after you finished the codes then you will see whether your software succeed in three cities around the world!
############################################################################################################

import unittest

class TestUndergroundSystem(unittest.TestCase):
    def __init__(self, func_list, input_args, output_list, testName = 'run_test', testId = 'test') -> None:
        super(TestUndergroundSystem, self).__init__(testName)
        self.func_list = func_list
        self.input_args = input_args
        self.output_list = output_list
        self.testId = testId

    def setUp(self):
        self.ugsys = UndergroundSystem()

    def tearDown(self) -> None:
        return super().tearDown()
    
    def run_test(self):
        for i in range(len(self.func_list)):
            f = getattr(self.ugsys, self.func_list[i])
            if self.output_list[i]:
                self.assertAlmostEqual(f(*self.input_args[i]), self.output_list[i], 5, 'Test in {} failed!'.format(self.testId))
            else:
                self.assertEqual(f(*self.input_args[i]), self.output_list[i], 'Test in {} failed!'.format(self.testId))
        print("\n You succeed in {}! Congratulations!".format(self.testId))
        

suite = unittest.TestSuite()

tokyo = [["checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"], [[45,"Ueno",3],[32,"Shibuya",8],[27,"Ueno",10],[45,"Shinjuku",15],[27,"Shinjuku",20],[32,"Shinagawa",22],["Shibuya","Shinagawa"],["Ueno","Shinjuku"],[10,"Ueno",24],["Ueno","Shinjuku"],[10,"Shinjuku",38],["Ueno","Shinjuku"]], [None,None,None,None,None,None,14.00000,11.00000,None,11.00000,None,12.00000]]

london = [["checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"], [[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]], [None,None,5.00000,None,None,5.50000,None,None,6.66667]]

shanghai = [["checkIn","checkIn","checkOut","checkOut","checkIn","checkIn","getAverageTime","getAverageTime","checkOut","getAverageTime","checkOut","getAverageTime"], [[1,"Lujiazui",3],[2,"Xujiahui",8],[1,"Xujiahui",10],[2,"Lujiazui",15],[1,"Xujiahui",20],[2,"Lujiazui",22],["Lujiazui","Xujiahui"],["Xujiahui","Lujiazui"],[1,"Lujiazui",24],["Xujiahui","Lujiazui"],[2,"Xujiahui",38],["Lujiazui","Xujiahui"]], [None,None,None,None,None,None,7.00000,7.00000,None,5.50000,None,11.50000]]

suite.addTest(TestUndergroundSystem(*tokyo, testId = 'Tokyo'))
suite.addTest(TestUndergroundSystem(*london, testId = 'London'))
suite.addTest(TestUndergroundSystem(*shanghai, testId = 'Shanghai'))

unittest.TextTestRunner().run(suite)
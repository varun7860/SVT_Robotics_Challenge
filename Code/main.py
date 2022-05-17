from urllib import robotparser
import requests
import json
import math
import numpy as np
import random

class SvtBot(object):
    def __init__(self):
        
        #API Endpoint Urls
        self.API_URL_1 = "https://60c8ed887dafc90017ffbd56.mockapi.io/robots"
        self.API_URL_2 = "https://svtrobotics.free.beeceptor.com/robots"

        #Get API Data using HTTP Request
        try:
           self.API_DATA = requests.get(self.API_URL_1)
        except Exception as e:
           print(e)
           self.API_DATA = requests.get(self.API_URL_2)
        finally:
            if self.API_DATA.status_code == 200:
                print("Data Extracted Successfully")

            else:
                print("Error : Issue with Data Extraction")

        self.API_DATA = self.API_DATA.json()

        #Robot data
        self.id = None
        self.battery_level = None
        self.distance_to_goal = None

    @staticmethod
    def calculate_distance(x1:float,x2:float,y1:float,y2:float)->float:
        distance = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
        return distance

    @staticmethod
    def get_random_payload():
        x = random.randrange(1,100,2)
        y = random.randrange(1,100,2)
        payload_id = str(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

        return x,y,payload_id

    @staticmethod
    def find_highest_battery_level_robot(distances:list,battery_levels:list)-> int:
         batteries = []
         index = []
         print(distances)

         for k in range(len(distances)):
            if distances[k] <= 10.0:
                batteries.append(battery_levels[k])
                index.append(k)

            else:
                pass

         print(batteries)
         return index[np.argmax(batteries)]
                
    def remove_zero_battery_level(self):
        counter = 0
        for p in range(len(self.API_DATA)):
            robot = self.API_DATA[p]
            battery = robot.get('batteryLevel')
            if battery == 0:
                self.API_DATA.pop(p)
                counter+=1
            if p == len(self.API_DATA)-counter:
                break
                

    def get_robot_params(self,index):
        robot = self.API_DATA[index]
        id = robot.get('robotId')
        battery = robot.get('batteryLevel')
        y = robot.get('y')
        x = robot.get('x')
        return id,battery,y,x

    def find_robot(self,x_load:float,y_load:float,load_id:str)-> dict:

        distance = []
        battery_levels = []
        ids = []
        counter = 0

        #Remove Zero Battery Level Robots
        self.remove_zero_battery_level()

        for i in range(len(self.API_DATA)):
            '''
            Extract robot params (x,y,id,battery)
            distance formula
            append distance
            append battery
            append ids
            '''
            id,battery,y1,x1 = self.get_robot_params(i)
            d = round(self.calculate_distance(x1,x_load,y1,y_load),2)
            distance.append(d)
            battery_levels.append(battery)
            ids.append(id)

        '''
        Find the robot which is to the minimum distance
        if many robots lie in same range then check the battery levels
        '''

        for j in range(len(distance)):

            if distance[j]<=10:

                if counter > 1:
                   robot_num = self.find_highest_battery_level_robot(distance,battery_levels)
                   break

                counter += 1

            else:
                robot_num = np.argmin(distance)

        ideal_robot = self.API_DATA[robot_num]
        id = ideal_robot.get('robotId')
        d_to_goal = distance[robot_num]
        battery_level = ideal_robot.get('batteryLevel')

        print({'robotId': id,'distanceToGoal': d_to_goal,'batteryLevel': battery_level})

        return {'robotId': id,'distanceToGoal': d_to_goal,'batteryLevel': battery_level}


def main():
    #create the SvtBot Object
    bot = SvtBot()

    #Get a random payload config
    x,y,payload_id = bot.get_random_payload()

    #Find the ideal robot that can pick up the payload
    robot = bot.find_robot(x,y,payload_id)

    #Display the output
    print("The ideal robot to pick the payload:",robot)

    
if __name__ == '__main__':
    main()

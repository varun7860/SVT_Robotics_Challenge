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

        #Get API Data
        try:
           self.API_DATA = requests.get(self.API_URL_1)
        except:
           print("API 1 Failed")

        self.API_DATA = self.API_DATA.json()
        robot_1 = self.API_DATA[0]
        id = robot_1.get('robotId')
        print(id)

        #Robot data
        self.id = None
        self.battery_level = None
        self.distance_to_goal = None

    @staticmethod
    def calculate_distance(x1:float,x2:float,y1:float,y2:float)->float:
        distance = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
        return distance

    def get_robot_params(self,index):
        robot = self.API_DATA[index]
        id = robot.get('robotId')
        battery = robot.get('batteryLevel')
        y = robot.get('y')
        x = robot.get('x')
        return id,battery,y,x

    def get_random_payload():
        x = random()
        y = random()
        payload_id = str(random())

        return x,y,payload_id

    def get_find_robot(self,x_load:float,y_load:float,load_id:str)-> dict:
        distance = []
        battery_levels = []
        ids = []
        counter = 0

        for i in range(len(self.API_DATA)):
            '''
            Extract robot params (x,y,id,battery)
            distance formula
            append distance
            append battery
            append ids
            '''
            id,battery,y1,x1 = self.get_robot_params(i)
            d = self.calculate_distance(x1,x_load,y1,y_load)
            distance.append(d)
            battery_levels.append(battery)
            ids.append(id)

        '''
        Find the robot which is to the minimum distance
        if many robots lie in same range then check the battery levels
        '''

        for j in range(len(distance)):

            if counter > 1:
                break

            if distance[j]<=10:
                counter += 1

        robot_num = np.argmax(battery_levels)
        ideal_robot = self.API_DATA[robot_num]
        id = ideal_robot.get('robotId')
        d_to_goal = distance[robot_num]
        battery_level = ideal_robot.get('batteryLevel')

        return {'robotId': id,'distanceToGoal': d_to_goal,'batteryLevel': battery_level}


def main():
    #create the SvtBot Object
    bot = SvtBot()

    #Get a random payload config
    #x,y,payload_id = bot.get_random_payload()

    #Find the ideal robot that can pick up the payload
    #robot_id,dis_to_goal,battery_level = bot.get_robot_id(x,y,payload_id)

    #Display the output
    #print("The ideal robot to pick the payload:",robot_id,dis_to_goal,battery_level)

    

if __name__ == '__main__':
    main()

# SVT_Robotics_Challenge

Problem Statement: Make a function that takes 3 input arguments loadId,X,Y of the load and returns the best robot that can pick up that load in the following format:
```
{
    robotId: 58,
    distanceToGoal: 49.9, //Indicates how far the robot is from the load which needs to be moved.
    batteryLevel: 30 //Indicates current battery level of the robot.
}
```
## Installations
I have used python language for coding the functions.I have also used additional libraries that can perform HTTP Request, Performing mathematical functions and performing array operations. Below are the instructions to install those libraries:

1.Numpy Library - To Perform Array Operations
- ```pip3 install numpy```

2.Requests Library - To perform HTTP Request
- ```pip3 install requests```

3.Math Library - To perform Math Operations
- ```pip3 install python-math```

4.Random Library - To Randomly Generate Load id and Its position
- ```pip3 install random2```

5.Json Library - Loading the .json file data locally when there is no internet.
- This Library is already there in python.

I have made a requirements.txt file which you can use to install all these commands with one go like this
- ```pip3 install -r requirements.txt```

## My Solution and Documentation
For my solution I made a class called SVTBot that contains all the necessary functions to find the best robot that can pick up load. Given below is a overview of all the functions that I have made within SVTBot Class:

1. get_random_load(args:None): This function generates a random load and returns its id and position(x,y). x,y and id are generated randomly using the random library in python.

2. remove_zero_battery_level(args:None): This function removes the robots with zero battery level as they are of no use to pick up and transport the load without a battery. It reads API data and then finds out the robot with zero battery level.

3. get_robot_params(args:None): This function finds the robot's id,battery level, its x and y coordinates and then returns them. It reads API data to get these parameters of the robot.

4. calculate_distance(x1,x2,y1,y2): This function calculates the distance between the robot and load.Here (x1,y1) is the robot's position and (x2,y2) is the load's position. It calculates the distance using distance formula sqrt((x2-x1)^2 + (y2-y1)^2 and then returns it.

5. find_highest_battery_level_robot(distances,batteries): This function calculates the highest battery level robot when more than 1 robot lies within 10 distance units. It takes list of distances and battery leves as an argument and returns the index of robot which has highest battery level.

6. find_robot(x,y,id): This function takes the load (x,y,id) as an argument and returns the robot (id,distance_to_goal,battery level) thats best to transport the load.(closest to load and has decent battery level). If there are more than 1 robot within 10 distance units it returns the robot with highest battery level.

## Approach
1. I first get the data from API Endpoint using HTTP Request.
2. After getting the data the program remove all the robots which have zero battery levels.
3. After that the program generates random load configuration and feeds it to the function which find the robot for transporting that load.
4. The function calculates the distance of each robot from the load and then with help of that distance and battery levels finds the best robot that can transport the load.
5. Finally the output is displayed as per the requirements.

## Instructions for Running and Testing the Program
The repository contains a folder called code which has the main function program. Other files in the repository are README.md which contains the instructions to run the program and testing it. Following is the structure of the repository:

SVT_Robotics Challege
- Code
- README.md

To run the program go to the folder where the python program is saved and then run the python file. Given below are the steps to execute the program:

1. ```cd ~/SVT_Robotics_Challenge/Code```
2. ```python3 main.py```

To test the program go the Unit_Tests Folder and run the program unit_tests.py. The unit test program checks for python version, installations and the distance calculation function. If all goes correct you should't see any error and program should execute with no output. If something is missing assertion error will be displayed in the terminal.

1. ```cd ~/SVT_Robotics_Challenge/Unit_Tests```
2. ```python3 unit_tests.py```

## What Next?



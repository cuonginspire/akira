import pyttsx3

robot_brain = "Hi CT, you are so handsome"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

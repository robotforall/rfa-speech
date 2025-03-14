#!/usr/bin/env python
#
# RobotForAll www.robotforall.net
#
# Authors: Jeffrey Tan <i@jeffreytan.org>

import rospy
from std_msgs.msg import String
from gtts import gTTS
import os

def callback(data):
    rospy.loginfo("Input: %s", data.data)

    text = data.data
    tts = gTTS(text, lang="en-US")
    
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
    os.remove("speech.mp3")
    
def googletts():
    rospy.init_node('googletts', anonymous=True)

    rospy.Subscriber("input", String, callback)
    print(">>> Waiting for input text...")
    rospy.spin()

if __name__ == '__main__':
    googletts()
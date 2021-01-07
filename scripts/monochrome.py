#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def gray(msg):
    try:
        bridge = CvBridge()
        orig = bridge.imgmsg_to_cv2(msg, "bgr8")
        img = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
        gray_img = bridge.cv2_to_imgmsg(img, "mono8")
        pub = rospy.Publisher('image_monochrome', Image, queue_size=10)
        pub.publish(gray_img)
                                                  
    except Exception as err:
        print(err)

def start_node():
    rospy.init_node('img_mono')
    sub = rospy.Subscriber('/cv_camera/image_raw', Image, gray)
    rospy.spin()

if __name__ == '__main__':
    try:
        start_node()

    except rospy.ROSInterruptException:
        pass  

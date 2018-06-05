#!/usr/bin/env python

# marker_calibration.py: Code to publish calibration matrix
# Author: Nishanth Koganti
# Date: 2016/06/15
# Source: https://github.com/osrf/baxter_demos/blob/master/scripts/get_ar_calib.py

import tf
import yaml
import math
import rospy
import numpy as np
from math import pi

def main():
    # initialize ros node
    rospy.init_node('publish_calibration')

    # parameter initialization
    rot = [0.0,0.0,1.0,0.0]
    child = '/world'
    trans = [0.0,0.0,1.0]
    parent = '/iiwa_link_0'

    # create tf listener and broadcaster
    tf_broadcaster = tf.TransformBroadcaster()

    # loop rate
    rate = rospy.Rate(100)

    # Publish transform and marker
    while not rospy.is_shutdown():
        tf_broadcaster.sendTransform(trans, rot, rospy.Time.now(), child, parent)
        print('Success!')
        rate.sleep()

if __name__=='__main__':
    main()

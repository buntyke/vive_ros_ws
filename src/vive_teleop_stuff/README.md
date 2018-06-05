# Vive teleop stuff

## Run node
The node you want to run is [scripts/vive_tf_and_joy.py](scripts/vive_tf_and_joy.py) which is nicely prepared in a launchfile for you.
```bash
roslaunch htc_vive_teleop_stuff htc_vive_tf_and_joy.launch
```

You'll see plenty of output (that's the OpenVR initializing) and you may need to touch your controllers to get it started. Then you'll see the output: `Running!`

You'll find the topics:
```
Topic                   Type                Rate
/tf                     tf2_msgs/TFMessage  250Hz
/vive_left              sensor_msgs/Joy     On Event
/vive_right             sensor_msgs/Joy     On Event
/vive_left_vibration    std_msgs/Float64    Listening
/vive_right_vibration   std_msgs/Float64    Listening
```

The TF tree looks like (there is only one lighthouse because I only had one plugged in):
![tf_tree.png](tf_tree.png)

The `sensor_msgs/Joy` topics are as:
```
header: 
  seq: 541
  stamp: 
    secs: 1508649347
    nsecs: 147578954
# which controller
  frame_id: left_controller
# Trigger, Trackpad X, Trackpad Y
axes: [0.0, 0.0, 0.0]
# Trigger, Trackpad touched, Trackpad pressed, Menu, Gripper
buttons: [0, 0, 0, 0, 0]
```



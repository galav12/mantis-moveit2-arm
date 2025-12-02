# Mantis Moveit2 Robotic Arm

###Instructions
- Follow [Getting Started](https://moveit.picknik.ai/main/doc/tutorials/getting_started/getting_started.html) to set up moveit2
- Move and build colcon workspace
```bash
cd ~/ws_moveit/src
git clone https://github.com/galav12/mantis-moveit2-arm.git
```
- Install missing packages
```bash
rosdep install --from-paths . --ignore-src --rosdistro $ROS_DISTRO
```
- Build the workspace
```bash
cd ~/ws_moveit
colcon build
```
- Start by launching initial launch file
```bash
ros2 launch mantis-moveit2-arm moveit_project.launch.py
```
- Launch pick and place movement node
```bash
ros2 launch mantis-moveit2-arm pick_and_place_project.launch.py
```
cmake_minimum_required(VERSION 3.0.2)
project(otomo-webserver)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  std_msgs
  sensor_msgs
  otomo_msgs
  rosbridge_server
  roslaunch
)

catkin_package()

install(
  PROGRAMS
    scripts/otomo_webserver
    scripts/heartbeat
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(
  DIRECTORY
    scripts/templates
    scripts/static
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(
  DIRECTORY
    launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

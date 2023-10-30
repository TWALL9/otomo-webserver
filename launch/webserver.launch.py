# my_python_node_launch.py

import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    node_name = 'otomo_webserver'
    package_name = 'otomo_webserver'
    # Declare launch arguments
    # my_node_name = DeclareLaunchArgument(node_name, description='Name of the Python node')
    # my_node_package = DeclareLaunchArgument(package_name, description='Name of the package containing the Python node')

    rosbridge_node = Node(
        package='rosbridge_server',
        executable='rosbridge_websocket',
        name='rosbridge_node',
        output='screen',
    )
    
    webserver_node = Node(
        package=package_name,
        executable=node_name,
        name=node_name,
        output='screen',
    )

    return LaunchDescription([
        rosbridge_node,
        webserver_node,
    ])

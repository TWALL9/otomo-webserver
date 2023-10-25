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
    
    # Define the Python node to launch
    my_python_node = Node(
        package=package_name,
        executable=node_name,
        name=node_name,
        output='screen',
    )

    # Create a LaunchDescription and add the actions
    # return LaunchDescription([
    #     my_node_name,
    #     my_node_package,
    #     my_python_node,
    # ])
    return LaunchDescription([
        my_python_node,
    ])

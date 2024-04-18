import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    param_file = os.path.join(get_package_share_directory('abu_framework'), 'config/main_params.yaml')

    return LaunchDescription([

        Node(
            package="abu_framework",
            executable="main_node.py",
            parameters=[param_file],
        )
    ])

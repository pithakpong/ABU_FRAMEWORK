from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import launch
def generate_launch_description():
	dir = get_package_share_directory('mecanum_controller')
	included_launch = launch.actions.IncludeLaunchDescription(
	launch.launch_description_sources.PythonLaunchDescriptionSource(
	dir + '/launch/mecanum_launch.py'))
	return LaunchDescription([
		Node(
			package='abu_framework',
			executable="Tsl_node.py"),
		Node(
			package='abu_framework',
			executable='mega_interface.py'),
		Node(
			package='abu_framework',
			executable='AreaPub.py'),
		Node(
			package='abu_framework',
			executable='detect_server.py'),
		included_launch,
	])

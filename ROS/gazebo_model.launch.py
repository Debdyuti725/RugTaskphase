from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node 
import os 
import xacro


def generate_launch_description():
     
    robotXacroName='mobile_robot'

    namePackage='mobile_robot_controller'

    model_relative_path='model/robot.xacro'

    world_relative_path="model/empty_world.world"

    Model_path=os.path.join(get_package_share_directory(namePackage),model_relative_path)

    pathWorld=os.path.join(get_package_share_directory(namePackage),world_relative_path)

    robotDescription=xacro.process_file(Model_path).toxml()

    gazebo_rosPackageLaunch=PythonLaunchDescriptionSource(os.path.join(get_package_share_directory('gazebo_ros'),'launch','gazebo.launch.py'))
    
    gazeboLaunch=IncludeLaunchDescription(gazebo_rosPackageLaunch,launch_arguments={'world':pathWorld}.items())
    
    spawnModelNode=Node(package='gazebo_ros',
                        executable='spawn_entity.py', 
                        arguments=['-topic','robot_description','-entity',robotXacroName],
                        output='screen')

    nodeRobotStatePublisher=Node(package='robot_state_publisher',
                                 executable='robot_state_publisher',
                                 output="screen",
                                 parameters=[{'robot_description':robotDescription,
                                             'use_sim_time':True}])
    
    
    
    LaunchDescriptionObject=LaunchDescription()

    LaunchDescriptionObject.add_action(gazeboLaunch)
    
    LaunchDescriptionObject.add_action(spawnModelNode)

    LaunchDescriptionObject.add_action(nodeRobotStatePublisher)


    return LaunchDescriptionObject
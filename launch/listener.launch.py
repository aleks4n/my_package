from launch import LaunchDescription
from launch_ros.actions import node
def generate_launch_desciption():
        return LaunchDescription([
            Node(
              package = 'demo_nodes_py',
              executable = 'listener'
            )   

        ])
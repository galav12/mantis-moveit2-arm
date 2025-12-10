from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("moveit_resources_panda").to_dict()

    scenario_arg = DeclareLaunchArgument(
        "scenario",
        default_value="triangle",
        description="Pick-and-place scenario: triangle, stack, cylinder, custom"
    )

    scenario = LaunchConfiguration("scenario")

    pick_place_project = Node(
        package="moveit_project",
        executable="moveit_node",
        output="screen",
        emulate_tty=True,
        parameters=[moveit_config],
        arguments=[scenario],
    )

    # return LaunchDescription([pick_place_project])
    return LaunchDescription([scenario_arg, pick_place_project])
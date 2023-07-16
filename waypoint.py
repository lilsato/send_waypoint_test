#! /usr/bin/env python3
import time

import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from rclpy.clock import Clock, ClockType
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped


class SampleActionClient(Node):
    def __init__(self):
        super().__init__('send_waypoint_action_client')

        self.follow_waypoints_client = ActionClient(self, FollowWaypoints, 'FollowWaypoints')

    def send_goal(self, poses):
        print("Waiting for 'FollowWaypoints' action server")
        while not self.follow_waypoints_client.wait_for_server(timeout_sec=1.0):
            print("'FollowWaypoints' action server not available, waiting...")
        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = poses
        self.follow_waypoints_client.send_goal_async(goal_msg)

def main(args=None):
    goal_poses = []
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    #goal_pose.header.stamp = 630
    goal_pose.pose.position.x = 1.3
    goal_pose.pose.position.y = 6.0
    goal_pose.pose.position.z = 0.0
    goal_pose.pose.orientation.x = 0.0
    goal_pose.pose.orientation.y = 0.0
    goal_pose.pose.orientation.z = 0.23
    goal_pose.pose.orientation.w = 0.97
    goal_poses.append(goal_pose)

    rclpy.init(args=args)
    action_client = SampleActionClient()

    action_client.send_goal(goal_poses)
    rclpy.spin(node)

if __name__ == '__main__':
    main()
"""
This file claims the ALMemory Keys used in the project.
The keys store the torque of part of the sensors on the robot.
"""

UPPERBODY_TORQUE_KEY = {
    # Head
    "HeadYaw": "Motion/Torque/Sensor/HeadYaw",
    "HeadPitch": "Motion/Torque/Sensor/HeadPitch",

    # Wrist
    "RWristYaw": "Motion/Torque/Sensor/RWristYaw",
    "LWristYaw": "Motion/Torque/Sensor/LWristYaw",

    # Elbow
    "RElbowYaw": "Motion/Torque/Sensor/RElbowYaw",
    "LElbowYaw": "Motion/Torque/Sensor/LElbowYaw",
    "RElbowRoll": "Motion/Torque/Sensor/RElbowRoll",
    "LElbowRoll": "Motion/Torque/Sensor/LElbowRoll",

    # Shoulder
    "RShoulderRoll": "Motion/Torque/Sensor/RShoulderRoll",
    "LShoulderRoll": "Motion/Torque/Sensor/LShoulderRoll",
    "RShoulderPitch": "Motion/Torque/Sensor/RShoulderPitch",
    "LShoulderPitch": "Motion/Torque/Sensor/LShoulderPitch"
}

LEG_TORQUE_KEY = {

    # Ankle
    "RAnkleRoll": "Motion/Torque/Sensor/RAnkleRoll",
    "LAnkleRoll": "Motion/Torque/Sensor/LAnkleRoll",
    "RAnklePitch": "Motion/Torque/Sensor/RAnklePitch",
    "LAnklePitch": "Motion/Torque/Sensor/LAnklePitch",

    # Knee
    "RKneePitch": "Motion/Torque/Sensor/RKneePitch",
    "LKneePitch": "Motion/Torque/Sensor/LKneePitch",

    # Hip
    "RHipRoll": "Motion/Torque/Sensor/RHipRoll",
    "LHipRoll": "Motion/Torque/Sensor/LHipRoll",
    "RHipPitch": "Motion/Torque/Sensor/RHipPitch",
    "LHipPitch": "Motion/Torque/Sensor/LHipPitch",
    "RHipYawPitch": "Motion/Torque/Sensor/RHipYawPitch",
    "LHipYawPitch": "Motion/Torque/Sensor/LHipYawPitch"
}


ALMEMORY_TORQUE_THRESHOLD = {
    "RShoulderRoll": 0.4,
    "LShoulderRoll": 0.4,
    "RShoulderPitch": 0.35,
    "LShoulderPitch": 0.35,
    "RElbowRoll": 0.2,
    "LElbowRoll": 0.2,
    "RElbowYaw": 0.5,
    "LElbowYaw": 0.5,
    "HeadYaw": 0,
    "HeadPitch": 0,
    "RWristYaw": 0,
    "LWristYaw": 0,

}


UPPERBODY_POSITION_KEY = {
    # Wrist
    "LWristYaw": "Motion/Position/Sensor/LWristYaw",
    "RWristYaw": "Motion/Position/Sensor/RWristYaw",

    # Elbow
    "LElbowRoll": "Motion/Position/Sensor/LElbowRoll",
    "LElbowYaw": "Motion/Position/Sensor/LElbowYaw",
    "RElbowRoll": "Motion/Position/Sensor/RElbowRoll",
    "RElbowYaw": "Motion/Position/Sensor/RElbowYaw",

    # Shoulder
    "RShoulderRoll": "Motion/Position/Sensor/RShoulderRoll",
    "RShoulderPitch": "Motion/Position/Sensor/RShoulderPitch",
    "LShoulderRoll": "Motion/Position/Sensor/LShoulderRoll",
    "LShoulderPitch": "Motion/Position/Sensor/LShoulderPitch",

    # Head
    "HeadPitch": "Motion/Position/Sensor/HeadPitch",
    "HeadYaw": "Motion/Position/Sensor/HeadYaw"
}


LEG_POSITION_KEY = {
    # Ankle
    "RAnkleRoll": "Motion/Position/Sensor/RAnkleRoll",
    "LAnkleRoll": "Motion/Position/Sensor/LAnkleRoll",
    "RAnklePitch": "Motion/Position/Sensor/RAnklePitch",
    "LAnklePitch": "Motion/Position/Sensor/LAnklePitch",

    # Knee
    "RKneePitch": "Motion/Position/Sensor/RKneePitch",
    "LKneePitch": "Motion/Position/Sensor/LKneePitch",

    # Hip
    "RHipPitch": "Motion/Position/Sensor/RHipPitch",
    "RHipYawPitch": "Motion/Position/Sensor/RHipYawPitch",
    "LHipPitch": "Motion/Position/Sensor/LHipPitch",
    "RHipRoll": "Motion/Position/Sensor/RHipRoll",
    "LHipRoll": "Motion/Position/Sensor/LHipRoll",
    "LHipYawPitch": "Motion/Position/Sensor/LHipYawPitch"
}


# MEMORY_LFOOT_NAMES is the list of ALMemory values names you want to save.
# The value will be 1.0 when the bumper been touch
LEG_FEET_SENSOR = {
    "LFootR": "Device/SubDeviceList/LFoot/Bumper/Right/Sensor/Value",
    "LFootL": "Device/SubDeviceList/LFoot/Bumper/Left/Sensor/Value",
    "RFootR": "Device/SubDeviceList/RFoot/Bumper/Right/Sensor/Value",
    "RFootL": "Device/SubDeviceList/RFoot/Bumper/Left/Sensor/Value"
}

BUMPER = {
    "LBumper": "LeftBumperPressed",
    "RBumper": "RightBumperPressed",
}

HAND_BACK_TOUCHED = {
    "RHandBack": "HandRightBackTouched",
    "LHandBack": "HandLeftBackTouched"
}

HEAD_TACTIL_TOUCHED = {
    "FrontTactil": "FrontTactilTouched",
    "MiddleTactil": "MiddleTactilTouched",
    "RearTactil": "RearTactilTouched"
}
import csv
import os
import sys

# Headers of csv file
fieldnames = ["RShoulderRoll", "LShoulderRoll", "RShoulderPitch", "LShoulderPitch",
              "RElbowRoll", "LElbowRoll", "RElbowYaw", "LElbowYaw", "HeadYaw", "HeadPitch",
              "RWristYaw", "LWristYaw"]


def save_result(results, path):
    """
    Append the results at the end of the exsisting CSV file.
    """
    try:
        with open(path, "ab") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for result in results:
                writer.writerow(result)
    except Exception:
        return False
    else:
        return True


def create_csv(path, filename):
    """
    Create a new CSV file with the headers listed above.
    """
    path = os.path.join(path, filename)
    with open(path, 'wb+') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    return path


def load_result(path):
    """
    Load results from CSV file.
    """
    results = {}
    results["RShoulderRoll"] = []
    results["LShoulderRoll"] = []
    results["RShoulderPitch"] = []
    results["LShoulderPitch"] = []
    results["RElbowRoll"] = []
    results["LElbowRoll"] = []
    results["RElbowYaw"] = []
    results["LElbowYaw"] = []
    results["HeadYaw"] = []
    results["HeadPitch"] = []
    results["RWristYaw"] = []
    results["LWristYaw"] = []
    results["HeadYaw"] = []
    results["HeadPitch"] = []
    results["RWristYaw"] = []
    results["LWristYaw"] = []
    #results["RAnkleRoll"] = []
    #results["LAnkleRoll"] = []
    #results["RAnklePitch"] = []
    #results["LAnklePitch"] = []
    #results["RKneePitch"] = []
    #results["LKneePitch"] = []
    #results["RHipRoll"] = []
    #results["LHipRoll"] = []
    #results["RHipPitch"] = []
    #results["LHipPitch"] = []
    #results["RHipYawPitch"] = []
    #results["LHipYawPitch"] = []

    with open(path, "rb") as csvfile:
        print(path)
        reader = csv.DictReader(csvfile)
        length = 0
        for row in reader:
            length += 1
            for fieldname in fieldnames:
                #print(row[fieldname])
                #print(type(float(row[fieldname])))
                results[fieldname].append(float(row[fieldname]))
    return results, length


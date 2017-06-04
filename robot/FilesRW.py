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

def load_result_demo(path):
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
    with open(path, "rb") as csvfile:
        print(path)
        reader = csv.DictReader(csvfile)
        length = 0
        for row in reader:
            length += 1
            for fieldname in fieldnames:
                results[fieldname].append(float(row[fieldname]))
    return results, length


def load_result(list):
    """
    Load results from CSV file.
    """
    results1 = {}

    results1["RShoulderRoll"] = []
    results1["LShoulderRoll"] = []
    results1["RShoulderPitch"] = []
    results1["LShoulderPitch"] = []
    results1["RElbowRoll"] = []
    results1["LElbowRoll"] = []
    results1["RElbowYaw"] = []
    results1["LElbowYaw"] = []
    results1["HeadYaw"] = []
    results1["HeadPitch"] = []
    results1["RWristYaw"] = []
    results1["LWristYaw"] = []
    results1["HeadYaw"] = []
    results1["HeadPitch"] = []
    results1["RWristYaw"] = []
    results1["LWristYaw"] = []
    length = 0

    for line in list:
        print line
        print type(line)
        length += 1
        for fieldname in fieldnames:
            results1[fieldname].append(float(line[fieldname]))


    return results1, length


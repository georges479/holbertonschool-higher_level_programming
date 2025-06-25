#!/usr/bin/python3
import json

"""Create a basic serialization module"""


def serialize_and_save_to_file(data, filename):
    """Function for save data"""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Function for deserialize data"""
    with open(filename, 'r') as file:
        return json.load(file)

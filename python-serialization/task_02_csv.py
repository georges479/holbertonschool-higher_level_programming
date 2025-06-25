#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(file_csv):
    try:
        with open(file_csv, 'r') as cfile:
            csv_read = csv.DictReader(cfile)
            data = [row for row in csv_read]

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)

        return True
    except (FileNotFoundError, IOError) as e:
        print(f"Error: {e}")
        return False

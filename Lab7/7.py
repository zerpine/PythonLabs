import csv
import json
import os


def json_to_csv(json_name):

    csv_name = os.path.splitext(json_name)[0] + '.csv'

    with open(json_name, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    main_key = list(json_data.keys())[0]

    if main_key not in json_data or not isinstance(json_data[main_key], list):
        return

    with open(csv_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=json_data[main_key][0].keys())
        writer.writeheader()
        for row in json_data[main_key]:
            writer.writerow(row)

    print(f"Файл {csv_name} создан.")


input_json = input("Введите 'файл.json': ")
json_to_csv(input_json)

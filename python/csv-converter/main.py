import csv
import json
import sys

def csv_to_json(source, output):
    '''Takes csv file as input and generates json file as output.'''
    with open(source,"r", newline='') as input_csv:
        reader = csv.DictReader(input_csv)
        data = [row for row in reader]

    with open(output, "w") as output_json:
        json.dump(data, output_json, indent=4)

def json_to_csv(source, output):
    '''Takes json file as input and generates csv file as output.'''
    with open(source, "r") as input_json:
        data = json.load(input_json)

    # allow a single dict (object) as input
    if isinstance(data, dict):
        data = [data]

    with open(output, "w", newline='') as output_csv:
        if not data:
            return

        # build a fieldnames list preserving first-seen order
        fieldnames = []
        for item in data:
            if isinstance(item, dict):
                for k in item.keys():
                    if k not in fieldnames:
                        fieldnames.append(k)

        writer = csv.DictWriter(output_csv, fieldnames=fieldnames, restval='', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    source = sys.argv[1]
    if source.endswith('.csv'):
        output = source.rsplit('.', 1)[0] + '.json'
        csv_to_json(source, output)
    elif source.endswith('.json'):
        output = source.rsplit('.', 1)[0] + '.csv'
        json_to_csv(source, output)
    else:
        print("Unsupported file format. Please provide a .csv or .json file.")
import csv
import json

def load_from_csv(filepath):
    records = []
    try:
        with open(filepath, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                records.append(row)
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    return records

def save_to_csv(filepath, records, fieldnames):
    with open(filepath, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)

def save_report_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
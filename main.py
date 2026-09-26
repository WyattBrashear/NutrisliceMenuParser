import argparse
import requests
import time
import os
import json
from datetime import datetime
from datetime import date, timedelta


parser = argparse.ArgumentParser()
parser.add_argument("source_menu")
args = parser.parse_args()
reading = True
i = 0
while reading:
    items = []
    target_date = date.today() + timedelta(days=i)
    print(f"Parsing menu for {target_date} ({args.source_menu}{target_date})")
    target_date_special = str(target_date).replace("-", "/")
    r = requests.get(f"{args.source_menu}{target_date_special}")
    if r.status_code == 200:
        if not os.path.exists("json_data"):
            os.makedirs("json_data")
        with open(f"json_data/{target_date}.json", "w") as f:
            json.dump(r.json(), f, indent=4)
    i+=7
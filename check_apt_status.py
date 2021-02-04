#!/usr/bin/env python3
from datetime import datetime
import logging
import json
import re


def write_to_file(unit_number, print_price):
    with open("price_records.json") as fh:
        data = json.load(fh)
    try:
        unit = data[unit_number]
        parsed_price = re.sub("[$,]", "", print_price)
        unit["prices"].append(
            {"print_price": int(parsed_price), "price_date": str(datetime.now())}
        )
        with open("price_records.json", "w") as fh:
            json.dump(data, fh)

    except Exception:
        new_unit = {"unit_number": unit_number, "prices": []}
        data.update({unit_number: new_unit})
        with open("price_records.json", "w") as fh:
            json.dump(data, fh)

        write_to_file(unit_number, print_price)


def run(apt):
    try:
        title = apt.select(".title")[0].contents[0]
        unit_number = title[-4:]
        if unit_number != "able" and unit_number[1] == "4":
            price_container = apt.select(".price")[0]
            price = price_container.select(".brand-main-text-color")
            print_price = price[0].contents[0]
            if len(price) > 1:
                print_price = price[1].contents[0]

            write_to_file(unit_number=unit_number, print_price=print_price)
    except Exception:
        print(Exception)

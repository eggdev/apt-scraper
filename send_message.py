#!/usr/bin/env python3
import requests
from datetime import date, datetime, timedelta
from url import url

headers = {"content-type": "application/json"}

sixtydays = datetime.now() + timedelta(60)


def calculate_average(prices):
    avg = 0
    for price in prices:
        avg += price["print_price"]
    return avg / len(prices)


def send_message(units):
    blocks = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Apartment Prices: {date.today()}",
                "emoji": False,
            },
        },
        {
            "type": "section",
            "text": {"type": "plain_text", "text": f"60 Days: {sixtydays}"},
        },
    ]
    for u in units:
        if u[1] == "4":
            blocks.append({"type": "divider"})
            current_unit = units[u]
            unit_prices = current_unit["prices"][-1]
            todays_price = unit_prices["print_price"]
            average_unit_price = calculate_average(current_unit["prices"])
            text = f"Unit {u}: {todays_price}\n Average Price: {average_unit_price}"
            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": text,
                    },
                }
            )
        else:
            blocks.append({"type": "divider"})
            current_unit = units[u]
            unit_prices = current_unit["prices"][-1]
            todays_price = unit_prices["print_price"]
            text = f"New Unit {u}: {todays_price}"
            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": text,
                    },
                }
            )

    payload = {"blocks": blocks}
    requests.post(url, headers=headers, json=payload)

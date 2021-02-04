#!/usr/bin/env python3
import requests
from datetime import date

url = "https://hooks.slack.com/services/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"

headers = {"content-type": "application/json"}


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
    ]
    for u in units:
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

    payload = {"blocks": blocks}
    requests.post(url, headers=headers, json=payload)
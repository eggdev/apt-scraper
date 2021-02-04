#!/usr/bin/env python3
import logging
import json
import scrape_site
from send_message import send_message

def run():
  scrape_site.run()
  with open('price_records.json') as fh:
    units = json.load(fh)
  
  send_message(units)

if __name__ == "__main__":
  logging.basicConfig(level=logging.DEBUG)
  run()
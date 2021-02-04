from bs4 import BeautifulSoup
import requests
import check_apt_status

MAIN_DOMAIN = "https://www.avaloncommunities.com/new-york/mamaroneck-apartments/avalon-mamaroneck/apartments?bedroom=1BD"

def run():
  res = requests.get(MAIN_DOMAIN)
  try:
    res.raise_for_status()
    soup_home = BeautifulSoup(res.text, 'html.parser')
    contents = soup_home.select('.content')
    for apt in contents:
      check_apt_status.run(apt)
  except Exception:
    print(Exception)

if __name__ == '__main__':
  run()
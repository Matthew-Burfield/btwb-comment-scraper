import requests, bs4
from selenium import webdriver
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-u", dest="username", required=True,
                    help="The username you want to login with")
parser.add_argument("-p", dest="password", required=True,
                    help="The password you want to login with")
args = parser.parse_args()

browser = webdriver.Chrome()
browser.get('https://beyondthewhiteboard.com/signin')
try:
		username = browser.find_element_by_id('login')
		password = browser.find_element_by_id('password')
		username.send_keys(args.username)
		password.send_keys(args.password)
		password.submit();
except:
		print('Was not able to log in.')

browser.get('https://beyondthewhiteboard.com/members/114549/workout_sessions')
# print(browser.get_cookies())
res = requests.get('https://beyondthewhiteboard.com/members/114549/workout_sessions?page=2')
soup = bs4.BeautifulSoup(res.content, 'html.parser')
print(soup.find_all('li', 'workout_session'))
browser.quit()
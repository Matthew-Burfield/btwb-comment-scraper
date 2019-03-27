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
		print('Was not able to find an element with that name.')
browser.quit()
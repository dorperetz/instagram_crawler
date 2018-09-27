#!/usr/bin/env python3.5

"""Goes through all usernames and collects their information"""
import json
import datetime
from util.settings import Settings
from util.datasaver import Datasaver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from util.cli_helper import get_all_user_names
from util.extractor import extract_information


def main(usernames):
    chrome_options = Options()
    chrome_options.add_argument('--dns-prefetch-disable')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--lang=en-US')
    chrome_options.add_argument('--headless')
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
    browser = webdriver.Chrome('C:/devl/inst_data/instagram_profilecrawl/assets/chromedriver', chrome_options=chrome_options)

    # makes sure slower connections work as well
    print ("Waiting 10 sec")
    browser.implicitly_wait(10)
    try:
        for username in usernames:
            print('Extracting information from ' + username)
            information = []
            user_commented_list = []
            try:
                information, user_commented_list = extract_information(browser, username, Settings.limit_amount)
            except:
                print("Error with user " + username)
            Datasaver.save_profile_json(username, information)

            print ("Number of users who commented on his/her profile is ", len(user_commented_list), "\n")

            Datasaver.save_profile_commenters_txt(username, user_commented_list)
            print ("\nFinished. The json file and nicknames of users who commented were saved in profiles directory.\n")

    except KeyboardInterrupt:
        print('Aborted...')

    finally:
        browser.delete_all_cookies()
        browser.close()


if __name__ == '__main__':
    usernames = get_all_user_names()
    main(usernames)

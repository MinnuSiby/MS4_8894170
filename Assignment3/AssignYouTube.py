# Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the YouTube homepage
driver.get("https://www.youtube.com/")
time.sleep(3)

# Finding the search bar and entering text
search_bar = driver.find_element("name", "search_query")
search_bar.send_keys("selenium testing tutorial")

# Submitting the search query
search_bar.send_keys(Keys.RETURN)

# Waiting for the search results page to load
time.sleep(5)

# Verifying that the search results page has loaded
assert "selenium testing tutorial" in driver.title

# Selecting a video from the search results
video_link = driver.find_element("css selector", "#video-title > yt-formatted-string")
video_link.click()


# Waiting for the video to load and play
time.sleep(10)

# Making the video mute
mute_button = driver.find_element("class name", "ytp-mute-button")
mute_button.click()

# Waiting for the video to mute and play for sometime
time.sleep(6)

# Making the video pause/stop
stop_button = driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[32]/div[2]/div[1]/button")
stop_button.click()

# Waiting for the video to pause for sometime
time.sleep(5)


# Closing the webdriver
driver.close()

![alt text](https://github.com/schikani/Easyetc-News/blob/master/easyetc.png)
# Easyetc-News 

Easyetc-News is basically a Python based webscraper which scrapes through the very famous Hacker News website (https://news.ycombinator.com) and gives the news in a browser like GUI with Votes.

## Installation
* `$ mkdir Easyetc-News-base`
* `$ cd Easyetc-News-base`
* `$ virtualenv ./venv`
* `$ source ./venv/bin/activate`
* `$ git clone https://github.com/schikani/Easyetc-News.git`
* `$ cd Easyetc-News`
* `$ pip install -r requirements.txt`

### Currently this project is tested in Ubuntu 20.04 but hopefully it should work in Mac and Windows sytems too.

### 1. GUI app 
#### This is the GUI version of Easyetc-news 
**Note:** If you have problems opening this GUI version, try 2. Terminal app shown in the next section
* #### Run `$ python easyetc_news.py`
#### If everything works fine, you should see a similar result like shown below.

![alt text](https://github.com/schikani/Easyetc-News/blob/master/Easyetc_news_screenshot.png)

#### Features:
1. To open any news, press `>>>` button.
2. The votes of the opened news will be displayed in the bottom right corner.
3. Navigate through 10 news at a time with `1-10`, `11-20`, `21-30` buttons.
4. Navigate to any random news by pressing `Randomize` button. It will also produce 10 random news from our 30 news.

### 2. Terminal app
![alt text](https://github.com/schikani/Easyetc-News/blob/master/Easyetc_news_screenshot_term.png)


# Run in Terminal

## Install
```bash
pip install scrapy
```

## Start a Project
```bash
scrapy startproject <project_name>
```

## Create a Spider
```bash
## direct into the project folder
cd <project_name>

## generate a spider
scrapy genspider <spider_name> <url>
```
Note: the url does not need http, e.g. Google url would be `www.google.com`, quotes url would be `quotes.toscrape.com`.

## Modify Settings
- Open `settings.py` 
    - Set `ROBOTSTXT_OBEY` as `False`
    - Set `DOWNLOAD_DELAY`, determine the time in seconds based on your judgement of whether there is antispider
    - Add `User-Agent` in `DEFAULT_REQUEST_HEADERS`. To acqure the information, see below:
        1. Right-click and select `Inspect` to open the developer tools
        2. Select the `Network` tab
        3. Reload the page
        4. Select any HTTP request on the left panel
    - Set `FEED_EXPORT_ENCODING = 'utf-8-sig'` when there are special characters appearing in output

- Open `items.py`
    - Define the fields for your item

- Open `<spider>.py` in `spiders` folder
    - import item field `from ..items import <class_name>`
    - assign item `item = <class_name>`
    - extract values with `xpath()`
    - assign values to item fields `item['<field_name>'] = <values>`
    - yield the item `yield item`

## Run a Spider
```bash
## run and output
scrapy crawl <spider_name> -o <file_name>.csv
```
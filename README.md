Instagram Scraper [![starme](https://img.shields.io/github/stars/joscha0/instagram-scraper.svg?style=social&label=Star)](https://github.com/joscha0/instagram-scraper)
=================
[![Source](https://img.shields.io/badge/source-GitHub-303030.svg?style=flat-square)](https://github.com/joscha0/instagram-scraper/) [![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://choosealicense.com/licenses/mit/)

Instagram Python:snake: (2&3) Scraper. Get follower count, following count, post count, and profile pic url :sunglasses:.

Requirements
------------
* **request**  [![Pypi](https://img.shields.io/pypi/v/requests.svg?style=flat-square)](https://pypi.org/project/requests) [![Source](https://img.shields.io/badge/source-GitHub-303030.svg?style=flat-square)](https://github.com/kennethreitz/requests)

* **bs4 (beautifulsoup)**  [![Pypi](https://img.shields.io/pypi/v/beautifulsoup4.svg?style=flat-square)](https://pypi.org/project/beautifulsoup4/)

```bash
pip install -r requirements.txt
```

## Usage

### As library

```python
from scraper import get_data

print(get_data('<username>'))
```


### As script

```bash
python3 scraper.py <username>
```
or
```bash
python scraper.py <username>
```

# Get a cool PDF summary
Scrapes data from an Instagram Profile and prints it out in a nice and easy to read pdf file.

:warning: requires [weasyprint](https://weasyprint.readthedocs.io/en/stable/index.html)

### Usage

```bash
python getpdf.py <username>
```

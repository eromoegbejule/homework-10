{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Texas Cosmetologist Violations\n",
    "\n",
    "Texas has a system for [searching for license violations](https://www.tdlr.texas.gov/cimsfo/fosearch.asp). You're going to search for cosmetologists!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Setup: Import what you'll need to scrape the page\n",
    "\n",
    "We'll be using Selenium for this, *not* BeautifulSoup and requests."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/eromoegbejule/.pyenv/versions/3.8.2/lib/python3.8/site-packages/pandas/compat/__init__.py:120: UserWarning: Could not import the lzma module. Your installed Python is incomplete. Attempting to use lzma compression will result in a RuntimeError.\n",
      "  warnings.warn(msg)\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.support.ui import Select\n",
    "from selenium.webdriver.support.ui import WebDriverWait"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Starting your search\n",
    "\n",
    "Starting from [here](https://www.tdlr.texas.gov/cimsfo/fosearch.asp), search for **cosmetologist violations** for people with the last name **Nguyen**."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver = webdriver.Chrome()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "driver.get(\"https://www.tdlr.texas.gov/cimsfo/fosearch.asp\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#select cosmetologist from \"license program type\" dropdown menu\n",
    "dropdown = driver.find_element_by_xpath(\"/html/body/div[1]/div/div[2]/div/div/section/div/div/table/tbody/tr/td/form/table/tbody/tr[3]/td/select/option[10]\")\n",
    "dropdown.click()\n",
    "\n",
    "#click in \"search by last name\" and type Nguyen\n",
    "last_name_search = driver.find_element_by_id(\"pht_lnm\")\n",
    "last_name_search.send_keys(\"Nguyen\")\n",
    "\n",
    "#search\n",
    "search_button = driver.find_element_by_name(\"B1\")\n",
    "search_button.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scraping\n",
    "\n",
    "Once you are on the results page, do this."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Loop through each result and print the entire row\n",
    "\n",
    "Okay wait, that's a heck of a lot. Use `[:10]` to only do the first ten (`listname[:10]` gives you the first ten)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "#to view the page html:\n",
    "#driver.page_source"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Loop through each result and print each person's name\n",
    "\n",
    "You'll get an error because the first one doesn't have a name. How do you make that not happen?! If you want to ignore an error, you use code like this:\n",
    "\n",
    "```python\n",
    "try:\n",
    "   # try to do something\n",
    "except:\n",
    "   # Instead of stopping on an error, it'll jump down here instead\n",
    "   print(\"It didn't work')\n",
    "```\n",
    "\n",
    "It should help you out. If you don't want to print anything, you can type `pass` instead of the `print` statement. Most people use `pass`, but it's also nice to print out debug statements so you know when/where it's running into errors.\n",
    "\n",
    "**Why doesn't the first one have a name?**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Loop through each result, printing each violation description (\"Basis for order\")\n",
    "\n",
    "> - *Tip: You'll get an error even if you're ALMOST right - which row is causing the problem?*\n",
    "> - *Tip: You can get the HTML of something by doing `.get_attribute('innerHTML')` - it might help you diagnose your issue.*\n",
    "> - *Tip: Or I guess you could just skip the one with the problem...*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Loop through each result, printing the complaint number\n",
    "\n",
    "- TIP: Think about the order of the elements"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Saving the results\n",
    "\n",
    "### Loop through each result to create a list of dictionaries\n",
    "\n",
    "Each dictionary must contain\n",
    "\n",
    "- Person's name\n",
    "- Violation description\n",
    "- Violation number\n",
    "- License Numbers\n",
    "- Zip Code\n",
    "- County\n",
    "- City\n",
    "\n",
    "Create a new dictionary for each result (except the header).\n",
    "\n",
    "> *Tip: If you want to ask for the \"next sibling,\" you can't use `find_next_sibling` in Selenium, you need to use `element.find_element_by_xpath(\"following-sibling::div\")` to find the next div, or `element.find_element_by_xpath(\"following-sibling::*\")` to find the next anything."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Save that to a CSV\n",
    "\n",
    "- Tip: Use `pd.DataFrame` to create a dataframe, and then save it to a CSV."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Open the CSV file and examine the first few. Make sure you didn't save an extra weird unnamed column."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Let's do this an easier way\n",
    "\n",
    "Use Selenium and `pd.read_html` to get the table as a dataframe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

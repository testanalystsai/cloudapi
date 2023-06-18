import re

import playwright
from playwright.sync_api import Page, expect
from ui_utils import genericutils as gu
import logging
from playwright.sync_api import Playwright, sync_playwright, expect

emails=gu.generateEmails(131,171)
phoneNumbers=list(gu.generatePhoneNumbers(70))
print(len(emails),len(phoneNumbers))
i=0

with sync_playwright() as playwright:
   for email in emails:
    gu.run(playwright,email,phoneNumbers[i],i)
    i=i+1
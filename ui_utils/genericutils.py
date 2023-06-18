import time
from random import randint
import re
from gmail import gmail as gm
import json
import logging
from playwright.sync_api import sync_playwright
import playwright
from playwright.sync_api import Page, expect

def generateEmails(l,m):
    emails=list()
    for i in range (l,m):
        if l<10:
            emails.append("saiciamuser+{0}@gmail.com".format("0"+str(i)))
        else:
            emails.append("saiciamuser+{0}@gmail.com".format(str(i)))
    outPutfile=open("emails.json",'w')
    json.dump(emails,outPutfile)

    return emails

from faker import Faker

def fake_phone_number(fake: Faker) -> str:
    return f'06{fake.msisdn()[5:]}'

def generatePhoneNumbers(n):
    fake = Faker()
    ph=list()
    while(len(ph)<=n):
        phNumber=fake_phone_number(fake)
        if phNumber not in ph:
            ph.append(phNumber)
    return ph
def run(playwright,email,ph,i):
    failedEmails=list()
    try:
        ff = playwright.webkit
        browser = ff.launch(headless=False)
        page = browser.new_page()
        page.goto("https://oidc-playground.akamai.com/")
        page.get_by_label("OpenID Connect URL").click()
        page.get_by_label("OpenID Connect URL").fill(
            "https://v1.api.eu.janrain.com/ad1882fb-e493-4f16-880e-9f9da7bfa1ca/login")
        page.get_by_label("OpenID Connect URL").press("Tab")
        page.get_by_role("button", name="Next").click()
        page.get_by_label("OIDC Client ID").click()
        page.get_by_label("OIDC Client ID").fill("ff61906a-39f4-4d5a-93c5-f7982591d579")
        page.get_by_label("OIDC Client ID").press("Tab")
        page.get_by_role("button", name="Next").click()
        page.get_by_role("button", name="Next").click()
        page.locator("(//span[text()='Finish'])[1]").click()
        page.get_by_role("button", name="Start").click()
        time.sleep(5)
        print("Processing record number:{0}".format(0, (i + 1)))
        page.get_by_role("link", name="Create a Multichoice ID").click()
        page.get_by_placeholder("Email Address", exact=True).click()
        page.get_by_placeholder("Email Address", exact=True).fill(str(email))
        page.locator("input[type=\"tel\"]").click()
        page.locator("input[type=\"tel\"]").click()
        page.locator("input[type=\"tel\"]").fill(str(ph))
        page.get_by_text("ValidatingCreate PasswordInclude capital letters, special characters & numbers t").click()
        page.get_by_placeholder("Password", exact=True).click()
        page.get_by_placeholder("Password", exact=True).fill("Saimyself@1")
        page.get_by_role("button", name="Create Your MultiChoice ID").click()
        time.sleep(9)
        otp = gm.getEmails()
        page.locator("#otp-1").click()
        page.locator("#otp-1").fill(otp[0])
        page.locator("#otp-2").fill(otp[1])
        page.locator("#otp-3").fill(otp[2])
        page.locator("#otp-4").fill(otp[3])
        page.locator("#otp-5").fill(otp[4])
        page.locator("#otp-6").fill(otp[5])
        page.locator("//h1[text()='Access Code Required']").click()
        page.keyboard.press("Tab")
        time.sleep(4)
        page.keyboard.press("Tab")
        page.get_by_role("button", name="Continue").click()
        time.sleep(5)
        print("Completed processing email :{0}".format(0, email))
        page.close()
        browser.close()
    except Exception as e:
        print(e)
        failedEmails.append(email)
    finally:
        failures=open('failures.json','w')
        json.dump(failedEmails,failures)


def processUIData(page: Page,emails,phoneNumbers):
    try:
        i = 0
        for email in emails:
            page.goto("https://oidc-playground.akamai.com/")
            page.get_by_label("OpenID Connect URL").click()
            page.get_by_label("OpenID Connect URL").fill(
                "https://v1.api.eu.janrain.com/ad1882fb-e493-4f16-880e-9f9da7bfa1ca/login")
            page.get_by_label("OpenID Connect URL").press("Tab")
            page.get_by_role("button", name="Next").click()
            page.get_by_label("OIDC Client ID").click()
            page.get_by_label("OIDC Client ID").fill("ff61906a-39f4-4d5a-93c5-f7982591d579")
            page.get_by_label("OIDC Client ID").press("Tab")
            page.get_by_role("button", name="Next").click()
            page.get_by_role("button", name="Next").click()
            page.locator("(//span[text()='Finish'])[1]").click()
            page.get_by_role("button", name="Start").click()
            time.sleep(3)
            logging.debug("Processing record number:{0}".format(0, (i + 1)))
            page.get_by_role("link", name="Create a Multichoice ID").click()
            page.get_by_placeholder("Email Address", exact=True).click()
            page.get_by_placeholder("Email Address", exact=True).fill(str(email))
            page.locator("input[type=\"tel\"]").click()
            page.locator("input[type=\"tel\"]").click()
            page.locator("input[type=\"tel\"]").fill(str(phoneNumbers[i]))
            page.get_by_text("ValidatingCreate PasswordInclude capital letters, special characters & numbers t").click()
            page.get_by_placeholder("Password", exact=True).click()
            page.get_by_placeholder("Password", exact=True).fill("Saimyself@1")
            page.get_by_role("button", name="Create Your MultiChoice ID").click()
            time.sleep(6)
            otp = gm.getEmails()
            page.locator("#otp-1").click()
            page.locator("#otp-1").fill(otp[0])
            page.locator("#otp-2").fill(otp[1])
            page.locator("#otp-3").fill(otp[2])
            page.locator("#otp-4").fill(otp[3])
            page.locator("#otp-5").fill(otp[4])
            page.locator("#otp-6").fill(otp[5])
            page.locator("//h1[text()='Access Code Required']").click()
            page.keyboard.press("Tab")
            time.sleep(2)
            page.keyboard.press("Tab")
            page.get_by_role("button", name="Continue").click()
            time.sleep(2)
            logging.debug("Completed processing email :{0}".format(0, email))
            page.close()

            i += 1


    except Exception as e:
        print(e)

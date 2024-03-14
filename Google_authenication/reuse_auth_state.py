from creds import *
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context( storage_state=".auth/storage_state.json")

    page = context.new_page()

    # Visit google accounts
    page.goto("https://accounts.google.com")

    page.pause()
    context.close()

    

    browser.close()
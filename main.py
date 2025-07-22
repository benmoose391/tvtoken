import requests
import json
from playwright.sync_api import sync_playwright

def get_thetvapp_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://thetvapp.to/tv", timeout=60000)

        # Wait for cookies to load (you can increase if needed)
        page.wait_for_timeout(5000)

        cookies = context.cookies()
        browser.close()

        return cookies

if __name__ == "__main__":
    cookies_raw = get_thetvapp_cookies()
    required = ['thetvapp_session']
    cookies = {c['name']: c['value'] for c in cookies_raw} # if c['name'] in required}
    #cookies['return_url'] = '%2Ftv%2Fxptv-sports'
    with open ('thetvapp-cookies.json', 'w') as f:
        json.dump(cookies, f, indent=2)

from playwright.sync_api import sync_playwright

def test_basic():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.gluteguard.ca/home")
        text_to_find = "Norwell Consumer Healthcare Inc."
        assert text_to_find in page.content(), f"'{text_to_find}' not found on the page."
        if text_to_find in page.content():
        page.evaluate("alert('Text found!')")
        #cdpage.wait_for_timeout(30000)
        browser.close()
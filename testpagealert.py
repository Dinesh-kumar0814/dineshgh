from playwright.sync_api import sync_playwright
from openpyxl import load_workbook
import time

def read_links_from_excel(testpagealertlinks.xlsx, sheet_name="links", column="A"):
    workbook = load_workbook(filename=file_path)
    sheet = workbook[sheet_name]

    links = []
    for cell in sheet[column]:
        if cell.value and isinstance(cell.value, str):
            links.append(cell.value.strip())

    return links

def open_links_in_browser(links):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        for link in links:
            print(f"Opening: {link}")
            page.goto(link)
            page.wait_for_timeout(30000)  # wait 30 seconds for each link

        print("All links opened.")
        page.wait_for_timeout(10000)  # keep browser open 10 sec
        browser.close()

if __name__ == "__main__":
    excel_file = "testpagealertlinks.xlsx"        # your Excel file
    sheet = "links"                 # sheet name
    column = "A"                     # column containing URLs

    links_list = read_links_from_excel(excel_file, sheet, column)
    open_links_in_browser(links_list)

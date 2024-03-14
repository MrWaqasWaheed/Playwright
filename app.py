from playwright.sync_api import sync_playwright
from time import perf_counter

def on_filechooser(filechooser):
    print("file choosen", filechooser)
    filechooser.set_files("file.txt")
def on_dialog(dialog):
    print("dialog box appears")
    dialog.accept()
def on_prompt(dialog):
    print("prompt box appears", dialog)
    dialog.accept("playwright")

with sync_playwright() as playwright:
    # Launch a browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)    
    # Create a new page
    page = browser.new_page()   
    print("Page loading...")
    start=perf_counter()
    
    # Visit the URL
    page.goto("https://bootswatch.com/default", wait_until='load')
    time_taken=perf_counter()-start
    print(f"...Page loaded in {round(time_taken,2)}s")
    
    
    page.on("filechooser",on_filechooser)
    file_input=page.get_by_label("Default file input example")
    file_input.click()

    page.goto("https://testpages.eviltester.com/styled/alerts/alert-test.html")

    # page.on("dialog", on_dialog)
    # alert_btn=page.get_by_text("Show confirm box")
    # alert_btn.click()

    page.on("dialog", on_prompt)
    alert_btn=page.get_by_text("Show prompt box")
    alert_btn.click()


    
    # Close the browser
    browser.close()

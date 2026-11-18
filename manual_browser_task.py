import sys

from playwright.sync_api import sync_playwright

sys.stdout.reconfigure(encoding="utf-8")

URL = "https://qa-playground-automation-testing.onrender.com/"


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(
            URL,
            # wait_until="domcontentloaded",
            # timeout=60000,
        )
        # page.wait_for_timeout(30000)

        print("Page title:", page.title())
        print("Current URL:", page.url)

        # Click the "Products" link and wait for the products page to load
        page.get_by_role("link", name="Products", exact=True).click()
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2000)

        print("\n--- After clicking Products ---")
        print("Page title:", page.title())
        print("Current URL:", page.url)

        print("\n--- Page snapshot (aria) ---")
        print(page.aria_snapshot())

        browser.close()


if __name__ == "__main__":
    main()

"""The automated vote trolling module."""

import config
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from chromedriver_py import binary_path


# Web driver options
options = {
    'proxy': {
        'http': config.http_proxy_string,
        'https': config.https_proxy_string,
        'no_proxy': ''
    }
}


def vote_for_names(driver, names):
    """Take a list of names and vote for each one."""
    for name in names:
        # Find the root element with the name
        root_el = driver.find_element(
            By.XPATH, config.root_element_xpath.replace('NAME', name)
        )

        # Get the root element location
        location = root_el.location

        # Scroll to the element
        driver.execute_script(
            """
            window.scrollTo(
              {
                top: arguments[0],
                left: 0,
                behavior: 'instant'
              }
            );
            """,
            location['y']
        )

        # Find the button
        button_el = driver.find_element(
            By.XPATH,
            config.root_element_xpath.replace('NAME', name) +
            config.button_xpath
        )

        # Click it
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(button_el)
        ).click()


# Loop the specified number of times
for i in range(0, config.num_of_votes):
    # Create the webdriver
    driver = webdriver.Chrome(
        seleniumwire_options=options,
        executable_path=binary_path
    )
    driver.implicitly_wait(10)

    # Visit the URL of the poll
    driver.get(config.poll_url)

    # Vote for the names
    vote_for_names(driver, config.names)

    # Close the web driver
    driver.close()

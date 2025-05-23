from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver
driver = webdriver.Chrome()

# Load the webpage
driver.get("https://demoqa.com/")
# Maximize the window
driver.maximize_window()

# 1. Click the "Elements" tab
elements_tab = driver.find_element(By.XPATH, "//h5[text()='Elements']")
elements_tab.click()

# 2. Handle Web Elements (Find all columns, first row first data, last row last data)
# Navigate to "Web Tables"
driver.find_element(By.XPATH, "//span[text()='Web Tables']").click()

# Find all columns
columns = driver.find_elements(By.XPATH, "//div[@class='rt-resizable-header-content']")
print("Columns:")
for col in columns:
    print(col.text)

# Find the first row's first data
first_row_first_data = driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div[1]/div/div[1]")
print("First row, first data:", first_row_first_data.text)

# Find the last row's last data
last_row_last_data = driver.find_element(By.XPATH, "//div[@class='rt-tbody']/div[last()]/div/div[last()]")
print("Last row, last data:", last_row_last_data.text)

# 3. Find the broken link
# Navigate to "Links"
driver.find_element(By.XPATH, "//span[text()='Links']").click()

# Click on the "Broken" link to check for broken link
broken_link = driver.find_element(By.LINK_TEXT, "Broken Link")
broken_link.click()

# Verify the page title or status
try:
    WebDriverWait(driver, 10).until(EC.title_contains("404"))
    print("Broken link verified: 404 page found.")
except:
    print("No 404 page found; link is not broken.")

# Navigate back to the main page
driver.back()

# 4. Upload and download the file
# Navigate to "Upload and Download"
driver.find_element(By.XPATH, "//span[text()='Upload and Download']").click()

# Download the file
download_button = driver.find_element(By.ID, "downloadButton")
download_button.click()
print("Download initiated.")

# Upload a file (Replace with the correct path to your file)
upload_button = driver.find_element(By.ID, "uploadFile")
upload_button.send_keys("C:/path/to/your/file.txt")
uploaded_file_path = driver.find_element(By.ID, "uploadedFilePath").text
print("Uploaded file path:", uploaded_file_path)

# 5. Click the "Alerts, Frame & Windows" tab
driver.find_element(By.XPATH, "//h5[text()='Alerts, Frame & Windows']").click()

# 6. Click "Browser Windows", open a new tab, fetch text, and assert it
driver.find_element(By.XPATH, "//span[text()='Browser Windows']").click()
driver.find_element(By.ID, "tabButton").click()

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])
new_tab_text = driver.find_element(By.ID, "sampleHeading").text
assert "This is a sample page" in new_tab_text
print("New tab text asserted:", new_tab_text)

# Close the new tab and switch back to the main window
driver.close()
driver.switch_to.window(driver.window_handles[0])

# 7. Handle the iframe and validate
driver.find_element(By.XPATH, "//span[text()='Frames']").click()
driver.switch_to.frame("frame1")
iframe_text = driver.find_element(By.ID, "sampleHeading").text
assert "This is a sample page" in iframe_text
print("Iframe text asserted:", iframe_text)

driver.switch_to.default_content()  # Switch back to main content

# 8. Handle the nested iframe and validate
driver.find_element(By.XPATH, "//span[text()='Nested Frames']").click()
driver.switch_to.frame(driver.find_element(By.ID, "frame1"))
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

nested_iframe_text = driver.find_element(By.TAG_NAME, "p").text
assert "Child Iframe" in nested_iframe_text
print("Nested iframe text asserted:", nested_iframe_text)

driver.switch_to.default_content()  # Switch back to the main content

# Clean up
driver.quit()

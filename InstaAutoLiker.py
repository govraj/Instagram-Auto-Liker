# import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# create webdriver object for Edge Browser(Change Driver as per your preference.)
driver = webdriver.Edge('.\\edgedriver_win64\\msedgedriver.exe')
#Explicit wait with 10 second timer.
wait = WebDriverWait(driver, 20)  
# Open URL
driver.get("https://www.instagram.com/")


# Username and Password of your Instagram account.
# Change 123 with your username and 456 with password.
up_dict = {'username':['123'],
'password':['456']}


# Login to Instagram with your username and password
for u,p in zip(up_dict['username'],up_dict['password']):
    user = u
    password = p
    # Input Username
    u_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm>div>div:nth-child(1)>div>label>input")))
    driver.find_element_by_css_selector('#loginForm>div>div:nth-child(1)>div>label>input').send_keys(user)
    
    # Input Password
    u_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm>div>div:nth-child(2)>div>label>input")))
    driver.find_element_by_css_selector('#loginForm>div>div:nth-child(2)>div>label>input').send_keys(password)
    
    driver.implicitly_wait(3)
    
    # Click on Log in.
    login_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#loginForm>div>div:nth-child(3)>button")))
    element = driver.find_element_by_css_selector('#loginForm>div>div:nth-child(3)>button')
    # check if button is enable.
    if element.is_enabled():
        element.click()
    else:
        # wait for 5 second then click.
        driver.implicitly_wait(5)
        element.click()


# Enter username you want like there posts.
username = 'path_to_datascience' # change it.
url = "https://www.instagram.com/"+username+"/"
# Navigate to url.
driver.get(url)
try:
    posts_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.v1Nh3>a')))
    posts = driver.find_elements_by_css_selector('.v1Nh3>a')
except:
    posts=[]
    print('Posts Not Found')
try:
    posts[0].click()
    # 5 is no of posts you want like.
    for i in range(5):
        # Like Pic
        like_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.fr66n>button')))
        like = driver.find_element_by_css_selector('span.fr66n>button')
        like.click()
        # Next post.
        Next_wait = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.EfHg9>div>div>a._65Bje.coreSpriteRightPaginationArrow')))
        Next = driver.find_element_by_css_selector('div.EfHg9>div>div>a._65Bje.coreSpriteRightPaginationArrow')
        Next.click()            
except:
    print('Posts Not clicked')

# close driver
driver.close()



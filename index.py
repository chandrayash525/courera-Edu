print("+----------------------------------------------------------------+")
print("|     Canva premoum Education account                            |")
print("+----------------------------------------------------------------+")
###########################################################################################
#          Import                                                                         #
###########################################################################################
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from clipboard import paste
from random import choice
from os import system
#=========================================================================================#
#          important function                                                             #
#=========================================================================================# 
# use to print the progress of programm
def printC(n):
    system("cls")
    print("+----------------------------------------------------------------+")
    print("|     Canva premoum Education account                            |")
    print("+----------------------------------------------------------------+")
    print("Progress  : ",str(n)+"/7")
# use to click on buttons
def click(driver,css,time = 60):
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , css))
        )
        element.click()
    except:
def click(driver,css,time = 60):
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , css))
        )
        element.click()
    except:
        sleep(5)
        click(driver,css)
# use to type in input box
def type(driver,css,text,time = 60):
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , css))
        )
        element.send_keys(text)
    except:
        sleep(5)
# waiting until a we go to specif url
def waitPage(driver,eUrl,time=180,has=False):
    WebDriverWait(driver,time).until(
        lambda driver: (1-has)*(driver.current_url == eUrl)+has*(eUrl in driver.current_url)
    )
# checking mail of url
def checkNewMail():
    eduEmailAccount.get('https://10minutesemail.net/email?id=1')
    if(eduEmailAccount.title == "Email: Action Required: Please confirm your email - 10 Minutes Email"):
        return True
    return False
# getting element from driver(page)
def getElement(driver,css,time=50):
    sleep(5)
    try:
        element = WebDriverWait(driver, time).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR , css))
        )
        return element
    except:
        sleep(5)
#=========================================================================================#
#          Getting basic information                                                      #
#=========================================================================================#
# taking basic emformation like name and password
name = input("Enter your name : ")
passWord = input("Enter the password \nIf you leave it bot will aurtomatically generat password and provide you :")
if(not passWord):
    for x in range(8):
        passWord += choice("""ABCDEFGHIJKMNOPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz1234567890~!@#$%^&*()_+-=`{}|[]\\:;<,.>/?""")
print("All information is saved in file data.txt")
input("Are your ready \n Press Enter")
    print("+----------------------------------------------------------------+")
    print("|     Canva premoum Education account                            |")
    print("+----------------------------------------------------------------+")
#=========================================================================================#
#          Getting Edu email                                                              #
#=========================================================================================#
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
eduEmailAccount = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
eduEmailAccount.get("https://10minutesemail.net/")
eduEmailAccount.implicitly_wait(20)
while(1==1):
    email = getElement(eduEmailAccount,"#tempEmailAddress").get_attribute('value')
    printC(1) 
    if(email[-13:]=="@email.edu.pl"):
        break
    else:
        click(eduEmailAccount,"#deleteEmailAddress > i")
printC(2)
# scraping/getting recoveryKey
recoverKey = eduEmailAccount.find_element_by_id("recoverKey").text
#=========================================================================================#
#          coursera signup                                                                #
#=========================================================================================#
courseraWebsite = webdriver.Chrome(ChromeDriverManager().install())
# coursera signup page
link = "https://www.coursera.org/for-university-and-college-students/?authMode=signup&canContinue=true&continueWith=&email=&utm_campaign=header-for-students&utm_content=corp-to-landing-for-students&utm_medium=coursera&utm_source=header-for-students-link"
courseraWebsite.get(link)
# prerequisite for entering data
courseraWebsite.implicitly_wait(30)
courseraWebsite.execute_script("arguments[0].remove()",getElement(courseraWebsite,"body > div._1widl7g > div > div > section > section > div:nth-child(2) > form > div._p2k6y2.css-scmj5h > button > svg"))
#courseraWebsite.execute_script('document.querySelector("body > div._1widl7g > div > div > section > section > div:nth-child(2) > form > div._p2k6y2.css-scmj5h > button").remove()')
courseraWebsite.execute_script("arguments[0].setAttribute('type', 'password')",getElement(courseraWebsite,"#email"))

# Entering data
type(courseraWebsite,"#name",name) #entring name
type(courseraWebsite,"#email",email) #entring email
type(courseraWebsite,"#password",passWord)  #entrin password
click(courseraWebsite,"body > div._1widl7g > div > div > section > section > div:nth-child(2) > form > button") # Signup button
# waiting of confirmation
printC(3)
    print("+----------------------------------------------------------------+")
    print("|     Canva premoum Education account                            |")
    print("+----------------------------------------------------------------+")


# applyting to coursera education programm
waitPage(courseraWebsite,"https://www.coursera.org/for-university-and-college-students/?canContinue=true&continueWith=&email=&utm_campaign=header-for-students&utm_content=corp-to-landing-for-students&utm_medium=coursera&utm_source=header-for-students-link")
courseraWebsite.execute_script(f"""arguments[0].innerText = \"{'•'*len(email)}\"""",getElement(courseraWebsite,"#rendered-content > div > div > div.rc-UpswellPage.styleguide > div.rc-UniversityBanner > div > div._jyhj5r > div._jwcsk0 > div > div.link-message > div > span > span > strong"))
courseraWebsite.execute_script("arguments[0].setAttribute('type', 'password')",getElement(courseraWebsite,"#university-email-input-input"))
type(courseraWebsite,"#university-email-input-input",email) #entring edu email
click(courseraWebsite,"#rendered-content > div > div > div.rc-UpswellPage.styleguide > div.rc-UniversityBanner > div > div._jyhj5r > div._jwcsk0 > div > div.input-button-wrapper > button > span")
waitPage(courseraWebsite,"https://www.coursera.org/programs",has=True)
printC(4)
# formality buttons
click(courseraWebsite,"#rendered-content > div > div > div.rc-ProgramHomeWrapper.rc-SingleProgramPage.ph-cds-enabled > div.rc-UpswellModal > div > div.c-modal-content > div.rc-UpswellUserTypeScreen > div > div > div.button-container > button")
click(courseraWebsite,"#rendered-content > div > div > div.rc-ProgramHomeWrapper.rc-SingleProgramPage.ph-cds-enabled > div.rc-UpswellModal > div > div.c-modal-content > div.rc-UpswellSocialShareScreen > div > div > div.button-container > button > span")
click(courseraWebsite,"#rendered-content > div > div > div.rc-ProgramHomeWrapper.rc-SingleProgramPage.ph-cds-enabled > div.rc-UpswellModal > div > div.c-modal-content > div.c-modal-x-out > a")
printC(5)
# exit for browser of coursera website
courseraWebsite.quit()

#=========================================================================================#
#          Confirmation of email                                                          #
#=========================================================================================#

# until a confirmation email comes from coursera
WebDriverWait(eduEmailAccount,900).until(
    lambda ankit : checkNewMail()
)
# switch to iFrame having confirmation email link
iFrame = eduEmailAccount.find_element_by_css_selector("body > main > div.container.mt-2 > div > div.col-md-8.p-2 > div > div.card-body.px-3 > div.mt-2 > iframe")
eduEmailAccount.switch_to.frame(iFrame)
# clicking to confirmation link
click(eduEmailAccount,"#backgroundTable > tbody > tr > td > table:nth-child(3) > tbody > tr > td > div > p:nth-child(2) > a > span")
# closing brawser of education email
eduEmailAccount.quit()
printC(6)
#=========================================================================================#
#          Saving the data                                                                #
#=========================================================================================#
with open("static.txt","w") as f:
    data = f"""Name :  {name}
    Email :  {email}
    Password : {passWord}
    Email Recovery (how to use comming soon) : {recoverKey} 
    """
    f.write(data)
    f.close()
printC(7)
print("All information is saved in file data.txt")
input("exit")

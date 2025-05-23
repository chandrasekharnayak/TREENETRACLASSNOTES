*** Settings ***
Documentation    To validate the login page
Library    SeleniumLibrary



*** Test Cases ***
Validate UnSuccesful Login
    open the browser with the perfect url
    Fill the login form
#    wait until it checks and display error messages
#    verify error message is correct

*** Keywords ***
open the browser with the perfect url
    Create Webdriver    Chrome
    Go To    https://www.facebook.com/login/

Fill the login form
    Input Text    id:email    dummyvalue@gamil.com
    Input Password    pass    password@123
    Click Button    loginbutton





    
    


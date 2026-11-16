*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  maija
    Set Password  aijaahans
    Set Password Confirmation  aijaahans
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  Pö
    Set Password  pomppulinna
    Set Password Confirmation  pomppulinna
    Click  button >> text=Register
    Register Should Fail With Message  Username

Register With Valid Username And Too Short Password
    Set Username  Rolli
    Set Password  peikko
    Set Password Confirmation   peikko
    Click  button >> text=Register
    Register Should Fail With Message  Password

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle1234
    Set Password Confirmation  kalle1234
    Click  button >> text=Register
    Register Should Fail With Message  already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    ${content}=  Get Text  body
    Should Contain  ${content}  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Fill Secret  id=password_confirmation  $password_confirmation

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page


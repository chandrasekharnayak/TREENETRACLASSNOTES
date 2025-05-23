*** Settings ***
Library    source_file.py


*** Variables ***
${A}    10
${B}    5

*** Test Cases ***
Addition Test
    ${result}=    Mul    ${A}    ${B}
    Should Be Equal    ${result}    15

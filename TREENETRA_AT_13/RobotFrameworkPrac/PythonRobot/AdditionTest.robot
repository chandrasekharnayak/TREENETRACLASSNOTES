*** Settings ***
Library    MathLibrary.py

*** Variables ***
${number1}    10
${number2}    20
${expected_result}    30

*** Test Cases ***
Validate Addition Of Two Numbers
    ${num1}    Evaluate    ${number1}
    ${num2}    Evaluate    ${number2}
    ${output}    Evaluate    ${expected_result}

    ${result}=    Add Two Num    ${num1}    ${num2}
    Should Be Equal    ${result}    ${output}

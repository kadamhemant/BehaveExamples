from behave import *


@given('I am on calculater')
def step_impl(context):
    # number = input("Please enter the numbers for addition")
    print("Welcome to calculator app")


@when('I enter "{number1}" and "{number2}"')
def step_impl(context, number1, number2):
    context.number1 = number1
    context.number2 = number2

    print("number entered are", number1, number2)


@step('I click on "{operation}" button')
def step_impl(context, operation):
    context.operation = operation
    if context.operation == 'plus':
        context.total = int(context.number1) + int(context.number2)
    elif context.operation == 'minus':
        context.total = int(context.number1) - int(context.number2)
    elif context.operation == 'multiplication':
        context.total = int(context.number1) * int(context.number2)
    elif context.operation == 'division':
        context.total = int(context.number1) / int(context.number2)


@then('Calculate the amount and display')
def step_impl(context):
    print(context.operation, "Calculated amount is", context.total)

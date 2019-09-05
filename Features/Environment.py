from behave import *


@fixture
def fix_name_1(context):
    print("Now in fixture")


def before_feature(context, feature):
    use_fixture(fix_name_1, context)
    print("Before each feature")


def before_scenario(context, scenario):
    print("Before each scenario")

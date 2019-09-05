# Created by hemant.kadam at 9/4/2019
Feature: Calculation of two digits
  # Enter feature description here
  @smoke @regression
  Scenario: Addition of two digits
    Given I am on calculater
    When I enter "23" and "24"
    And I click on "plus" button
    Then Calculate the amount and display

    @regression
  Scenario: Subtraction of two digits
    Given I am on calculater
    When I enter "23" and "45"
    And I click on "plus" button
    Then Calculate the amount and display

  Scenario: Multiplication of two digits
    Given I am on calculater
    When I enter "23" and "24"
    And I click on "multiplication" button
    Then Calculate the amount and display

  Scenario: Division of two digits
    Given I am on calculater
    When I enter "23" and "24"
    And I click on "division" button
    Then Calculate the amount and display
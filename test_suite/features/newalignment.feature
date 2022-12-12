@skf_tkba
@regression
Feature: Verify the new alignment page functionalities

  @smoke
  Scenario: Verify user can launch mobile application
    Given user has just launched the "SKF-TKBA" application
    Then he lands on "NEW ALIGNMENT" page

  @wip
  Scenario: verify the add new machine page
    When he clicks on "Add new machine" button
    And he lands on "ADD NEW MACHINE" page

  @skip
  @bug
  Scenario: Verify the select machine page
    When he clicks on "Select machine" button
    And he lands on "SELECT MACHINE" page

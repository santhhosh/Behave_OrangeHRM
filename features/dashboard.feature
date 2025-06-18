Feature: Dashboard

  Background:
    Given the user redirects to the login page
    When the user login in with username "Admin" and password "admin123"


  @Timeatwork
  Scenario Outline: Dashboard Page_Time_At_Work
    When the user clicks on the stopwatch link
    When the user enters note "<Note>"
    And the user clicks on the button

    Examples: credentials

       | Note|
       |Testing|

  @Upgrade
  Scenario: Dashboard Page_click_upgrade_button
    When the user clicks on the upgrade button




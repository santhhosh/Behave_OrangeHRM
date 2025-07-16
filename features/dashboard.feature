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
  Scenario Outline: Dashboard Page_click_upgrade_button
    When click on upgrade button
    When the user selects locale "<locale>"
    When click on bookademo button
    When the user enters firstname "<firstname>" at bookademo
    When the user enters phonenumber "<phonenumber>" at bookademo
    When the user enters email "<email>" at bookademo
    When the user enters companyname "<companyname>" at bookademo
    When the user selects country "<country>" at bookademo
    When the user clicks submit button at bookademo

  Examples: credentials

      |locale | firstname| phonenumber | email| companyname |country|
      |En    |santosh   | 9999988888  | s@gmail.com | LSR  |Angola |

  @QuickLaunch_assignleave
  Scenario:
    When the user goes to quicklaunch and clicks assignleave

  @QuickLaunch_leavelist
  Scenario:
    When the user goes to quicklaunch and clicks leavelist

  @QuickLaunch_timesheets
  Scenario:
    When the user goes to quicklaunch and clicks timesheets

  @QuickLaunch_applyleave
  Scenario:
    When the user goes to quicklaunch and clicks applyleave

  @QuickLaunch_myleave
  Scenario:
    When the user goes to quicklaunch and clicks myleave

  @QuickLaunch_mytimesheet
  Scenario:
    When the user goes to quicklaunch and clicks mytimesheet
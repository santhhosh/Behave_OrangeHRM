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
  Scenario Outline:
    When the user goes to quicklaunch and clicks Assign_Leave and enters "<employee_name>","<leave_type>","<from_date>","<to_date>","<comments>"
      Examples:
      | employee_name  | leave_type     | from_date  | to_date  | comments |
      |  Ravi M B      |CAN - Vacation  |2025-01-01  |2025-31-12| testing  |

  @QuickLaunch_leavelist
  Scenario:
    When the user goes to quicklaunch and clicks leavelist

  @QuickLaunch_timesheets
  Scenario Outline:
    When the user goes to quicklaunch and clicks timesheets and enters "<timesheetperiod>"
    Examples:
    |timesheetperiod|
    | 2025-16-09 to 2025-22-09 |

  @QuickLaunch_applyleave
  Scenario Outline:
    When the user goes to quicklaunch and clicks applyleave and enters "<employee_name>","<leave_type>","<from_date>","<to_date>","<comments>"
      Examples:
      | employee_name  | leave_type     | from_date  | to_date  | comments |
      |  Ravi M B      |CAN - Vacation  |2025-01-01  |2025-31-12| testing  |

  @QuickLaunch_myleave
  Scenario:
    When the user goes to quicklaunch and clicks myleave

  @QuickLaunch_mytimesheet
  Scenario:
    When the user goes to quicklaunch and clicks mytimesheet
Feature: PIM

  Background:
    Given the user redirecting to the login page
    When the user logins in with username "Admin" and password "admin123"
    When the user clicks on the PIM menu and redirects to the PIM page

  @Addemployee
  Scenario Outline: Addemployee
    When the user clicks on Addemployee
    When the user enters firstname "<Firstname>"
    When the user enters middlename "<Middlename>"
    When the user enters lastname "<Lastname>"
    When the user enters the employeeid "<Employeeid>"
    When the user uploads file
    When the user clicks on the save button

    Examples:
      | Firstname | Middlename | Lastname | Employeeid |
      | Santosh   | Avengers   | Patnana  | 0501       |

  @Reports
  Scenario Outline: Reports
    When the user clicks on Reports
    When the user enters reportname "<ReportName>" of Reports
    When the user clicks on the search button of Reports

    Examples:
      | ReportName |
      |Employee Contact info report|


Feature: PIM

  Background:
    Given the user redirecting to the login page
    When the user logins in with username "Admin" and password "admin123"
    When the user clicks on the PIM menu and redirects to the PIM page


  #configuration
  @OptionalFields
  Scenario:
    When the user clicks on configuration for optionalfields
    When the user clicks on optionalfields
    When the user clicks on showdeprecatedfields of optionalfields
    When the user clicks on ShowSSNfieldinPersonalDetails of optionalfields
    When the user clicks on ShowSINfieldinPersonalDetails of optionalfields
    When the user clicks on ShowUSTaxExemptionsmenu of optionalfields
    When the user clicks on savebutton of optionalfields

  @CustomFields
  Scenario Outline:
    When the user clicks on configuration for CustomFields and enters "<fieldname>","<screen>","<type>"
    Examples:
      | fieldname | screen             | type            |
      | Santosh   | Personal Details   | Text or Number  |

  @DataImport
  Scenario:
    When the user clicks on configuration for dataimport and uploads file

  @ReportingMethods
  Scenario Outline:
    When the user clicks on configuration for ReportingMethods and enters "<name>"
    Examples:
      | name      |
      | Santosh   |

  @TerminationReasons
  Scenario Outline:
    When the user clicks on configuration for TerminationReasons and enters "<name>"
    Examples:
      | name      |
      | Testing_Termination  |





  @EmployeeList
  Scenario Outline:
    When the user clicks on EmployeeList on employeelist
    When the user enters employeename "<employeename>" on employeelist
    When the user enters employeeid "<employeeid>" on employeelist
    When the user selects employmentstatus "<employmentstatus>" on employeelist
    When the user selects include "<include>" on employeelist
    When the user enters supervisorname "<supervisorname>" on employeelist
    When the user selects jobtitle "<jobtitle>" on employeelist
    When the user selects subunit "<subunit>" on employeelist
    When the user clicks on search button on employeelist

    Examples:
      | employeename        | employeeid | employmentstatus | include                    | supervisorname    | jobtitle        | subunit |
      | Ahmad Ali  Badaha   | 0418       | Freelance        | Current and Past Employees | Ahmad Ali  Badaha | Software Tester | Administration |
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


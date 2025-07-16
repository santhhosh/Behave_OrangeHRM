Feature: TIME

  Background:
    Given the user redirecting to the login page for Time Module
    When the user logins in with username "Admin" and password "admin123" for Time Module
    When the user clicks on the Time menu and redirects to the Time page for Time Module

  @MyTimeSheets
  Scenario Outline:
    When the user clicks on TimeSheets for mytimesheets and enters "<timesheetperiod>" and clicks on submit button
    Examples:
      | timesheetperiod          |
      | 2025-16-06 to 2025-22-06 |

  @EmployeeTimeSheets
  Scenario Outline:
    When the user clicks on TimeSheets for employeetimesheets and enters "<employeename>" and clicks on save button
    Examples:
      | employeename     |
      | manda akhil user |

  @MyRecords
  Scenario Outline:
    When the user clicks on attendance for myrecords and enters "<date>" and clicks on view button
    Examples:
      | date     |
      | 2025-30-06 |

  @PunchInOut
  Scenario Outline:
    When the user clicks on attendance for PunchIn/Out and enters "<date>","<note>"and clicks on submit button
    Examples:
      | date       | hour | minute | note    |
      | 2025-25-06 | 22   | 05     | punchin |

  @EmployeeRecords
  Scenario Outline:
    When the user clicks on attendance for EmployeeRecords and enters "<employeename>","<date>"and clicks on view button
    Examples:
      | date       |employeename           | minute | note    |
      | 2025-30-06 |Chup Saúl Vélez Ponce   | 05     | punchin |

  @Configuration
  Scenario Outline:
    When the user clicks on attendance for Configuration and clicks on save button
    Examples:
      | date       |employeename           | minute | note    |
      | 2025-25-06 |Timothy Lewis Amiano   | 05     | punchin |

  #Reports
  @ProjectReports
  Scenario Outline:
    When the user clicks on reports for projectreports and enters "<projectname>","<fromdate>","<todate>"clicks on view button
    Examples:
      | projectname                                    |fromdate    |todate       |
      | Global Corp and Co - Global Software phase - 2 |2025-01-06  | 2025-30-06  |

  @EmployeeReports
  Scenario Outline:
    When the user clicks on reports for employeereports and enters "<employeename>","<projectname>","<activityname>","<fromdate>","<todate>"clicks on view button
    Examples:
      |employeename  | projectname                            |activityname  |fromdate    |todate       |
      |Ranga  Akunuri| The Coca-Cola Company - Coke - Phase 1 |Administration|2025-01-06  | 2025-30-06  |

  @AttendanceSummary
  Scenario Outline:
    When the user clicks on reports for attendancesummary and enters "<employeename>","<jobtitle>","<subunit>","<employeementstatus>","<fromdate>","<todate>"clicks on view button
    Examples:
      |employeename    | jobtitle                |subunit    |employeementstatus  |fromdate    |todate       |
      |Vanessa  Edwards| Chief Executive Officer |Engineering|Part-Time Internship|2025-01-06  | 2025-30-06  |

  #ProjectInfo
  @Customers
  Scenario Outline:
    When the user clicks on projectinfo for customers and enters "<name>","<description>"clicks on view button
    Examples:
      |name    | description     |
      |Santhosh| testing purpose |

  @Projects
  Scenario Outline:
    When the user clicks on projectinfo for projects and enters "<customername>","<project>","<projectadmin>"clicks on search button
    Examples:
      |customername   | project    | projectadmin |
      |ACME Ltd       | ACME Ltd   | ACME Ltd     |

  @Add_Projects
  Scenario Outline:
    When the user clicks on projectinfo for projects and enters "<name>","<customername>","<description>","<projectadmin>"clicks on save button
    Examples:
     |name    |customername   | description    | projectadmin |
     |santosh |ACME Ltd       | ACME Ltd       | ACME Ltd     |





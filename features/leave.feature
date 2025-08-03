Feature: Leave

  Background:
    Given the user redirect to the login page
    When the user logging in with username "Admin" and password "admin123"
    When the user clicks on the leave menu and redirects to the leave page

  #apply
  @Apply
  Scenario Outline: Apply
    When the user clicks on Apply
    When the user selects leave type "<leave_type>" from dropdown of Apply
    When the user selects fromdate "<from_date>" from the calendar of Apply
    When the user selects todate "<to_date>" from the calendar of Apply
    When the user enters comments "<comments>" of Apply
    When the user clicks on the search button of Apply
    Examples: credentials
       | from_date | to_date  |  leave_type       | comments |
       |2025-01-07 |2025-02-07|  US - Vacation   | Testing  |

  #myleave
  @MyLeave
  Scenario Outline: My_Leave
    When the user clicks on My_Leave
    When the user selects fromdate "<from_date>" from the calendar of My_Leave
    When the user selects todate "<to_date>" from the calendar of My_Leave
    When the user selects leave type "<leave_type>" from dropdown of My_Leave
    When the user clicks on the search button of My_Leave
    Examples: credentials
       | from_date | to_date  |  leave_type       |
       |2025-01-01 |2025-31-12|  US - Bereavement |

  #Entitlements
  @AddEntitlements
  Scenario Outline: Entitlements_AddEntitlements
    When the user clicks on the Entitlements for Add_Entitlements
    When the user clicks on the Add_Entitlements
    When the user enters employee name "<employee_name>" of Add_Entitlements
    When the user clicks on the dropdown arrow and select leave type "<leave_type>" from dropdown of Add_Entitlements
    When the user clicks on the dropdown arrow and select leave period "<leave_period>" from dropdown of Add_Entitlements
    When the user enters entitlement in the particular field "<entitlement_data>" of Add_Entitlements
    When the user clicking on the save button of Add_Entitlements
    When the user clicking on the confirm button of Add_Entitlements
    Examples: credentials
        | employee_name |    leave_type    | leave_period            | entitlement_data |
        | Ranga  Akunuri |    CAN - FMLA    | 2026-01-01 - 2026-31-12 | 5.02             |

  @EmployeeEntitlements
  Scenario Outline: Leave Page_Entitlements_EmployeeEntitlements
    When the user clicking on the Entitlements for Employee_Entitlements
    When the user clicks on the EmployeeEntitlements
    When the user enters employee name "<employee_name>" of Employee_Entitlements
    When the user clicks on the dropdown arrow and select leavetype "<leave_type>" from dropdown of Employee_Entitlements
    When the user clicks on the dropdown arrow and select leaveperiod "<leave_period>" from dropdown of Employee_Entitlements
    When the user clicking on the search button of Employee_Entitlements

    Examples: credentials
       |  employee_name        |  leave_type       |  leave_period           |
       | Shree Sanju Bhosale | CAN - Matternity  | 2024-01-01 - 2024-31-12 |

  @MyEntitlements
  Scenario Outline: Leave Page_Entitlements_MyEntitlements
    When the user is on the Entitlements for My_Entitlements
    When the user clicks on the MyEntitlements
    When the user clicks on the dropdown arrow and select leavetype "<leave_type>" from dropdown of My_Entitlements
    When the user clicks on the dropdown arrow and select leaveperiod "<leave_period>" from dropdown of My_Entitlements
    When the user clicking on the search button of My_Entitlements

    Examples: credentials
        | leave_type        |  leave_period           |
        | CAN - Matternity  | 2025-01-01 - 2025-31-12 |

  #Reports
  @LeaveEntitlementsandUsageReport
  Scenario Outline: Reports_Leave_Entitlements_and_Usage_Report
    When the user is on the Reports for LeaveEntitlementsandUsageReport
    When the user clicks on the LeaveEntitlementsandUsageReport
    When the user clicking on the radio button of LeaveEntitlementsandUsageReport
    When the user enters employeename "<employee_name>" of LeaveEntitlementsandUsageReport
    When the user clicks on the dropdown arrow and select leaveperiod "<leave_period>" from dropdown of LeaveEntitlementsandUsageReport
    When the user clicking on the generate button of LeaveEntitlementsandUsageReport

    Examples: credentials
        | employee_name     |  leave_period           |
        | Ravi M B          | 2025-01-01 - 2025-31-12 |

  @MyLeaveEntitlementsandUsageReport
  Scenario Outline: Reports_Leave_Entitlements_and_Usage_Report
    When the user is on the Reports for MyLeaveEntitlementsandUsageReport
    When the user clicks on the MyLeaveEntitlementsandUsageReport
    When the user clicks on the dropdown arrow and select leaveperiod "<leave_period>" from dropdown of MyLeaveEntitlementsandUsageReport
    When the user clicking on the generate button of MyLeaveEntitlementsandUsageReport

    Examples: credentials
        |  leave_period           |
        | 2025-01-01 - 2025-31-12 |

  #configure
  @LeavePeriod
  Scenario Outline: configure_LeavePeriod
    When the user is on the configure for LeavePeriod
    When the user clicks on the LeavePeriod
    When the user selects startmonth "<start_month>" from the calendar of LeavePeriod
    When the user selects startdate "<start_date>" from the calendar of LeavePeriod
    When the user clicks on the save button of LeavePeriod

    Examples: credentials
       |start_month  | start_date  |
       |  June       |  30         |

  @LeaveTypes
  Scenario Outline: configure_LeaveTypes
    When the user is on the configure for LeaveTypes
    When the user clicks on the LeaveTypes
    When the user clicks on the add button of LeaveTypes
    When the user enters name "<name>" of LeaveTypes
    When the user clicks radiobutton of LeaveTypes
    When the user clicks on the save button of LeaveTypes

    Examples: credentials
       |     name               |
       |  CAN - Professional    |

  @WorkWeek
  Scenario Outline: configure_WorkWeek
    When the user is on the configure for WorkWeek
    When the user clicks on the WorkWeek
    When the user selects monday dropdown "<monday>" of WorkWeek
    When the user selects tuesday dropdown "<tuesday>" of WorkWeek
    When the user selects wednesday dropdown "<wednesday>" of WorkWeek
    When the user selects thursday dropdown "<thursday>" of WorkWeek
    When the user selects friday dropdown "<friday>" of WorkWeek
    When the user selects saturday dropdown "<saturday>" of WorkWeek
    When the user selects sunday dropdown "<sunday>" of WorkWeek
    When the user clicks on the save button of WorkWeek

    Examples: credentials
       |    monday    |tuesday | wednesday | thursday | friday   |  saturday       | sunday         |
       |  Full Day    |Full Day|  Full Day |Half Day  | Half Day | Non-working Day| Non-working Day |


  @Holidays
  Scenario Outline: configure_Holidays
    When the user is on the configure for Holidays
    When the user clicks on the Holidays
    When the user selects fromdate "<from_date>" from the calendar of Holidays
    When the user selects todate "<to_date>" from the calendar of Holidays
    When the user clicks on the search button of Holidays

    Examples: credentials
       |from_date  | to_date  |
       |2025-01-01 |2025-31-12|

  @LeaveList
  Scenario Outline: Leave_List
    When the user selects fromdate "<from_date>" from the calendar of leave_list
    When the user selects todate "<to_date>" from the calendar of leave_list
    When the user selects leave with status "<leave_with_status>" from dropdown of leave_list
    When the user selects leave type "<leave_type>" from dropdown of leave_list
    When the user enters employeename "<employee_name>" of leave_list
    When the user selects subunit "<sub_unit>" from dropdown of leave_list
    When the user clicks on the radio button of leave_list
    When the user clicks on the search button of leave_list

    Examples: credentials
       |from_date  | to_date  | leave_with_status| leave_type     |    employee_name      | sub_unit      |
       |2025-01-01 |2025-31-12|    Scheduled     | CAN - Personal |  Timothy Lewis Amiano |Administration |

  @AssignLeave
  Scenario Outline:
    When the user clicks on Assign_Leave and enters "<employee_name>","<leave_type>","<from_date>","<to_date>","<comments>"
    #When the user clicks on Assign_Leave
    #When the user enters employeename "<employee_name>" of Assign_Leave
    #When the user selects leave type "<leave_type>" from dropdown of Assign_Leave
    #When the user selects fromdate "<from_date>" from the calendar of Assign_Leave
    #When the user selects todate "<to_date>" from the calendar of Assign_Leave
    #When the user enters comments "<comments>" of Assign_Leave
    #When the user clicks on the assign button of Assign_Leave
    #When the user clicking on the confirm button of Assign_Leave

    Examples: credentials
       | employee_name  | leave_type     | from_date  | to_date  | comments |
       |  Ravi M B      |CAN - Vacation  |2025-01-01  |2025-31-12| testing  |

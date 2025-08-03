Feature: PIM

  Background:
    Given the user redirecting to the login page
    When the user logins in with username "Admin" and password "admin123"
    When the user clicks on the PIM menu and redirects to the PIM page


  #Configuration
  @Configuration_OptionalFields
  Scenario:
    When the user clicks on configuration for optionalfields and clicks on
    When the user clicks on optionalfields
    When the user clicks on showdeprecatedfields of optionalfields
    When the user clicks on ShowSSNfieldinPersonalDetails of optionalfields
    When the user clicks on ShowSINfieldinPersonalDetails of optionalfields
    When the user clicks on ShowUSTaxExemptionsmenu of optionalfields
    When the user clicks on savebutton of optionalfields

  @Configuration_CustomFields_save
  Scenario Outline:
    When the user clicks on configuration for CustomFields and enters "<fieldname>","<screen>","<type>" and clicks on save button
    Examples:
      | fieldname | screen             | type            |
      | Santosh   | Personal Details   | Text or Number  |

  @Configuration_CustomFields_cancel
  Scenario Outline:
    When the user clicks on configuration for CustomFields and enters "<fieldname>","<screen>","<type>" and clicks on cancel button
    Examples:
      | fieldname | screen             | type            |
      | Santosh   | Personal Details   | Text or Number  |


  @Configuration_CustomFields_list_checkbox_delete
  Scenario:
    When the user clicks on configuration for customfields and clicks on checkbox and clicks on alertcancel button

  @Configuration_CustomFields_list_deletebutton
  Scenario:
    When the user clicks on configuration for customfields and clicks on delete button of list and clicks on alertcancel button

  @Configuration_CustomFields_list_editbutton_save
  Scenario Outline:
    When the user clicks on configuration for customfields and clicks on edit button of list and performs edit "<name>" and clicks on save button
    Examples:
      | name      |
      | Santosh   |

  @Configuration_CustomFields_list_editbutton_cancel
  Scenario Outline:
    When the user clicks on configuration for customfields and clicks on edit button of list and performs edit "<name>" and clicks on cancel button
    Examples:
      | name      |
      | Santosh   |


  @Configuration_DataImport
  Scenario:
    When the user clicks on configuration for dataimport and uploads file

  @Configuration_ReportingMethods_save
  Scenario Outline:
    When the user clicks on configuration for reportingmethods and enters "<name>" and clicks on save button
    Examples:
      | name      |
      | Santosh   |

  @Configuration_ReportingMethods_cancel
  Scenario Outline:
    When the user clicks on configuration for reportingmethods and enters "<name>" and clicks on cancel button
    Examples:
      | name      |
      | Santosh   |

  @Configuration_ReportingMethods_list_checkbox_delete
  Scenario:
    When the user clicks on configuration for reportingmethods and clicks on checkbox and clicks on alertcancel button

  @Configuration_ReportingMethods_list_deletebutton
  Scenario:
    When the user clicks on configuration for reportingmethods and clicks on delete button of list and clicks on alertcancel button

  @Configuration_ReportingMethods_list_editbutton_save
  Scenario Outline:
    When the user clicks on configuration for reportingmethods and clicks on edit button of list and performs edit "<name>" and clicks on save button
    Examples:
      | name      |
      | Santosh   |

  @Configuration_ReportingMethods_list_editbutton_cancel
  Scenario Outline:
    When the user clicks on configuration for reportingmethods and clicks on edit button of list and performs edit "<name>" and clicks on cancel button
    Examples:
      | name      |
      | Santosh   |

  @Configuration_TerminationReasons_save
  Scenario Outline:
    When the user clicks on configuration for terminationreasons and enters "<name>" and clicks on save button
    Examples:
      | name                 |
      | Testing_Termination  |

  @Configuration_TerminationReasons_cancel
  Scenario Outline:
    When the user clicks on configuration for terminationreasons and enters "<name>" and clicks on cancel button
    Examples:
      | name                 |
      | Testing_Termination  |

  @Configuration_TerminationReasons_list_checkbox_delete
  Scenario:
    When the user clicks on configuration for terminationreasons and clicks on checkbox and clicks on alertcancel button

  @Configuration_TerminationReasons_list_deletebutton
  Scenario:
    When the user clicks on configuration for terminationreasons and clicks on delete button of list and clicks on alertcancel button

  @Configuration_TerminationReasons_list_editbutton_save
  Scenario Outline:
    When the user clicks on configuration for terminationreasons and clicks on edit button of list and performs edit "<name>" and clicks on save button
    Examples:
      | name      |
      | Santosh   |

  @Configuration_TerminationReasons_list_editbutton_cancel
  Scenario Outline:
    When the user clicks on configuration for terminationreasons and clicks on edit button of list and performs edit "<name>" and clicks on cancel button
    Examples:
      | name      |
      | Santosh   |







  @EmployeeList_save
  Scenario Outline:
    When the user clicks on employeelist and enters "<employeename>","<employeeid>","<employmentstatus>","<include>","<supervisorname>","<jobtitle>","<subunit>" clicks on save button
    Examples:
      | employeename       | employeeid | employmentstatus | include                    | supervisorname    | jobtitle           | subunit        |
      | santosh p patnana  | 0418       | Freelance        | Current and Past Employees | Darsghan  P       | Software Architect | Administration |

  @EmployeeList_cancel
  Scenario Outline:
    When the user clicks on employeelist and enters "<employeename>","<employeeid>","<employmentstatus>","<include>","<supervisorname>","<jobtitle>","<subunit>" clicks on cancel button
    Examples:
      | employeename       | employeeid | employmentstatus | include                    | supervisorname    | jobtitle           | subunit        |
      | santosh p patnana  | 0418       | Freelance        | Current and Past Employees | Darsghan  P       | Software Architect | Administration |

  @Employeelist_list_checkbox_delete
  Scenario:
    When the user clicks on employeelist and clicks on checkbox and clicks on alertcancel button

  @Employeelist_list_deletebutton
  Scenario:
    When the user clicks on employeelist and clicks on delete button of list and clicks on alertcancel button

  #@Employeelist_list_editbutton_save
  #Scenario:
    #When the user clicks on employeelist and clicks on edit button of list and clicks on save button

  #@Employeelist_list_editbutton_cancel
  #Scenario:
    #When the user clicks on employeelist and clicks on edit button of list and clicks on cancel button




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

  @Reports_save
  Scenario Outline:
    When the user clicks on reports enters "<ReportName>" and clicks on the save button
    Examples:
      | ReportName                 |
      |Employee Contact info report|

  @Reports_cancel
  Scenario Outline:
    When the user clicks on reports enters "<ReportName>" and clicks on the cancel button
    Examples:
      | ReportName                 |
      |Employee Contact info report|

  @Reports_add_save
  Scenario Outline:
    When the user clicks on reports and click on add button enters "<reportname>","<selectioncriteria>","<include>","<displayfieldgroup>","<displayfield>" and clicks on the save button
    Examples:
      | reportname    | selectioncriteria | include               | displayfieldgroup | displayfield |
      |Employee report| Employee Name     |Current Employees Only | Contact Details   | Mobile       |

  @Reports_add_cancel
  Scenario Outline:
    When the user clicks on reports and click on add button enters "<reportname>","<selectioncriteria>","<include>","<displayfieldgroup>","<displayfield>" and clicks on the cancel button
    Examples:
      | reportname    | selectioncriteria | include               | displayfieldgroup | displayfield |
      |Employee report| Employee Name     |Current Employees Only | Contact Details   | Mobile       |

  @Reports_list_checkbox_delete
  Scenario:
    When the user clicks on reports and clicks on checkbox and clicks on alertcancel button

  @Reports_list_deletebutton
  Scenario:
    When the user clicks on reports and clicks on delete button of list and clicks on alertcancel button

  @Reports_list_editbutton_save
  Scenario Outline:
    When the user clicks on reports and clicks on edit button of list and performs edit "<name>" and clicks on save button
    Examples:
      | name                         |
      |Employee Contact info report_1|

  @Reports_list_editbutton_cancel
  Scenario Outline:
    When the user clicks on reports and clicks on edit button of list and performs edit "<name>" and clicks on cancel button
    Examples:
      | name                         |
      |Employee Contact info report_1|

  @Reports_list_textfill
  Scenario:
    When the user clicks on reports and clicks on textfill button of list




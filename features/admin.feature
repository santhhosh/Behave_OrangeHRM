Feature: ADMIN

  Background:
    Given the user redirecting to the login page for Admin Module
    When the user logins in with username "Admin" and password "admin123" for Admin Module
    When the user clicks on the Admin menu and redirects to the Admin page for Admin Module

  @Users_add
  Scenario Outline:
    When the user clicks on usermanagement for users and clicks add and enters "<userrole>","<employeename>","<status>","<username>","<password>","<confirmpassword>"
    Examples:
      | userrole | employeename   | status  | username |  password   | confirmpassword |
      | Admin    |santosh  patnana| Enabled | santhosh | Santosh@123 |  Santosh@123    |

  @Systemusers
  Scenario Outline:
    When the user clicks on usermanagement for users and search and enters "<username>","<userrole>","<employeename>","<status>"
    Examples:
      | userrole | employeename    | status  | username |
      | Admin    |abcd Bortoluzzi| Enabled | Admin    |

  #Job_JobTitles
  @JobTitles_add_save
  Scenario Outline:
    When the user clicks on job for jobtitles and enters "<jobtitle>","<jobdescription>","<note>" and save
    Examples:
      | jobtitle | jobdescription    | note    |
      | Admin    | administrator     | Testing |

  @JobTitles_add_cancel
  Scenario Outline:
    When the user clicks on job for jobtitles and enters "<jobtitle>","<jobdescription>","<note>" and cancel
    Examples:
      | jobtitle | jobdescription    | note    |
      | Admin1    | administrator     | Testing |

  #Job_PayGrades
  @PayGrades_add_save
  Scenario Outline:
    #When the user clicks on job for paygrades and clicks on save button
    When the user clicks on job for paygrades and enters "<name>" and clicks on save button
    Examples:
      | name       |
      | Grade_11   |

  @PayGrades_add_cancel
  Scenario Outline:
    When the user clicks on job for paygrades and enters "<name>" and clicks on cancel button
    Examples:
      | name        |
      | Grade_12    |

  @PayGrades_checkbox_delete
  Scenario:
    When the user clicks on job for paygrades and clicks on checkbox and clicks on alertcancel button

  @PayGrades_list_deletebutton
  Scenario:
    When the user clicks on job for paygrades and clicks on deletebutton of list and clicks on alertcancel button

  @PayGrades_list_editbutton
  Scenario Outline:
    When the user clicks on job for paygrades and clicks on editbutton of list and edit "<name>" and clicks on save button
    Examples:
      | name        |
      | Grade_12    |


  #employmentstatus_add
  @EmploymentStatus_add_save
  Scenario Outline:
    When the user clicks on job for employmentstatus and enters "<name>" and clicks on save button
    Examples:
      | name               |
      | Testing_purpose    |

  @EmploymentStatus_add_cancel
  Scenario Outline:
    When the user clicks on job for employmentstatus and enters "<name>" and clicks on cancel button
    Examples:
      | name               |
      | Testing_purpose    |

  #JobCategories_add
  @JobCategories_add_save
  Scenario Outline:
    When the user clicks on job for jobcategories and enters "<name>" and clicks on save button
    Examples:
      | name               |
      | Testing_purpose    |

  @JobCategories_add_cancel
  Scenario Outline:
    When the user clicks on job for jobcategories and enters "<name>" and clicks on cancel button
    Examples:
      | name               |
      | Testing_purpose    |

  @Job_workshifts_add_save
  Scenario Outline:
    When the user clicks on job for workshifts and enters "<shiftname>","<fromtime>","<totime>","<assignedemployees>" and clicks on save button
    Examples:
      | shiftname | fromtime | totime  | assignedemployees |
      | Morning   | 10:00 AM |07:00 PM | Mohammed Zikria   |

  @Job_workshifts_add_cancel
  Scenario Outline:
    When the user clicks on job for workshifts and enters "<shiftname>","<fromtime>","<totime>","<assignedemployees>" and clicks on cancel button
    Examples:
      | shiftname | fromtime | totime  | assignedemployees |
      | Morning   | 10:00 AM |07:00 PM | Mohammed Zikria   |

  @Job_workshifts_checkbox_delete
  Scenario:
    When the user clicks on job for workshifts and clicks on checkbox and clicks on alertcancel button

  @Job_workshifts_list_deletebutton
  Scenario:
    When the user clicks on job for workshifts and clicks on delete button of list and clicks on alertcancel button

  @Job_workshifts_list_editbutton_save
  Scenario Outline:
    When the user clicks on job for workshifts and clicks on edit button of list and performs edit "<name>" and clicks on save button
    Examples:
      | name      |
      | General   |

  @Job_workshifts_list_editbutton_cancel
  Scenario Outline:
    When the user clicks on job for workshifts and clicks on edit button of list and performs edit "<name>" and clicks on cancel button
    Examples:
      | name     |
      | General  |

  @Organization_Locations_Save
  Scenario Outline:
    When the user clicks on organization for locations and enters "<name>","<city>","<country>" and clicks on save button
    Examples:
      | name      | city      | country   |
      | Tower2    | Hyderabad |Afghanistan|

  @Organization_Locations_Cancel
  Scenario Outline:
    When the user clicks on organization for locations and enters "<name>","<city>","<country>" and clicks on cancel button
    Examples:
      | name      | city      | country   |
      | Tower2    | Hyderabad |Afghanistan|

  @Organization_Locations_Add_Save
  Scenario Outline:
    When the user clicks on organization for locations and enters "<name>","<city>","<state>","<postal>","<country>","<phone>","<fax>","<address>","<notes>"and clicks on save button
    Examples:
      | name        | city      | state    | postal | country      | phone     | fax       | address  | notes   |
      | Hitech city | Hyderabad | Telangana| 500084 | Afghanistan  | 9848032919| 9848032910| Hyderabad| Testing |

  @Organization_Locations_Add_Cancel
  Scenario Outline:
    When the user clicks on organization for locations and enters "<name>","<city>","<state>","<postal>","<country>","<phone>","<fax>","<address>","<notes>"and clicks on cancel button
    Examples:
      | name        | city      | state    | postal | country     | phone     | fax       | address  | notes   |
      | Hitech city | Hyderabad | Telangana| 500084 | Afghanistan | 9848032919| 9848032910| Hyderabad| Testing |

  @Organization_Locations_checkbox_delete
  Scenario:
    When the user clicks on organization for locations and clicks on checkbox and clicks on alertcancel button

  @Qualifications_Skills_add_save
  Scenario Outline:
    When the user clicks on qualifications for skills and enters "<name>","<description>" and clicks on save button
    Examples:
      | name      | description     |
      | Jmeter    | testing purpose |

  @Qualifications_Skills_add_cancel
  Scenario Outline:
    When the user clicks on qualifications for skills and enters "<name>","<description>" and clicks on cancel button
    Examples:
      | name      | description     |
      | Jmeter    | testing purpose |

  @Qualifications_Education_add_save
  Scenario Outline:
    When the user clicks on qualifications for education and enters "<level>" and clicks on save button
    Examples:
      | level        |
      | kindergarten |

  @Qualifications_Education_add_cancel
  Scenario Outline:
    When the user clicks on qualifications for education and enters "<level>" and clicks on cancel button
    Examples:
      | level          |
      | kindergarten_1 |

  @Qualifications_Education_list_checkbox_delete
  Scenario:
    When the user clicks on qualifications for education and clicks on checkbox and clicks on alertcancel button

  @Qualifications_Education_list_deletebutton
  Scenario:
    When the user clicks on qualifications for education and clicks on delete button of list and clicks on alertcancel button

  @Qualifications_Licenses_add_save
  Scenario Outline:
    When the user clicks on qualifications for licenses and enters "<name>" and clicks on save button
    Examples:
      | name                                             |
      | Corps Information Systems Control Officer(CISCO) |

  @Qualifications_Licenses_add_cancel
  Scenario Outline:
    When the user clicks on qualifications for licenses and enters "<name>" and clicks on cancel button
    Examples:
      | name                                             |
      | Corps Information Systems Control Officer(CISCO) |

  @Qualifications_Languages_add_save
  Scenario Outline:
    When the user clicks on qualifications for languages and enters "<name>" and clicks on save button
    Examples:
      | name   |
      | Telugu |

  @Qualifications_Languages_add_cancel
  Scenario Outline:
    When the user clicks on qualifications for languages and enters "<name>" and clicks on cancel button
    Examples:
      | name   |
      | Telugu |

  @Qualifications_memberships_add_save
  Scenario Outline:
    When the user clicks on qualifications for memberships and enters "<name>" and clicks on save button
    Examples:
      | name   |
      | BCA    |

  @Qualifications_memberships_add_cancel
  Scenario Outline:
    When the user clicks on qualifications for memberships and enters "<name>" and clicks on cancel button
    Examples:
      | name   |
      | BBA    |

  #@myinfo_download
  #Scenario:
    #When the user clicks on myinfo and clicks on download button

  @Nationalities_add_save
  Scenario Outline:
    When the user clicks on nationalities and enters "<name>" and clicks on save button
    Examples:
      | name         |
      | Bharateeyudu |

  @Nationalities_add_cancel
  Scenario Outline:
    When the user clicks on nationalities and enters "<name>" and clicks on cancel button
    Examples:
      | name         |
      | Anglo-Indian |

  @Nationalities_list_checkbox_delete
  Scenario:
    When the user clicks on nationalities and clicks on checkbox and clicks on alertcancel button

  @Nationalities_list_deletebutton
  Scenario:
    When the user clicks on nationalities and clicks on delete button of list and clicks on alertcancel button

  @Nationalities_list_editbutton_save
  Scenario Outline:
    When the user clicks on nationalities and clicks on edit button of list and performs edit "<name>" and clicks on save button
    Examples:
      | name         |
      | American     |

  @Nationalities_list_editbutton_cancel
  Scenario Outline:
    When the user clicks on nationalities and clicks on edit button of list and performs edit "<name>" and clicks on cancel button
    Examples:
      | name         |
      | American     |

Feature: RECRUITMENT

  Background:
    Given the user redirecting to the login page for Recruitment Module
    When the user logins in with username "Admin" and password "admin123" for Recruitment Module
    When the user clicks on the Recruitment menu and redirects to the Recruitment page for Recruitment Module



  @Recruitment_Candidates_form
  Scenario Outline: Candidate form submission with action
  When the user clicks candidates and selects "<jobtitle>","<vacancy>","<hiringmanager>","<status>","<keywords>","<fromdate>","<todate>","<methodofapplication>","<action>"

    Examples:
      | jobtitle          | vacancy        | hiringmanager | status               | keywords | fromdate  | todate    | methodofapplication | action |
      | Account Assistant | Senior QA Lead | Rahul Patil   | Application Initiated| testing  | 2025-07-17| 2025-08-30| Manual              | save   |
      | Account Assistant | Senior QA Lead | Rahul Patil   | Application Initiated| testing  | 2025-07-17| 2025-08-30| Manual              | cancel |

  @Recruitment_Candidates_addbutton
  Scenario Outline:
    When the user clicks on candidates and clicks on add button and selects "<firstname>","<middlename>","<lastname>","<vacancy>","<email>","<contactnumber>","<path>",<keywords>","<fromdate>","<notes>","<action>"
    Examples:
      | firstname | middlename | lastname | vacancy               | email        |contactnumber|keywords| fromdate | notes           | action |
      | Madhu     | Sudhan     | Rao      | Payroll Administrator | sss@gmail.com|  9998887776 | Testing|2025-06-30| Testing Purpose | save   |
      | Madhu     | Sudhan     | Rao      | Payroll Administrator | sss@gmail.com|  9998887776 |Testing |2025-06-30| Testing Purpose | cancel |





  @Candidates_list_checkbox_delete
  Scenario:
    When the user clicks on candidates and clicks on checkbox and clicks on alertcancel button

  @Candidates_list_delete_button
  Scenario:
    When the user clicks on candidates and clicks on delete button and clicks on alertcancel button

  @Candidates_list_eye_button
  Scenario:
    When the user clicks on candidates and clicks on eye button

  @Recruitment_Vacancies_form
  Scenario Outline: Vacancies form submission with action
  When the user clicks candidates and selects "<jobtitle>","<vacancy>","<hiringmanager>","<status>","<action>"

    Examples:
      | jobtitle          | vacancy        | hiringmanager | status| action |
      | Account Assistant | Senior QA Lead | Rahul Patil   | Active| save   |
      | Account Assistant | Senior QA Lead | Rahul Patil   | Active| cancel |

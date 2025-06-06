Feature: Login functionality

  Background:
    Given the user is on the login page

  @login
  Scenario Outline: Login with various username and password combinations
    When the user enters username "<username>"
    And the user enters password "<password>"
    And the user clicks on the login button
    Then the user must be able to login to the dashboard successfully "<expected_result>"

    Examples:
      | username | password  | expected_result     |
      | Admin    | admin123  | Dashboard           |
      | Admin1   | admin123  | Invalid credentials |
      | Admin    | admin1234 | Invalid credentials |
      | Admin1   | admin1234 | Invalid credentials |

  @forgotpassword
  Scenario Outline: Forgot Password Functionality
    When the user clicks on the Forgot Password link
    And the user enters username "<username_1>" to reset password
    Then the user clicks on the reset password button

    Examples:
      | username_1 |
      | Admin      |

  @icon_links
  Scenario Outline: Login page different icons
    When the user clicks on the "<Icon>" link

    Examples:
      | Icon     |
      | Linkedin |
      | Facebook |
      | Youtube  |
      | Twitter  |

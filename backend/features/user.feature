# [1] https://docs.djangoproject.com/en/2.1/topics/auth/default/
# [2] https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#substituting-a-custom-user-mode
# [3] https://www.linkedin.com/pulse/django-2-register-authenticate-users-email-george-bikas/
# [4] https://github.com/tmm/django-username-email/
# [5] https://github.com/tmm/django-username-email/blob/master/cuser/models.py
Feature: User interacts with the system
  # very broad overview, skim and go back when you're ready: [1]
  # to extend user with your own fields: [2]
  Scenario: User can log in
    # Q: how can we get rid of Django's default username field? Check [2] and [3]
    # Ambitious: check how CUser does this and read models code with a mentor [5], also read README [4]
    Given user with email 'user@example.com' with password 'pass' exists
    When user visits the log in page
    # Check if rendered form has <input> tags with proper ids
    Then a form asking for email and password displays
    And no username is displayed in login form
    # How does django signal user logged in, by default? Check redirect and what else?
    And user can log in
    And user is redirected to home page

#  Scenario: User can log out
#    Given user with email 'user@example.com' with password 'pass' exists
#    When user visits the log out page
#    Then user can log out
#    # This depends on yout UX, this redirect is not a must-have, where else can user be redirected?
#    And user is redirected to log in page
#
#  Scenario: User can see main page
#    Given user with email 'user@example.com' with password 'pass' exists
#    And user is logged in
#    And user navigates to main page
#    # what should be on the home page?
#    Then user sees home page





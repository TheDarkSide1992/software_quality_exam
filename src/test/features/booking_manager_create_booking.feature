
Feature: Scenario outlines
    Scenario Outline: Create a booking successfully
        Given A booking starting on <start_date>
        And Ending on <end_date>
        When The booking is created
        Then The booking should be created successfully

        Examples:
          | start_date  | end_date  |
          | 5           | 7         |
          | 2           | 3         |
          | 21          | 25        |


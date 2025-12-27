
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

    Scenario Outline: Create a booking with invalid dates
         Given A booking starting on <start_date>
          And Ending on <end_date>
          When the booking fails to be created
          Then there should be an error message indicating invalid dates
      Examples:
        | start_date | end_date |
        | -20        | 0        |
        | -1         | 10       |
        | 25         | 5        |

    Scenario Outline: Create booking fully occupied
        Given A booking starting on <start_date>
        And Ending on <end_date>
        When The booking is created
        Then The booking should not be be created due to full occupancy

        Examples:
          | start_date  | end_date  |
          | 10          | 15        |
          | 12          | 14        |
          | 11          | 13        |
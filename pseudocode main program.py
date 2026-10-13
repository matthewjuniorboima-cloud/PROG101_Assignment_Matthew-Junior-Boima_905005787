Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> START Main
... CONSTANT MAX QUEUE = 100, MIN AGE = 0, MAX AGE = 120
... CONSTANT MIN TEMP = 34.0, MAX TEMP = 43.0
... CONSTANT FEVER TEMP = 38.0, EMERGENCY TEMP = 39.5
... CONSTANT CHILD_AGE = 5, ELDERLY AGE = 65
... SET queue = empty list
... SET ticketCounter = 0, servedCount = 0
... SET running = TRUE
... WHILE running = TRUE DO
... CALL displayMenu()
... INPUT choice
... IF choice = 1 THEN
... CALL registerPatient()
... ELSE IF choice = 2 THEN
... CALL callNextPatient()
... ELSE IF choice = 3 THEN
... CALL displayQueue()
... ELSE IF choice = 4 THEN
... CALL generateDailyReport()
... ELSE IF choice = 5 THEN
... SET running = FALSE
... ELSE
... OUTPUT "Invalid choice. Enter 1 to 5."
... END IF
... END WHILE
... OUTPUT "System closed. Stay safe."

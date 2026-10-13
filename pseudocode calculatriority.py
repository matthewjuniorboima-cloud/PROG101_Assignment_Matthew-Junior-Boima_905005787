Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> FUNCTION calculatePriority(age, temp, hasDangerSign, isPregnant)
... SET isEmergency = hasDangerSign OR temp >= EMERGENCY TEMP
... OR (age < CHILD AGE AND temp >= FEVER TEMP)
... SET isVulnerable = isPregnant OR age < CHILD AGE OR age >= ELDERLY AGE
... IF isEmergency = TRUE THEN
... RETURN 1
... ELSE IF isVulnerable = TRUE OR temp >= FEVER TEMP THEN
... RETURN 2
... ELSE
... RETURN 3
... END IF

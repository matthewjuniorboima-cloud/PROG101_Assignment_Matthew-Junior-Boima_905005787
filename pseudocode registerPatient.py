Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> FUNCTION registerPatient()
... IF size(queue) >= MAX QUEUE THEN
... OUTPUT "Queue full. Refer patient to nearest facility."
... RETURN
... END IF
... INPUT name
... REPEAT
... INPUT age
... IF age < MIN AGE OR age > MAX AGE THEN
... OUTPUT "Invalid age. Try again."
... END IF
... UNTIL age >= MIN AGE AND age <= MAX AGE
... REPEAT
... INPUT temp
... IF temp < MIN TEMP OR temp > MAX TEMP THEN
... OUTPUT "Invalid temperature. Try again."
... END IF
... UNTIL temp >= MIN TEMP AND temp <= MAX TEMP
... INPUT hasDangerSign, isPregnant
... SET priority = calculatePriority(age, temp, hasDangerSign, isPregnant)
... SET ticketCounter = ticketCounter + 1
... SET patient = (ticketCounter, name, age, priority)
... CALL insertInQueue(patient)
... OUTPUT "Ticket", ticketCounter, "Priority", priority

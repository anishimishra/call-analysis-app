Question 1 : Profanity Detection
Pattern Matching with a Predefined Profanity List
1. Read words from a text file ( e.g., profanity_list.txt )
2. Match each transcript utterance against this list
3. Flag detected profanity
Why?
1. Fast and lightweight for known profanity
2. Easy to update the list for specific use cases
3. Suitable for real-time detection

Question 2 : Privacy & Compliance Check
1. Define Rules for sensitive information
2. Regular expressions to detect patterns like SSNs, DOBs, phone numbers.
3. Trigger compliance violations on detection.
Why?
1. Rule-based detection ensures regulatory coverage.
2. Transparent logic for audit and governance.

Question 3 : Visualization Analysis
Metrics Visualized : 

a) Silence Percentage Chart
1. Measures how much of the conversation is silence
2. Helps evaluate:
   1. Call engagement level.
   2. Poorly trained agents causing excessive silence.

b) Overtalk Percentage Chart
1. Captures periods when both Agent and Customer speak simultaneously
2. Indicates lack of listening skills.
3. Indicates aggressive behavior or emotional tension in the call

Used bar charts to indicate.

# EXCHANGE_RATE_TRACKER
This is a python automation project  that fetches the exchange rate for (US) dollars to (NGN) naira, and saves the results to a json file.
And the program was made to run on schedule, that is, it has a time it will run and then save the results to the json file.
The program was also made to send and email message to the user email, that is for each time it runs the user will receive an email message, containing the result that was saved to the json file. 
But how come about the email message? Before the program was made to send the email message, i first created a new email account specifically for this project then i linked the email to an app that is how i was able to generate the password i used in gitub secret,
the github secret contain. Reciever email, email address,and the email password i got from the new email i created that i mentioned earlier.

FETURES
.Fetches the latest USD to NGN exchange rate.
.Saves exchange rate data to exchange_rate.json.
.Runs automatically on a schedule using GitHub Actions.
.Sends an email notification after each successful update.
.Uses GitHub Secrets to securely store email credentials.
.Skips unnecessary commits when no changes are detected.

#THE TOOLS I USED
Python
Git
Git action
json
Exchange rate api



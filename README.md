 Python Exchange Rate Automation Project

This is a Python automation project that fetches the exchange rate for US Dollars (USD) to Nigerian Naira (NGN) and saves the results to a JSON file.

## How It Works

1. **Scheduled Runs:** The program is set up to run automatically on a schedule. Every time it runs, it saves the latest results to a JSON file.
2. **Email Notifications:** The program also sends an email message to the user each time it runs, containing the exchange rate results that were saved.

### Setting Up the Email & Security

To make the email feature work safely, I created a new email account specifically for this project.

* I linked that email to an app to generate a unique **App Password**.
* I stored that password and the email addresses securely using **GitHub Secrets** so they aren't exposed in the code.
* The GitHub Secrets include: `RECEIVER_EMAIL`, `SENDER_EMAIL`, and the generated email password.

---

## Features

* Fetches the latest USD to NGN exchange rate.
* Saves exchange rate data to `exchange_rate.json`.
* Runs automatically on a schedule using GitHub Actions.
* Sends an email notification after each successful update.
* Uses GitHub Secrets to securely store email credentials.
* Skips unnecessary commits when no changes are detected.

---

## Tools Used

* **Python**
* **Git**
* **GitHub Actions**
* **JSON**
* **Exchange Rate API**

---

### 🛠️ How to Run It Locally

1. Clone this repository.
2. Install any required libraries (like `requests` if you are using it).
3. Run the main Python script:

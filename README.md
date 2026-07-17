## PYTHON EXCHANGE_RATE_TRACKER AUTOMATION PROJECT ##

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

## 🛠️ How to Run It Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/Exchange_Rate_Tracker.git
```

2. Navigate into the project folder:

```bash
cd Exchange_Rate_Tracker
```

3. (Optional but recommended) Create a virtual environment:

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install all required dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add your email credentials:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
RECEIVER_EMAIL=receiver@gmail.com
```

6. Run the application:

```bash
python main.py



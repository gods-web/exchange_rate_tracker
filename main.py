import requests
import json
from datetime import datetime 
import os
import smtplib

from dotenv import load_dotenv
load_dotenv
from email.message import EmailMessage
load_dotenv()

def send_email(subject, body):
    email = EmailMessage()
    email.set_content(body)
    email['subject'] = subject
    sender = os.environ['EMAIL_ADDRESS']
    receiver = os.environ['RECEIVER_EMAIL']
    password = os.environ['EMAIL_PASSWORD']
    email['from'] = sender
    email['to'] = receiver
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(email)
    server.quit()


url = ("https://open.er-api.com/v6/latest/usd")
    
    
def convert_from_USD_to_NGN():
    try:
        
            
            response = requests.get(url)
            data = response.json()
        
                
                
            rate = data["rates"]["NGN"]

            current_time = data["time_last_update_utc"]
            current_time = datetime.strptime(current_time, "%a, %d %b %Y %H:%M:%S %z")


        
            record = {"currency": "NGN",
                        "rate": rate,
                        "date": current_time.date().isoformat()
                        }
            print(record)
            return record
    except Exception as e:
        print(f"An error occurred while running this,{e}")
        
def save_to_json(record):    
        folder = os.getcwd()
        path = os.path.join(folder, "exchange_rate.json")

        if os.path.exists(path):
            with open("exchange_rate.json", "r") as f:
                history = json.load(f)
            if record not in history:
                history.append(record)
    
            with open("exchange_rate.json", "w") as f:
                    json.dump(history,f, indent=4)

        else:
            with open("exchange_rate.json", "w") as f:
                    json.dump([record],f, indent=4)

            
def main():
      naira_value = convert_from_USD_to_NGN()
      save_to_json(naira_value)
      send_email("convert_from_USD_to_NGN",f"{naira_value}")

main()
                
   
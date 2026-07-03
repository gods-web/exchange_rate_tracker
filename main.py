import requests
import json
from datetime import datetime 
import os


url = ("https://open.er-api.com/v6/latest/usd")
    
    
def convert_from_USD_to_NGN():
    try:
        
            
            response = requests.get(url)
            data = response.json()
        
                
                
            rate = data["rates"]["NGN"]

            current_time = data["time_last_update_utc"]
            current_time = datetime.striptime(current_time, "%a, %d %b %Y %H:%M:%S %z")


        
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
        path = os.path.join(folder, "history.json")

        if os.path.exists(path):
            with open("history.json", "r") as f:
                history = json.load(f)
        if record not in history:
            history.append(record)
    
            with open("history.json", "w") as f:
                    json.dump(history,f, indent=4)

        else:
            with open("history.json", "w") as f:
                    json.dump([record],f, indent=4)

            
def main():
      naira_value = convert_from_USD_to_NGN(1)
      save_to_json(naira_value)

main()
                
   
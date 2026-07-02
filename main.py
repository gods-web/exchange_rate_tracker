import requests
import json 
import datetime
import os
from datetime import datetime



url = ("https://open.er-api.com/v6/latest/usd")
    
    
def convert_from_USD_to_NGN(USD):
    try:
        
            
            response = requests.get(url)
            data = response.json()
                
                
            rate = data["rates"]["NGN"]
            last_update = data["time_last_update_utc"]
            NGN = rate * USD
            current_time = datetime.now()


            print("Time:", current_time)
                

            record = {"usd": USD,
                        "ngn": NGN,
                        "rate": rate,
                        "last_rate_update": last_update,
                        "time": str(current_time)
                        }
                
            os.path.exists("history.json")
            with open("history.json", "w") as f:
                json.dump([], f)
    

            with open("history.json", "r") as f:
                        history = json.load(f)
                        history.append(record)

            with open("history.json", "w")as f:
                    json.dump(history,f, indent=4)

                
            return NGN,last_update
    except requests.exceptions.RequestException as e:
        print("An error occured while fetching your request", e)
        return None
    
    
output = convert_from_USD_to_NGN(10)
print(output)




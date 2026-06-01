import csv
import requests
import os
import configparser
import pandas as pd
import random
import time 
from pathlib import Path

def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
    
def sleep_random_number(start=99,end=299):
    r_number = random.randint(start,end)
    print(f"Pause for {r_number} Seconds")
    time.sleep(r_number)
def add_country_code(contact,ccode):
    if len(str(contact)) == 10:
        return str(ccode)+str(contact).strip()
    else :
        return contact
def get_config(file_path="config.ini"):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config 
def identify_message_type_file(file_path):
    filename, file_extension = os.path.splitext(file_path)
    if file_extension in ["mp4",".3gp",".mov"] :
        return "video"
    elif file_extension in ["pdf","ppt","pptx","docx","doc"]:
        return "document"
    else:
        return None
def identify_message_type_ini(config):
    video_path = Path(config.get("Video","video_path"))
    pdf_file_path = Path(config.get("document","pdf_path"))
    if video_path and video_path.exists() :
        return "video", video_path
    elif pdf_file_path and pdf_file_path.exists():
        return "document" , pdf_file_path
    else :
        return None
def send_message(row,config,template_message) :
    
    contact = row.get("contact")
    contact = add_country_code(contact,ccode)
    if not check_number_exists(contact):
        print(f"Contact {contact} not avilable in the whatsapp")
        return "no_whatsapp"
    file_path = row.get("file_path")
    name = row.get("name")
    message = template_message.replace('{name}', name)
    if file_path and os.path.exists(file_path):
        media_type = identify_message_type_file(file_path)
        #check in the config  for attachement 
    else :
        media_type , file_path = identify_message_type_ini(config)
    if media_type == "document" :
        send_pdf_message(name,contact,file_path,message)
    elif media_type == "video" :
        send_video_message(name,contact,file_path,message)
    else : 
        return "wrong_media"
    sleep_random_number(25,150)
    return "success"
    #Check if CSV has the file tye
        #Check its type 
    #If csv does not have a file path then get the type n details from .env 

    #as per the task send message with details 
    pass 
def check_number_exists(contact):
    url = f"{API_URL}/chat/whatsappNumbers/{INSTANCE_NAME}"
    payload = {"numbers": [str(contact)]}
    headers = {
        "apikey": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            valid_numbers = data[0].get("exists", {})
            if valid_numbers:
                return True 
            else :
                return False
        else:
            print(f"[!] Number check failed ({contact}): {response.status_code}")
            return False
    except Exception as e:
        print(f"[!] Error checking number {contact}: {e}")
        return False
def send_video_message(name,contact, file_path,message):
        print(f"Trying to send video message to {name}")
        headers = {
            "apikey": API_KEY,
            "Content-Type": "application/json"
        }
        # message = f"Hello {name},\nPlease find your personalized invitation attached!"
        # 2️⃣ Send Video  file
        if file_path.exists():
            files = {'file': open(file_path, 'rb')}
            
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f, "video/mp4")}

                data = {
                    "number": str(contact),
                    "mediatype": "video",             # Important: type of media
                    "mimetype": "video/mp4",       # MIME type
                    "caption": message.splitlines()[0] if message.strip() else "" ,# Custom caption
                    "fileName": os.path.basename(file_path)
                }

                response = requests.post(
                    f"{API_URL}/message/sendMedia/{INSTANCE_NAME}",
                    headers={"apikey": API_KEY},
                    data=data,
                    files=files
                )
           
            print(f"[+] Video sent to {name}: {response.status_code}")
             # 1️⃣ Send text message
            msg_data = {
                "number": str(contact),
                "text": message
            }
            response = requests.post(
                f"{API_URL}/message/sendText/{INSTANCE_NAME}",
                headers=headers,
                json=msg_data
            )
            print(f"[+] Message sent to {name}: {response.status_code}")

        else:
            print(f"[!] File not found for {name}: {file_path}")
# === Function to send message ===
def send_pdf_message(name, contact,file_path,message):
        print(f"Trying to send pdf message to {name}")
        headers = {
            "apikey": API_KEY,
            "Content-Type": "application/json"
        }
        # message = f"Hello {name},\nPlease find your personalized invitation attached!"
        # 2️⃣ Send PDF file
        if file_path.exists(file_path):
            files = {'file': open(file_path, 'rb')}
            
            with open(file_path, "rb") as f:
                files = {"file": (os.path.basename(file_path), f, "application/pdf")}

                data = {
                    "number": str(contact),
                    "mediatype": "document",             # Important: type of media
                    "mimetype": "application/pdf",       # MIME type
                    "caption": message.splitlines()[0] if message.strip() else "" ,# Custom caption
                    "fileName": os.path.basename(file_path)
                }

                response = requests.post(
                    f"{API_URL}/message/sendMedia/{INSTANCE_NAME}",
                    headers={"apikey": API_KEY},
                    data=data,
                    files=files
                )
           
            print(f"[+] PDF sent to {name}: {response.status_code}")
             # 1️⃣ Send text message
            msg_data = {
                "number": str(contact),
                "text": message
            }
            response = requests.post(
                f"{API_URL}/message/sendText/{INSTANCE_NAME}",
                headers=headers,
                json=msg_data
            )
            print(f"[+] Message sent to {name}: {response.status_code}")

        else:
            print(f"[!] File not found for {name}: {file_path}")

# === Read CSV and send ===
config = get_config(os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini'))
CSV_PATH = Path(config.get("INVITATION","GUEST_CSV"))
ccode = config.get("INVITATION","COUNTRY_CODE")
INSTANCE_NAME = config.get("Evolution_API","INSTANCE_NAME")
API_KEY = config.get("Evolution_API","API_KEY")
API_URL = config.get("Evolution_API","SERVER_URL")
OUTPUT_CSV = Path(config.get("INVITATION","OUTPUT_CSV"))
TEMPLATE_PATH  = Path(config.get("INVITATION","Template"))
INVITATION_MESSAGE = load_template(TEMPLATE_PATH)


df = pd.read_csv(CSV_PATH)
if "whatsapp_status" not in df.columns:
    df["whatsapp_status"] = ""
for idx, row in df.iterrows():
    #Random sleep to prevent block from meta 
    whatsapp_status = str(row.get("whatsapp_status"))
    if whatsapp_status.lower()  == "success" :
        continue
    name = row.get("name")
    contact = row.get("contact")
    file_path = row.get("file_path")
    if not contact or pd.isna(contact):
        print(f"[!] Missing number for {name}")
        df.at[idx, "whatsapp_status"] = "Failed (No number)"
        continue
    result = send_message(row, config, INVITATION_MESSAGE)
    df.at[idx, "whatsapp_status"] = result

df.to_csv(OUTPUT_CSV, index=False,  encoding='utf-8')
print("\n✅ CSV updated with WhatsApp message status.")
import requests
import schedule
import time
import sys
import argparse
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument("interval", help="notification interval in minutes", type=int)
parser.add_argument("folder", help="path to folder with preview files")
parser.add_argument("token", help="Slack access token")
parser.add_argument("channel", help="ID of Slack channel to upload files")
args = parser.parse_args()

URL = "https://slack.com/api/files.upload"

def get_latest_file_and_send_to_slack():
	try: 
		list_of_files = glob.glob(args.folder + "/*")
		latest_file = max(list_of_files, key=os.path.getctime)
		print("Upload the file:", latest_file)
		data = {
			"channels": args.channel
		}
		files = {"file": open(latest_file, 'rb')}
		headers = {
			"Authorization": "Bearer " + args.token
		}
		requests.post(URL, data=data, files=files, headers=headers)
	except: 
		print("No file to upload")


schedule.every(args.interval).minutes.do(get_latest_file_and_send_to_slack) 

while True: 
    schedule.run_pending() 
    time.sleep(1) 


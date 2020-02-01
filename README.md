# modelwatch

ModelWatch sends model training progress updates to your Slack channel. No SDK required, the script simply checks a folder that you pass in at your desired notification interval and uploads the newest file in that folder to Slack.

First you need to install the Slack App (you can also create your own and install that into your workspace): https://slack.com/oauth/v2/authorize?client_id=923693895510.919675746625&scope=files:write,incoming-webhook,chat:write

After installation, an Oauth token will be posted to your Slack channel, which you'll need to run the script.

Then install requirements and run the modelwatch.py script while training your model.

**modelwatch.py arguments:**
interval    notification interval in minutes
folder      path to folder with preview files
token       Slack access token
channel     ID of Slack channel to upload files

### Important

Run modelwatch.py in the background or else the thread may get blocked and you won't receive the updates at the expected interval.

On Windows:

    start python {interval} {folder} {token} {channel}

On macOS/Linux:

    python {interval} {folder} {token} {channel} &
  

  
 
  
  


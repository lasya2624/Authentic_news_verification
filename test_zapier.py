import requests
import json
from datetime import datetime

# Paste your actual Zapier Webhook URL here
ZAPIER_WEBHOOK_URL = 'https://hooks.zapier.com/hooks/catch/24943492/ur29grl/'

payload = {
    'username': 'test_user',
    'email': 'test@example.com',
    'subscription_date': datetime.now().isoformat()
}
headers = {'Content-Type': 'application/json'}

print(f"Attempting to send test data to: {ZAPIER_WEBHOOK_URL}")

try:
    response = requests.post(ZAPIER_WEBHOOK_URL, data=json.dumps(payload), headers=headers, timeout=10)
    
    # A status code of 200 means success
    if response.status_code == 200:
        print("\nSUCCESS! The request was received by Zapier.")
        print(f"Response from Zapier: {response.text}")
    else:
        print(f"\nFAILURE! The request was sent, but Zapier responded with an error.")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

except requests.exceptions.RequestException as e:
    print(f"\nCRITICAL FAILURE! The request could not be sent from your computer.")
    print(f"Error: {e}")


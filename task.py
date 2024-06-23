from reclaim_sdk.client import ReclaimClient
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("RECLAIM_TOKEN")

# Initialize the Reclaim client with your token
reclaim_client = ReclaimClient(token=token)

if __name__ == "__main__":
    try:
        task_id = "6801408"  # Replace with the actual task ID
        url = f"{reclaim_client._api_url}/api/tasks/{task_id}"
        
        # Using the ReclaimClient instance to make the GET request
        res = reclaim_client.get(url)

        # Check if the request was successful (status code 200)
        if res.status_code == 200:
            task_data = res.json()
            print("Task Data:")
            print(task_data)
            print("Task prioritized successfully!")
        else:
            print(f"Failed to prioritize task. Status code: {res.status_code}")

    except Exception as e:
        print(f"Error: {str(e)}")

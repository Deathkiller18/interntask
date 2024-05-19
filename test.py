import requests
import threading
import time

# URL of the API endpoint
API_URL = 'http://localhost:5000/generate'

# Number of concurrent users to simulate
NUM_USERS = 30

# Test input texts
INPUT_TEXTS = "This is a sample input text"
    # Add more test input texts as needed


# Function to send a request to the API endpoint
def send_request(input_text):
    payload = {'input_text': input_text}
    start_time = time.time()
    response = requests.post(API_URL, json=payload)
    end_time = time.time()
    response_time = end_time - start_time

    if response.status_code == 200:
        print(f"Response time: {response_time:.2f} seconds")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Function to simulate a user
def simulate_user(user_id):
    input_text = INPUT_TEXTS[user_id % len(INPUT_TEXTS)]
    send_request(input_text)

if __name__ == '__main__':

    # Create and start threads for simulating users
    threads = []
    for user_id in range(NUM_USERS):
        thread = threading.Thread(target=simulate_user, args=(user_id,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
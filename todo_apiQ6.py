import requests
import json

# Fetch JSON data from the API URL
url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
data = response.json()

# Encode the JSON data to a string
encoded_data = json.dumps(data, indent=2)

# Decode the JSON string back to a Python object
decoded_data = json.loads(encoded_data)

# Find the number of users
user_ids = set(todo['userId'] for todo in data)
num_users = len(user_ids)

print(f"Number of users: {num_users}")

# Find the number of tasks for each user
tasks_per_user = {}
for todo in data:
    user_id = todo['userId']
    tasks_per_user[user_id] = tasks_per_user.get(user_id, 0) + 1

print("Number of tasks for each user:")
for user_id, num_tasks in tasks_per_user.items():
    print(f"User {user_id}: {num_tasks} tasks")

# Find the number of completed and incomplete tasks for each user and rank them
completed_tasks_per_user = {}
incomplete_tasks_per_user = {}

for todo in data:
    user_id = todo['userId']
    completed = todo['completed']

    if completed:
        completed_tasks_per_user[user_id] = completed_tasks_per_user.get(user_id, 0) + 1
    else:
        incomplete_tasks_per_user[user_id] = incomplete_tasks_per_user.get(user_id, 0) + 1

# Sort users by the number of completed tasks in descending order
sorted_users = sorted(completed_tasks_per_user, key=lambda user_id: completed_tasks_per_user[user_id], reverse=True)

print("\nRanking of users by completed tasks:")
for rank, user_id in enumerate(sorted_users, start=1):
    print(f"Rank {rank}: User {user_id} - {completed_tasks_per_user[user_id]} completed tasks")

# Rank users by the number of incomplete tasks in ascending order
sorted_users = sorted(incomplete_tasks_per_user, key=lambda user_id: incomplete_tasks_per_user[user_id])

print("\nRanking of users by incomplete tasks:")
for rank, user_id in enumerate(sorted_users, start=1):
    print(f"Rank {rank}: User {user_id} - {incomplete_tasks_per_user[user_id]} incomplete tasks")

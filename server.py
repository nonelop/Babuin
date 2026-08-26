import time
from server_data.database_operations import init_database

init_database()

while True:
    print("It's works")
    time.sleep(5)
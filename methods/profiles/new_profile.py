from server_data import database_operations

def new_profile(name: str, username: str | None):
    answer = database_operations.new_profile(name, username)

    return answer
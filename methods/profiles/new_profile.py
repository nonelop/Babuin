from server_data import database_operations

def new_profile(name: str, username: str | None):
    preanswer = database_operations.new_profile(name, username)

    status, profile_id = preanswer

    return {
        "status": status,
        "data": {
            "id": profile_id
        }
    }
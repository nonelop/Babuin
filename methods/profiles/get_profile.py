from server_data import database_operations

def get_profile(target: int | str):
    answer = database_operations.get_profile(target)

    status, profile = answer

    if profile:

        return {
            "status": status,
            "data": {
                "id": profile[0],
                "name": profile[1],
                "username": profile[2],
                "reg_time": profile[3]
            }
        }

    else:

        return {
            "status": status
        }
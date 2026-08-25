from methods.chats.new_chat import new_chat
from methods.profiles.new_profile import new_profile

def router(request: dict):
    if request and request.get("action"):

        action = request.get("action")
        actions = str(action).split(".")

        operation = actions[1]

    else:
        return {
            "status": "INVALID_REQUEST",
        }

    match operation:
        case "new_profile":
            data = request.get("data", {})

            name = data.get("name")
            username = data.get("username")

            preanswer = new_profile(name, username)

            status, profile_id = preanswer

            return {
                "status": status,
                "data": {
                    "id": profile_id
                }
            }
        case _:
            return {
                "status": "NOT_FOUND",
            }
from methods.chats.new_chat import new_chat
from methods.profiles.new_profile import new_profile
from methods.profiles.get_profile import get_profile

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

            answer = new_profile(name, username)

            return answer
        
        case "get_profile":
            data = request.get("data", {})

            target = data.get("target")

            try:
                target = int(target)
                answer = get_profile(target)
            except:
                answer = get_profile(target)

            return answer

        case _:
            return {
                "status": "NOT_FOUND",
            }
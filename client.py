from router.request_router import router

while True:
    print("\n\n[1] - new_profile\n[2] - get_profile\n\n[0] - quit\n")

    operation = input("> ")

    try:
        operation = int(operation)
    except:
        print("No")

    match operation:
        case 1:
            name = input("Name: ")
            username = input("Username: ")

            request = {
                "action": "profiles.new_profile",
                "data": {
                    "name": name,
                    "username": username
                }
            }

            answer = router(request)
            print(answer)

        case 2:
            target = input("Username || id: ")

            request = {
                "action": "profiles.get_profile",
                "data": {
                    "target": target
                }
            }

            answer = router(request)
            print(answer)

        case 0:
            break

        case _:
            print("No")
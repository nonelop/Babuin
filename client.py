from router.request_router import router

while True:
    name = input("Имя: ")
    username = input("Юзернейм: ")

    request = {
        "action": "profiles.new_profile",
        "data": {
            "name": name,
            "username": username
        }
    }

    answer = router(request)

    if answer:
        print(answer)
Method - метод, по сути раздел запроса. например метод chats, profiles
Operation - операция конкретного метода. например new_chat, get_profile

Запрос отправляется в формате

request {
    action: "profiles.get_profile"
    metadata: {
        auth_token: "0x565.."
        timestamp: "19:32:08 12.08.26"
        req_id: "req_3fN89w"
    }
    data: {
        profile_id: 347
    }
}

Ответ в формате

answer {
    status: 100 # Успех
    metadata: {
        timestamp: "19:32:09 12.08.26"
        req_id: "req_3fN89w"
    }
    data: {
        profile_id: 347
        profile_name: "John"
        profile_slug: "john_doe"
    }
}

Статусы: SUCCESSFUL - Успех NOT_FOUND - не найденно INVALID_REQUEST - невалидный запрос CONFLICT - догадайтесь
infos = [
    "kim password",
    "lee abc"
]

actions = [
    "ADD 30",
    "LOGIN kim abc",
    "LOGIN lee password",
    "LOGIN kim password",
    "LOGIN kim password",
    "ADD 30",
    "ORDER",
    "ORDER",
    "ADD 40",
    "ADD 50"
]

wish_list = []
result = []

isLogin = False

for action in actions:
    action = action.split()
    command = action[0]

    if command == "LOGIN":
        if isLogin:
            result.append(False)
        else:
            user_id = action[1]
            pwd = action[2]

            for info in infos:
                info = info.split()
                if user_id == info[0] and pwd == info[1]:
                    isLogin = True
                    result.append(True)
                    break
                else:
                    isLogin = False
            if isLogin == False:
                result.append(False)

    elif command == "ADD":
        if isLogin:
            result.append(True)
            wish_list.append(action[1])
        else:
            result.append(False)
    elif command == "ORDER":
        if isLogin and len(wish_list) > 0:
            result.append(True)
            wish_list.clear()
        else:
            result.append(False)
    else:
        print("Wrong Command")
print(result)
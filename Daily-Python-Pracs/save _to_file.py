def save_username(username: str):

    with open("user.txt", "a") as file:

        file.write(username + "\n")



save_username("akhi")
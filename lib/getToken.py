def getToken():
    with open("./token", "r") as f:
        token = f.read()
        f.close()
        return token

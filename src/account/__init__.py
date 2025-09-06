


class Account:
    def __init__(self):
        pass
    def __init__(self, name: str):
        self.NAME = name
    def getname(self):
        return self.NAME

def createAccount(**kwargs):
    return Account(kwargs)

if __name__=="__main__":
    account = createAccount(name="popeye")
class CommunityDriver:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def getName(self):
        return self.__name

    def updateStatus(self, status):
        print(f"   (Driver Notification) {self.__name} acknowledges status change → {status}")

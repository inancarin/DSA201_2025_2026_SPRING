class Dog:

    friends = [] # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.closeFriends = [] # instance variable

    def addCloseFriend(self, newFriend):
        self.closeFriends.append(newFriend)
    
    def printCloseFriends(self):
        print("Close friends for", self.name,  ":", self.closeFriends)
    
    def addNormalFriend(self, newFriend):
        self.friends.append(newFriend)
    
    def printNormalFriends(self):
        print("Normal friends for", self.name,  ":", self.friends)
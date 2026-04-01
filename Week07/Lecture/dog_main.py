import dog as d

d1 = d.Dog("Rosie", 4)
d2 = d.Dog("Joe", 5)

d1.printCloseFriends()
d2.printCloseFriends()

d1.addCloseFriend("Nala")
d1.addCloseFriend("Rocky")

d1.printCloseFriends()
d2.printCloseFriends()

d1.addNormalFriend("Jack")
d1.printNormalFriends()
d2.printNormalFriends()
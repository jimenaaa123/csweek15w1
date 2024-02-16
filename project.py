
class Graph:
    def __init__(self):
        self.members = {}  #store members and relationships

    def add_member(self, name, age):
        self.name = name
        self.age = age
        self.friends = [] #empty list of friends

    def add_relationship(self, member1, member2):
            member1.friends.append[member2] #add member 2 to the friend list of member1





network = Graph()


# Add some members to the network
network.add_member("Alice", age=25)
network.add_member("Bob", age=30)


# Add some relationships between members
network.add_relationship('Alice', 'Bob')
network.add_relationship('Bob', 'Alice')


# Find all the friends of Alice
#alice_friends = network.find_friends("Alice")
#print(alice_friends) # Output: ["Bob"]

# Find the shortest path between Alice and David
#shortest_path = network.shortest_path("Alice", "David")
#print(shortest_path) # Output: 3


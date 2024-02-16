
class Graph:
    self.Graph
    def __init__(self):
        self.members = {}  #store members and relationships

    def add_mem(self, name, age)
        self.name = name
        self.age = age

    def find_friends(self, member1):
        if member1 in self.friends:
            return list(self.friends[member1]['friends'])
        else:
            print("Member not found in the network.")
        return []

    def add_rel(self, member1, member2):


network = Graph()

# Add some members to the network
network.add_member("Alice", age = 25)
network.add_member("Bob", age = 30)


# Add some relationships between members
network.add_relationship("Alice", "Bob")
network.add_relationship("Bob", "Alice")




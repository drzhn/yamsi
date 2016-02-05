from py2neo import Graph


class last2neo:
    def __init__(self):
        self.graph = Graph()
        self.graph.cypher.execute("MATCH (n) DETACH DELETE n")

    def create_artist(self, name):
        self.graph.cypher.execute("CREATE (n:Artist { name : \"" + name + "\"})")

    def create_rel(self, name1, name2, ratio):
        self.graph.cypher.execute(
                "MATCH (a:Artist),(b:Artist) WHERE a.name = \"" + name1 + "\" AND b.name = \"" + name2 +
                "\" CREATE (a)-[r:similar { ratio : " + str(ratio) + " }]->(b)")

    def check_if_exists(self, name):
        ret = len(self.graph.cypher.execute("match (n:Artist) where n.name=\""+name+"\" return n"))

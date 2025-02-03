from rdflib import Graph, Namespace

D = Namespace("https://expertise.matdata.eu/#/page/")
# Create a new Graph
g = Graph()

# Parse the input TTL file
g.parse("skos.ttl", format="turtle")
        
for s, p, o in g.triples((None, None, D.Categories)):
    g.remove((s, p, o))

# Serialize and write to the output file
g.serialize(destination="skos2.ttl", format="turtle")
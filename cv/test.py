from rdflib import Graph
from ruamel.yaml import YAML

yaml = YAML()

# Create a Graph
g = Graph()

# Parse the TTL file
g.parse("../test.ttl", format="turtle")

# Print the number of triples in the graph
print(f"Number of triples in the graph: {len(g)}")

# Get projects SPARQL query
query_projects = """

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
prefix qudt: <http://qudt.org/2.1/schema/qudt/> 

delete {?s ?p ?o} 
WHERE {
  ?s a qudt:Quantity .
  ?s ?p ?o.
  FILTER NOT EXISTS {?s qudt:value ?value}
} 


"""

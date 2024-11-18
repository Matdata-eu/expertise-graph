from rdflib import Graph

# Create a Graph
g = Graph()

# Parse the TTL file
g.parse("matdata-expertise.ttl", format="turtle")

# Print the number of triples in the graph
print(f"Number of triples in the graph: {len(g)}")

# Example SPARQL query
query = """
    SELECT ?s ?p ?o
    WHERE {
        ?s ?p ?o
    }
    LIMIT 10
"""

# Execute the query
for row in g.query(query):
    print(row)
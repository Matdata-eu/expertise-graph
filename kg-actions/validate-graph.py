
from pyshacl import validate
import rdflib
# Load the data graph
data_graph = rdflib.Graph()
data_graph.parse("matdata-expertise.ttl", format="turtle")
print(f"Number of triples in data graph: {len(data_graph)}")

# Load the SHACL shapes graph
shacl_graph = rdflib.Graph()
shacl_graph.parse("kg-actions/matdata-expertise-shacl.ttl", format="turtle")
print(f"Number of triples in shacl graph: {len(shacl_graph)}")



# Validate the data graph against the SHACL shapes graph
conforms, results_graph, results_text = validate(
    data_graph,
    shacl_graph=shacl_graph,
    inference='none',
    abort_on_first=False,
    meta_shacl=False,
    advanced=True,
    debug=False
)

# Print the validation results
print(results_text)

# Save the validation report as TTL
results_graph.serialize(destination="validation-report.ttl", format="turtle")
print("\nValidation report saved to validation-report.ttl")

if not conforms:
    exit(1)
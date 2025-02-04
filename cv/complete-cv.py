from rdflib import Graph
from ruamel.yaml import YAML

yaml = YAML()

# Create a Graph
g = Graph()

# Parse the TTL file
g.parse("../matdata-expertise.ttl", format="turtle")

# Print the number of triples in the graph
print(f"Number of triples in the graph: {len(g)}")

# Get projects SPARQL query
query_projects = """

PREFIX s: <https://schema.org/>
PREFIX d: <https://expertise.matdata.eu/#/page/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?uri ?category ?name ?description
       (GROUP_CONCAT(distinct ?role_name; separator=", ") AS ?roles) 
       (GROUP_CONCAT(distinct ?technique_name; separator=", ") AS ?techniques) 
WHERE {
    {
        SELECT (REPLACE(str(?s),"([#%()])", "\\\\$$1") as ?uri) ?category ?name ?description ?role_name ?technique_name
        WHERE {
            ?s  a d:Project ;
                rdfs:label ?name ;
                rdfs:comment ?description ;
                d:is-featured ?project_featured ;
                d:has-category ?categoryUri ;
                d:has-tagged-techniques ?technique ;
                d:has-tagged-roles ?role .
            
            ?categoryUri skos:prefLabel ?category .

            ?technique a d:Technique ;
                d:is-featured ?technique_featured ;
                rdfs:label ?technique_name .

            ?role a d:Role ;
                d:is-featured ?role_featured ;
                rdfs:label ?role_name .

            FILTER(?project_featured)
        }
        ORDER BY ?role_name ?technique_name
    }
}
GROUP BY ?uri ?category ?name ?description
ORDER BY ?uri ?category ?name

"""

# Get techniques SPARQL query
query_technologies = """


PREFIX s: <https://schema.org/>
PREFIX d: <https://expertise.matdata.eu/#/page/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?category 
       (GROUP_CONCAT(
        CONCAT("[", str(?name), "]("
        , REPLACE(
            str(?s),
            "([#%()])", "\\\\$$1"
        )       
        , ")"
       ); separator=", ") AS ?technologies)
WHERE {
    SELECT ?s ?category ?name
    WHERE {
        ?s  a d:Technique;
            d:is-featured ?featured;
            d:has-category ?categoryUri;
            rdfs:label ?name.      
            
        ?categoryUri skos:prefLabel ?category .

        FILTER(?featured)
    }
    ORDER BY ?category ?name
}
GROUP BY ?category
ORDER BY ?category

"""

# Execute the query and collect results
project_results = []
for row in g.query(query_projects):
    project_results.append({
        "date": str(row.category),
        "name": '[' + str(row.name) +'](' +str(row.uri) + ')',
        "highlights": [str(row.description), '**Roles**: ' + str(row.roles), '**Technologies**: ' + str(row.techniques)]
    }) 

# Execute the query and collect results
technology_results = []
for row in g.query(query_technologies):
    technology_results.append({
        "label": str(row.category),
        "details": str(row.technologies)
    }) 

# Load existing YAML file
with open("Mathias_Vanden_Auweele_CV.yaml", "r") as file:
    cv_data = yaml.load(file)

# Append results to 'projects' section
cv_data['cv']['sections']['projects'] = project_results
cv_data['cv']['sections']['technologies'] = technology_results

# Save updated YAML file
with open("Mathias_Vanden_Auweele_CV.yaml", "w") as file:
    yaml.dump(cv_data, file)
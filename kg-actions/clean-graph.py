from rdflib import Graph, Namespace, RDF, OWL, RDFS, SKOS, URIRef, Literal, XSD

# Create namespaces
D = Namespace("https://expertise.matdata.eu/#/page/")
S = Namespace("https://schema.org/")

def map_types():
    # Load the input graphs
    g = Graph()
    g.parse("./matdata-expertise-raw.ttl", format="turtle")
    skos_g = Graph()
    skos_g.parse("./skos.ttl", format="turtle")
    
    # Merge graphs
    g += skos_g
    
    # Map d:type to rdf:type and d:Class to owl:Class
    for s, p, o in g.triples((None, D.type, None)):
        g.add((s, RDF.type, o))
        g.remove((s, p, o))

    for s, p, o in g.triples((None, None, D.Class)):
        g.add((s, p, OWL.Class))
        g.remove((s, p, o))

    # Map schema:name to rdfs:label
    for s, p, o in g.triples((None, S.name, None)):
        g.add((s, RDFS.label, o))
        g.remove((s, p, o))
    
    # Map d:description to rdfs:comment
    for s, p, o in g.triples((None, D.description, None)):
        g.add((s, RDFS.comment, o))
        g.remove((s, p, o))
        
    for s, p, o in g.triples((None, D.public, None)):
        g.remove((s, p, o))
        
    # Remove exclude-from-graph properties
    for s, p, o in g.triples((None, D['exclude-from-graph-view'], None)):
        g.remove((s, p, o))

    # Map Yes/No to boolean
    for s, p, o in g.triples((None, None, Literal("Yes"))):
        g.add((s, p, Literal(True)))
        g.remove((s, p, o))

    # Convert date strings to datetime literals
    for s, p, o in g.triples((None, D['ended-on'], None)):
        if isinstance(o, Literal) and o.datatype is None:
            date_str = str(o) + "-01T00:00:00"  # Add day and time components
            g.add((s, p, Literal(date_str, datatype=XSD.dateTime)))
            g.remove((s, p, o))

    for s, p, o in g.triples((None, D['started-on'], None)):
        if isinstance(o, Literal) and o.datatype is None:
            date_str = str(o) + "-01T00:00:00"  # Add day and time components
            g.add((s, p, Literal(date_str, datatype=XSD.dateTime)))
            g.remove((s, p, o))

    for s, p, o in g.triples((None, None, Literal("No"))):
        g.add((s, p, Literal(False)))
        g.remove((s, p, o))

    # Map categories to SKOS concepts
    for s, p, o in g.triples((None, D['has-category'], None)):
        category_uri = D[f"category-{o.lower().replace('/', '-').replace(' ', '-').replace('&', 'and').replace('#','sharp')}"]
        if (category_uri, RDF.type, SKOS.Concept) in g:
            g.add((s, D['has-category'], category_uri))
            g.remove((s, p, o))

    # Map proficiency levels to SKOS concepts
    for s, p, o in g.triples((None, D['self-estimated-proficiency'], None)):
        proficiency_uri = D[f"proficiency-{o.lower().replace(' ', '-')}"]
        if (proficiency_uri, RDF.type, SKOS.Concept) in g:
            g.add((s, D['self-estimated-proficiency'], proficiency_uri))
            g.remove((s, p, o))

    # Save the result
    g.serialize("./matdata-expertise.ttl", format="turtle")

if __name__ == "__main__":
    map_types()

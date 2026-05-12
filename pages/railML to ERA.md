public:: true
type:: [[Project]]
description:: Built a reusable pipeline to convert railML 3.2 infrastructure data into ERA ontology (RINF-compatible RDF), including enrichment and SHACL validation.
has-category:: Data processing
has-tagged-techniques:: #[[RailML]], #[[ERA ontology]], #[[RINF]], #RDF, #SPARQL, #SHACL, #Python, #[[Apache Jena Fuseki]], #Docker, #[[SPARQL Anything]], #GIS, #rdflib 
has-tagged-roles:: #[[Independent expert]], #Developer, #[[Data architect]]
has-linked-projects:: #[[Workshop RINF data provisioning]]
is-featured:: Yes
during-job:: #[[Job: ERA independent expert Safety & Telematics]]
external-link:: https://github.com/Matdata-eu/raillML-to-ERA

- Created a workshop-oriented conversion pipeline:
	- `01-prep`: railML XML to RDF (SPARQL Anything)
	- `02-construct`: SPARQL CONSTRUCT to ERA ontology graph
	- `03-post-process`: geometry enrichment and data fixes
	- `04-validate`: SHACL validation report generation
	- `05-validate`: SHACL-SHACL to validate ERA shapes
	- `06-create-topology`: a demo on how to create micro topology from GIS linestrings
- Added supporting steps for shape validation and topology generation.
- Prepared practical assets for the ERA RINF workshop while keeping scripts reusable for similar inputs.
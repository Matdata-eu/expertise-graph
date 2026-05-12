public:: true
type:: [[Project]]
description:: Lightweight linked-data dereferencer that turns resource URIs into interactive HTML views backed by SPARQL DESCRIBE queries, while also supporting content negotiation for RDF serializations.
has-category:: Semantic
has-tagged-techniques:: #RDF, #SPARQL, #Nginx, #Docker, #Javascript, #Leaflet, #GitHub
has-tagged-roles:: #Developer
has-linked-projects:: #[[Yasgui Graph Plugin]], #[[This expertise graph & website]]
is-featured:: No
during-job:: #[[Job: Independent railway data freelancer]]
external-link:: https://github.com/Matdata-eu/uri-dereferencer

- Designed for linked-data publication patterns where a URI should resolve both in the browser and as RDF.
- Renders property tables, related resources, and WKT geometries on a map without relying on third-party CDNs.
- Packaged as a Docker container for easy deployment in front of an existing SPARQL endpoint.
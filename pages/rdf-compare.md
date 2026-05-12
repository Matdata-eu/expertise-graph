public:: true
type:: [[Project]]
description:: Open source CLI and browser viewer to compute semantic diffs between RDF files, preserving named graphs, supporting blank-node-aware comparison, and producing machine-readable RDF diff output.
has-category:: Semantic
has-tagged-techniques:: #RDF, #[[Rust]], #Docker, #Leaflet, #GitHub, #[[Github actions]]
has-tagged-roles:: #Developer
has-linked-projects:: #[[This expertise graph & website]]
is-featured:: No
during-job:: #[[Job: Independent railway data freelancer]]
external-link:: https://github.com/Matdata-eu/rdf-compare

- Supports Turtle, N-Triples, RDF/XML, TriG, N-Quads, and gzipped inputs.
- Includes a local web viewer to inspect diffs interactively, including map visualisation for GeoSPARQL literals.
- Useful in CI pipelines because it can fail builds when RDF snapshots diverge.
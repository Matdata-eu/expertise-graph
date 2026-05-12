public:: true
type:: [[Project]]
description:: Small Docker-ready proxy to work around CORS restrictions when consuming APIs and SPARQL endpoints from browser-based tools, with built-in preflight handling and optional token-based protection.
has-category:: DevOps
has-tagged-techniques:: #Javascript, #Docker, #[[Forward proxy]], #GitHub
has-tagged-roles:: #Developer
has-linked-projects:: #[[Yasgui - SPARQL GUI]]
is-featured:: No
during-job:: #[[Job: Independent railway data freelancer]]
external-link:: https://github.com/Matdata-eu/simple-cors-proxy

- Supports routing through a request header or directly encoded destination URLs.
- Added specifically to solve practical browser integration issues, including problematic OPTIONS handling on some RDF backends.
- Distributed as a container for quick deployment in front of constrained APIs.
exclude-from-graph-view:: true
type:: [[Property]]
description:: describes which techniques and tools were used in the project

- To document:
	- #ESP32, #NodeMCU, #PLC, #Telnet, #[[PL/pgSQL]], #[[IBM MQ]]
	-
- {{query (page-property :type [[Technique]])}}
  query-sort-by:: has-category
  query-sort-desc:: true
  query-properties:: [:page :self-estimated-proficiency :is-featured :has-category]
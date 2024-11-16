exclude-from-graph-view:: true
type:: [[Property]]
description:: describes which techniques and tools were used by me in the project. It could be that more techniques are employed but if the use of the technique in the project doesn't in some way prove my proficiency, it is not linked by this property.

- To document:
	- #ESP32, #NodeMCU, #PLC, #Telnet, #[[PL/pgSQL]], #[[IBM MQ]], #[[MS Graph]], #ADFS, #Jira, #ClickOnce, #[[Project management]], #PMO, #[[JSON API]], #S3, #WMS, #Scichart, #SQL, #Binary, #[[RCM-DX format]], #LRS, #[[Data governance]]
	-
- {{query (page-property :type [[Technique]])}}
  query-sort-by:: has-category
  query-sort-desc:: true
  query-properties:: [:page :self-estimated-proficiency :is-featured :has-category]
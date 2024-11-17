exclude-from-graph-view:: true
type:: [[Property]]
description:: a list of roles I had during any phase of the project

- {{query (page-property :type [[Role]])}}
  query-sort-by:: has-category
  query-sort-desc:: false
  query-properties:: [:page :self-estimated-proficiency :has-category]
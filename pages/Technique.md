exclude-from-graph-view:: true
type:: [[Class]]
description:: a representative skill or tool required to execute a project

- {{query (page-property :type "Technique")}}
  query-properties:: [:page :is-featured :has-category]
  query-sort-by:: page
  query-sort-desc:: false
-
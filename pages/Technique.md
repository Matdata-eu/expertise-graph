exclude-from-graph-view:: true
type:: [[Class]]
description:: a representative skill or tool required to execute a project

- {{query (page-property :type "Technique")}}
  query-properties:: [:page :is-featured :has-category :self-estimated-proficiency]
  query-sort-by:: self-estimated-proficiency
  query-sort-desc:: false
-
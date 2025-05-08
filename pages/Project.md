exclude-from-graph-view:: true
type:: [[Class]]
description:: a thing you do when you have a goal in mind

- {{query (page-property :type [[Project]])}}
  query-sort-by:: page
  query-sort-desc:: false
- query-properties:: [:page :has-category]
  query-sort-by:: has-category
  query-sort-desc:: false
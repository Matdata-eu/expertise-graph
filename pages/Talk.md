exclude-from-graph-view:: true

- {{query (and (page-property :type [[Talk]]) )}}
  query-properties:: [:page :format :audience-size :is-featured :external-link :year]
  query-sort-by:: year
  query-sort-desc:: true
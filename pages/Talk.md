exclude-from-graph-view:: true
type:: [[Class]]
description:: presentation, workshop or course where I am the speaker in front of an audience

- {{query (and (page-property :type [[Talk]]) )}}
  query-properties:: [:page :format :audience-size :is-featured :external-link :year]
  query-sort-by:: year
  query-sort-desc:: true
- {{query (and (page-property :type [[Project]]) (page-property :is-featured "Yes"))}}
  query-properties:: [:page :has-category :description :has-tagged-techniques]
  query-sort-by:: has-category
  query-sort-desc:: false
-
-
-
- {{query (and (property :type [[Project]]) (property :is-featured "Yes"))}}
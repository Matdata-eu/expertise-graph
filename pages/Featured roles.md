- {{query (and (page-property :type "Role") (not (page-property :is-featured "No")))}}
  query-properties:: [:page :self-estimated-proficiency :category]
  query-sort-by:: created-at
  query-sort-desc:: false
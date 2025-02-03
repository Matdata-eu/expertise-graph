- {{query (and (page-property :type "Role") (not (page-property :is-featured "No")))}}
  query-properties:: [:page :self-estimated-proficiency :has-category]
  query-sort-by:: page
  query-sort-desc:: false
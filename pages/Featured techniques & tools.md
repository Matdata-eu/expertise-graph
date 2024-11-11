- {{query (and (page-property :type "Technique") (not (page-property :is-featured "No")))}}
  query-properties:: [:has-category :page :self-estimated-proficiency]
  query-sort-by:: has-category
  query-sort-desc:: false
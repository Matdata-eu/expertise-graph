- {{query (and (page-property :type "Technique") (not))}}
- {{query (and (property type "Technique") (not (property :is-featured "No")))}}
  query-table:: true
  query-sort-by:: has-category
  query-sort-desc:: false
  query-properties:: [:has-category :type :self-estimated-proficiency :is-featured]
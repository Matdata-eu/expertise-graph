- {{query (and (property type "Technique")) (order-by (property has-category) (property self-estimated-proficiency))}}
  query-table:: true
  query-properties:: [:page :self-estimated-proficiency :is-featured :has-category]
  query-sort-by:: has-category
  query-sort-desc:: false
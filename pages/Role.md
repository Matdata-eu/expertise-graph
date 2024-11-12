exclude-from-graph-view:: false
type:: [[Class]]
has-description:: the responsibilities taken in the project or job

- {{query (page-property :type [[Role]])}}
  query-properties:: [:page :self-estimated-proficiency :has-category :is-featured]
  query-sort-by:: page
  query-sort-desc:: false
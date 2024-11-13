- {{query (and (page-property :type "Role") (not (page-property :is-featured "No")))}}
  query-properties:: [:page :self-estimated-proficiency :category]
  query-sort-by:: page
  query-sort-desc:: false
- title: get all pages with property type:: Role
  - pages
     - *
  - pageproperties
     - type, "[[Role]]"
	- #+BEGIN_QUERY
	  {
	  :title [:b "get all pages with property type"]
	  :query [:find (pull ?block [*])
	  :where
	  [?block :block/name ?pagename]
	  (page-property ?block :type "Role")
	  ]
	  }
	  #+END_QUERY
-
-
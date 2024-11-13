- {{query (and (page-property :type "Role") (not (page-property :is-featured "No")))}}
  query-properties:: [:page :self-estimated-proficiency :category]
  query-sort-by:: page
  query-sort-desc:: false
-
	- #+BEGIN_QUERY
	  ;; WARNING: Must have 'pages' command or 'blocks' Command
	  ;;          otherwise the query cannot get any information
	  ;;          Inserting a blocks command for you
	  
	  {
	  :where
	  ]
	  }
	  #+END_QUERY
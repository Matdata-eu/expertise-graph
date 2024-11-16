exclude-from-graph-view:: true
type:: [[Property]]
description:: describes which techniques and tools were used in the project

- #+BEGIN_QUERY
  {
  :title[:h2 "Techniques not documented"]
  :query 
    [
      :find ?technique
      :where 
      (
       [?p :block/properties ?properties]
       [(get ?properties :type) ?type]
       [(= ?type "Project")]     
       [(get ?properties :has-tagged-techniques) ?techniques]
      )
    ]
  }
  #+END_QUERY
	- query-table:: false
	  #+BEGIN_QUERY
	  {
	    :title "List of all properties"
	    :query [
	      :find  ?property 
	      :where
	      [_ ?property _]
	    ]
	    :result-transform (fn [result] (sort-by (fn [r] (get-in r [:sort])) result))
	    :view (fn [result] (for [r result] [:pre (pr-str r)]))
	  }
	  #+END_QUERY
- query-sort-by:: started-on
- query-sort-desc:: true
- {{query (page-property :type [[Technique]])}}
  query-sort-by:: page
  query-sort-desc:: false
  query-properties:: [:page :self-estimated-proficiency :is-featured :has-category]
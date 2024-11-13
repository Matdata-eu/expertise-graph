exclude-from-graph-view:: true
type:: [[Property]]
description:: used to put things in buckets

- #+BEGIN_QUERY
  {
    :title "Distinct values of has-category"
    :query [
      :find (distinct ?value)
      :where
      [?page :block/properties ?props]
      [ page-property ?page :type "Project" ]
      [(get ?props :has-category) ?value]
    ]
    :result-transform (fn [result] (sort result))
    :view (fn [result] 
            [:ul (for [val result]
                   [:li val])])
  }
  #+END_QUERY
- #+BEGIN_QUERY
  {
  :query [
      :find ?prop
      :where
        [?b :block/properties ?prop]
  ]
  :view(fn [rows] (for
      [prop (sort (distinct (flatten (map keys rows))))]
      [:div (clojure.string/replace-first (str prop) ":" "") ]))
  }
  #+END_QUERY
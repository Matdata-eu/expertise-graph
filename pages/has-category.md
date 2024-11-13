exclude-from-graph-view:: true
type:: [[Property]]
description:: used to put things in buckets

- #+BEGIN_QUERY
  {
    :title "Distinct values of has-category for project pages"
  :query [
      :find ?value
      :where
      [?page :block/properties ?props]
      [ page-property ?page :type "Project" ]
      [(get ?props :has-category) ?value]
      [(not= ?value "")]
  ]
    :result-transform (fn [result] (sort result))
  :view(fn [rows] (for
      [prop (sort (distinct (flatten (map keys rows))))]
      [:div (clojure.string/replace-first (str value) ":" "") ]))
  }
  #+END_QUERY
- #+BEGIN_QUERY
  {
    :title "Distinct values of has-tagged-technique for project pages"
  :query [
      :find ?value
      :where
      [?page :block/properties ?props]
      [ page-property ?page :type "Project" ]
      [(get ?props :has-category) ?value]
      [(not= ?value "")]
  ]
    :result-transform (fn [result] (sort result))
  :view(fn [rows] (for
      [prop (sort (distinct (flatten (map keys rows))))]
      [:div (clojure.string/replace-first (str value) ":" "") ]))
  }
  #+END_QUERY
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
      [(get ?props :has-category) ?value]
    ]
    :result-transform (fn [result] (map first result))
    :view (fn [result]
            [:ul (for [value result]
                   [:li value])])
  }
  #+END_QUERY
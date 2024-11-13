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
    :result-transform (fn [result] (result))
    :view (fn [result]
            [:ul (for [val result]
                   [:li val])])
  }
  #+END_QUERY
-
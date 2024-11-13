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
  }
  #+END_QUERY
-
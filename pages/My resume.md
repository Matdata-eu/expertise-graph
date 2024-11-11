query-table:: true
query-properties:: [:page :start :end :duration :started-on :ended-on :at-company]
query-sort-by:: started-on
query-sort-desc:: true
#+BEGIN_QUERY
{:title [:h2 "Job titles"]
 :query [:find (pull ?p [*])
         :where
         (page-property ?p :type "Job")]}
#+END_QUERY

-
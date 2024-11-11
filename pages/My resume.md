query-table:: true
query-properties:: [:page :start :end :duration :at-company]
query-sort-by:: start
query-sort-desc:: true
#+BEGIN_QUERY
{:title [:h2 "Job titles"]
 :query [:find (pull ?p [*])
         :where
         (page-property ?p :type "Job title")]}
#+END_QUERY

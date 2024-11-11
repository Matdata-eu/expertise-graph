query-properties:: [:page :started-on :ended-on :at-company]
query-sort-by:: started-on
query-sort-desc:: true
#+BEGIN_QUERY
{:title [:h2 "Jobs"]
 :query [:find (pull ?p [*])
         :where
         (page-property ?p :type "Job")]}
#+END_QUERY

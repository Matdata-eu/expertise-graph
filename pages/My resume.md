- #+BEGIN_QUERY
  {:title [:h2 "Job titles"]
   :query [:find (pull ?p [*])
           :where
           (page-property ?p :type "Job")]}
  #+END_QUERY
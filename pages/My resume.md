- Below you find a classic resume
	- #[[Independent data freelancer]]
	- #[[Teamlead data centricity]]
	- #[[Project lead digitalisation linear assets]]
	- #[[Project lead SMILE 2.0]]
	- #[[Infrastructure engineer: overhead contact lines]]
	- #[[Ambassador]]
	- #[[Coordinator operational safety]]
	- #[[Fencing instructor]]
	- #[[Chairman committee 9]]
	- #[[EIM speaker for energy subsystem]]
	- #[[Entrepreneur, head of my own company]]
	- #[[Internship statistical analysis of voltage dips]]
- query-table:: true
  query-properties:: [:page :start :end :duration :at-company]
  query-sort-by:: start
  query-sort-desc:: true
  #+BEGIN_QUERY
  {:title [:h2 "Job Titles"]
   :query [:find (pull ?p [*])
           :where
           (property ?p :type "Job title")]}
  #+END_QUERY
- query-table:: false
  #+BEGIN_QUERY
  {:title [:h2 "Job Titles"]
   :query [:find (pull ?p [*])
           :where
           (property ?p :type "Job title")]
   :result-transform (fn [result]
                       (map (fn [page]
                              {:page-title (:name page)
                               :start (:start page)
                               :end (:end page)
                               :duration (:duration page)
                               :at-company (:at-company page)})
                            result))}
  #+END_QUERY
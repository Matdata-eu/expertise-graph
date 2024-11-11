public:: false
exclude-from-graph-view:: true

- Project
	- template:: Project
	  template-including-parent:: false
		- public:: true
		  type:: #[[Project]]
		  tagged-techniques::
		  tagged-roles::
		  linked-projects::
		  is-featured::
- Role
	- template:: Role
	  template-including-parent:: false
		- public:: true
		  type:: #[[Role]]
		  self-estimated-proficiency::
		  is-featured::
- Techniques
	- template:: Technique
	  template-including-parent:: false
		- public:: true
		  type:: #[[Technique]]
		  self-estimated-proficiency::
		  is-featured::
		  has-category::
- Talks
	- template:: Talk
	  template-including-parent:: false
		- public:: true
		  type:: #[[Talk]]
		  subject::
		  audience-size::
		  audience-type::
		  is-featured::
- Job
	- template:: Job
	  template-including-parent:: false
		- type:: #[[Job]]
		  start::
		  end::
		  duration:: ~ years
		  at-company::
		  description::
		  linked-roles::
- Company
	- template:: Company
	  template-including-parent:: false
		- type:: #[[Company]]
		  link::
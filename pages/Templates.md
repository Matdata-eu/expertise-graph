public:: false
exclude-from-graph-view:: true

- Project
	- template:: Project
	  template-including-parent:: false
		- public:: true
		  is-of-type:: #[[Project]]
		  has-tagged-techniques::
		  has-tagged-roles::
		  has-linked-projects::
		  is-featured::
- Role
	- template:: Role
	  template-including-parent:: false
		- public:: true
		  is-of-type:: #[[Role]]
		  self-estimated-proficiency::
		  is-featured::
- Techniques
	- template:: Technique
	  template-including-parent:: false
		- public:: true
		  is-of-type:: #[[Technique]]
		  self-estimated-proficiency::
		  is-featured::
		  has-category::
- Talks
	- template:: Talk
	  template-including-parent:: false
		- public:: true
		  is-of-type:: #[[Talk]]
		  has-subject::
		  audience-size::
		  has-audience-is-of-type::
		  is-featured::
- Job
	- template:: Job
	  template-including-parent:: false
		- is-of-type:: #[[Job]]
		  started-on::
		  ended-on::
		  has-duration:: ~ years
		  at-company::
		  has-description::
		  has-linked-roles::
- Company
	- template:: Company
	  template-including-parent:: false
		- is-of-type:: #[[Company]]
		  has-link::
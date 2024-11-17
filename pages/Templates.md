public:: false
exclude-from-graph-view:: true

- Project
	- template:: Project
	  template-including-parent:: false - public:: true
	  type:: [[Project]]
	  description::
	  has-category::
	  has-tagged-techniques::
	  has-tagged-roles::
	  has-linked-projects::
	  is-featured::
	  during-job::
- Role
	- template:: Role
	  template-including-parent:: false
		- public:: true
		  type:: [[Role]]
		  self-estimated-proficiency:: 
		  is-featured:: 
		  has-category::
- Techniques
	- template:: Technique
	  template-including-parent:: false
		- public:: true
		  type:: [[Technique]]
		  self-estimated-proficiency::
		  is-featured::
		  has-category::
- Talks
	- template:: Talk
	  template-including-parent:: false
		- public:: true
		  type:: [[Talk]]
		  format::
		  audience-size::
		  is-featured::
		  external-link::
		  year::
		  during-job::
- Job
	- template:: Job
	  template-including-parent:: false
		- type:: [[Job]]
		  started-on::
		  ended-on::
		  has-duration:: ~ years
		  at-company::
		  description::
		  has-linked-roles::
- Company
	- template:: Company
	  template-including-parent:: false
		- type:: [[Company]]
		  external-link::
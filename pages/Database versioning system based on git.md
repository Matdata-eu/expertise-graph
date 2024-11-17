public:: true
type:: [[Project]]
description:: A database is mostly managed in several environments and changes are pushed to production after a lengthy review process. For some database applications, this is a costly overhead that is preferably avoided. Development happens directly on the production system (no worries, this has been going well for over 10 years now). And one of the reasons this goes well is because we have a system that daily captures the DDL changes of the database and stores them in a git repository. Reverting to a previous state become a matter of using git.
has-category:: Data processing
has-tagged-techniques:: [[C# .NET]], #Git, #Postgresql, #Dbeaver, #Quartz.NET, #Serilog
has-tagged-roles:: #[[Project lead]], #[[Data architect]]
has-linked-projects::
is-featured:: No
during-job:: #[[Job: engineer overhead contact lines]]

-

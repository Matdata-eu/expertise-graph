public:: true
type:: [[Project]]
description:: A backend system to automate data transfers from several databases. Using several techniques such as delta transfer or ID based copying.
has-category:: Data processing
has-tagged-techniques:: [[C#]], #Postgresql, #Dbeaver, #SAS, #MSSQL, #Oracle, #Kerberos, #[[SAP HANA BIQ]], #Quartz, #Serilog, #Loki, #Git, #[[Gitlab CI CD]], #Openshift, #[[Apache nifi]] 
has-tagged-roles:: #Developer, #[[Data analyst]], #[[Data architect]], #[[DevOps engineer]]
has-linked-projects::
is-featured:: Yes
during-job:: #[[Job: engineer overhead contact lines]], #[[Job: Project lead digitalisation linear assets]], #[[Job: Teamlead data centricity]]

- The system needed to sync data around the enterprise into a #Postgresql based data platform. It's written in #[[C#]] and uses #Quartz for scheduling. It's a very flexible setup where source data is listed in the Postgres database. Adding additional source data is as simple as adding an additional record to the table.
- Logging is performed using #Serilog with sinks to email, #Loki and several other targets.
- I would prefer not to have to work with a #SAS "database" again. :)
-
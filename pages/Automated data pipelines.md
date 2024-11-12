public:: true
type:: [[Project]]
description:: A backend system to automate data transfers from several databases. Using several techniques such as delta transfer or ID based copying.
has-category:: Data processing
has-tagged-techniques:: [[C# .NET]], #Postgresql, #SAS, #MSSQL, #Oracle, #Kerberos, #[[SAP HANA BIQ]], #Quartz.NET 
has-tagged-roles:: #Developper, #[[Data analyst]], #[[Data architect]] 
has-linked-projects::
is-featured:: Yes
during-job:: #[[Job: engineer overhead contact lines]], #[[Job: Project lead digitalisation linear assets]], #[[Job: Teamlead data centricity]]

- The system needed to sync data around the enterprise into a #Postgresql based data platform. It's written in #[[C# .NET]] and uses #Quartz.NET for scheduling. It's a very flexible setup where source data is listed in the Postgres database.
- I would prefer not to have to work with a #SAS "database" again.
-
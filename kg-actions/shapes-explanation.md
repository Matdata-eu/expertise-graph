# SHACL Validation Rules

This SHACL shapes file defines validation rules for different entity types in the expertise knowledge graph.

## Projects

- Must have exactly one label (string)
- Must have exactly one category that is a SKOS concept from ProjectCategories scheme
- Must have exactly one is-featured boolean flag
- Can link to Job instances via during-job
- Can have multiple techniques and roles via has-tagged-techniques/roles
- Can have one description (comment)

## Techniques

- Must have exactly one label (string)
- Must have exactly one category that is a SKOS concept from TechniqueCategories scheme
- Must have exactly one is-featured flag
- Must have exactly one proficiency level from ProficiencyLevels scheme

## Roles

- Must have exactly one label (string)
- Must have exactly one category that is a SKOS concept from RoleCategories scheme  
- Must have exactly one is-featured flag
- Must have exactly one proficiency level

## Companies

- Must have exactly one label (string)
- Can have one external link (must be IRI)

## Jobs

- Must have exactly one label (string)
- Must have exactly one company reference
- Must have exactly one start date (dateTime)
- Can have one end date (dateTime)
- Must have exactly one duration string
- Can have multiple linked roles

## SKOS Categories

- Must have exactly one preferred label (string)
- Must belong to at least one concept scheme
- Can have one definition (string)

## SKOS Concept Schemes

- Must have exactly one label (string)

The shapes enforce data quality by:
- Validating cardinality constraints (minCount/maxCount)
- Checking data types (string, boolean, dateTime, IRI)
- Ensuring category membership in correct concept schemes
- Validating class relationships between entities
- Enforcing consistent proficiency level usage
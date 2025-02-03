# SHACL Validation Rules

This SHACL shapes file defines validation rules for different entity types in the expertise knowledge graph.

## Projects

- Must have a label
- Must have exactly one category (SKOS concept)
- Must have is-featured boolean flag
- Can have multiple techniques and roles
- Optional description

## Techniques

- Must have a label 
- Must have exactly one category
- Must have is-featured flag
- Must have exactly one proficiency level

## Roles

- Must have a label
- Must have exactly one category 
- Must have is-featured flag
- Must have exactly one proficiency level

## Companies

- Must have a label
- Can have one external link

## Jobs

- Must have a label
- Must have exactly one company
- Must have start date (xsd:dateTime format)
- Can have end date (xsd:dateTime format)
- Must have duration
- Can have multiple linked roles

## SKOS Categories

- Must have exactly one preferred label
- Must belong to at least one concept scheme
- Can have one definition

## SKOS Concept Schemes

- Must have exactly one label
# Expertise Knowledge Graph

These are my notes that together form a semantic knowledge graph built with [Logseq](https://logseq.com/). They document my professional expertise, projects, skills, and career history. The knowledge graph is automatically exported to RDF, validated using SHACL shapes, and published as a static website, PDF CV and RDF data. The RDF data is available both as ttl serialization and through SPARQL endpoint.

## 🌐 Live Deployments

- **Website**: [expertise.matdata.eu](https://expertise.matdata.eu)
- **SPARQL Endpoint**: [jena.mkwadraat.be/expertise](https://jena.mkwadraat.be/expertise)
- **CV (PDF)**: [expertise.matdata.eu/static/Mathias_Vanden_Auweele_CV.pdf](https://expertise.matdata.eu/static/Mathias_Vanden_Auweele_CV.pdf)
- **RDF Data**: 
  - [matdata-expertise.ttl](https://expertise.matdata.eu/static/matdata-expertise.ttl) (cleaned & validated)
  - [matdata-expertise-raw.ttl](https://expertise.matdata.eu/static/matdata-expertise-raw.ttl) (raw export)
  - [matdata-expertise-shacl.ttl](https://expertise.matdata.eu/static/matdata-expertise-shacl.ttl) (validation shapes)

## 📖 Overview

This repository contains my personal knowledge management system, structured as a semantic knowledge graph using Logseq as the authoring environment. The graph models:

- **Projects**: Professional work and initiatives
- **Techniques & Tools**: Technologies, programming languages, frameworks
- **Roles**: Professional roles and responsibilities  
- **Jobs**: Employment history with timeline
- **Companies**: Organizations I've worked with
- **Talks & Presentations**: Public speaking engagements
- **Categories**: SKOS-based taxonomies for organizing expertise

All content is authored in Logseq markdown pages with structured properties, automatically converted to RDF using the [logseq-rdf-export](https://github.com/MathiasVDA/logseq-rdf-export) tool, and validated against SHACL shapes to ensure data quality.

## 🏗️ Architecture

### Workflow

```
Logseq Pages (Markdown)
    ↓
logseq-rdf-export
    ↓
matdata-expertise-raw.ttl
    ↓
clean-graph.py (normalization)
    ↓
matdata-expertise.ttl
    ↓
validate-graph.py (SHACL validation)
    ↓
├─→ Static Website (Logseq SPA)
├─→ SPARQL Endpoint (Apache Jena Fuseki)
└─→ CV Generation (RenderCV)
```

### Key Components

1. **Logseq**: Knowledge authoring with structured properties
2. **RDF Export**: Custom tool to convert Logseq graph to RDF/Turtle
3. **Graph Cleaning**: Python script to normalize predicates and map categories
4. **SHACL Validation**: Ensures data quality and consistency
5. **CI/CD Pipeline**: GitLab/GitHub CI automates the entire workflow
6. **Publishing**: Multi-channel output (website, SPARQL, PDF CV)

## 🚀 Local Development

### Prerequisites

- Python 3.12+
- Docker (for RDF export)
- Git

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Expertise
```

2. Create a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\Activate.ps1
pip install -r kg-actions/requirements.txt
```

### Local Validation Workflow

Run the complete validation workflow locally:

```bash
# 1. Export Logseq to RDF
docker run -it -v ./:/data mathiasvda/logseq-rdf-export logseq-rdf-export matdata-expertise-raw.ttl --directory /data/

# 2. Clean and normalize the graph
python ./kg-actions/clean-graph.py

# 3. Validate against SHACL shapes
python ./kg-actions/validate-graph.py
```

Expected output for successful validation:
```
Number of triples in data graph: 2900
Number of triples in shacl graph: 168
Validation Report
Conforms: True
```

### Working with Logseq

Edit pages in the `pages/` directory following these conventions:

**Projects:**
```markdown
public:: true
type:: [[Project]]
description:: Brief description
has-category:: Strategy
has-tagged-techniques:: #Python, #RDF
has-tagged-roles:: #Developer
is-featured:: Yes
during-job:: #[[Job: Independent railway data freelancer]]
```

**Techniques:**
```markdown
public:: true
type:: [[Technique]]
self-estimated-proficiency:: Proficient
is-featured:: Yes
has-category:: Programming languages
```

See [kg-actions/shapes-explanation.md](kg-actions/shapes-explanation.md) for complete validation rules.

## 🔄 CI/CD Pipeline

The GitLab CI pipeline consists of 5 stages:

1. **RDF Export**: Convert Logseq to RDF using Docker image
2. **Validate**: Clean graph and run SHACL validation
3. **CV**: Generate PDF CV using RenderCV
4. **Pages**: Build static website using Logseq Publish SPA
5. **Upload**: Sync RDF data to SPARQL endpoint

Pipeline runs automatically on commits to the main branch.

## 📊 Data Model

The knowledge graph uses these main entity types:

- `d:Project` - Professional projects
- `d:Technique` - Skills, tools, technologies
- `d:Role` - Professional roles
- `d:Job` - Employment history
- `d:Company` - Organizations
- `d:Talk` - Presentations and talks
- `skos:Concept` - Taxonomy categories
- `skos:ConceptScheme` - Category schemes

Key predicates:
- `d:has-category` - Link to SKOS category
- `d:has-tagged-techniques` - Technologies used in project
- `d:has-tagged-roles` - Roles performed in project
- `d:self-estimated-proficiency` - Skill level
- `d:is-featured` - Highlight important items
- `d:during-job` - Job context for projects

## 🎯 SHACL Validation

SHACL shapes enforce:
- Required properties (labels, categories, dates)
- Cardinality constraints (min/max counts)
- Data type validation (strings, booleans, dates, IRIs)
- Category membership in correct SKOS concept schemes
- Proficiency level consistency
- Relationship integrity

See [kg-actions/matdata-expertise-shacl.ttl](kg-actions/matdata-expertise-shacl.ttl) for complete shapes.

## 📝 Scripts

- **clean-graph.py**: Normalizes RDF graph by mapping properties and merging SKOS concepts
- **validate-graph.py**: Validates RDF graph against SHACL shapes
- **formatter.py**: Utilities for RDF formatting
- **complete-cv.py**: Generates CV YAML from RDF data for RenderCV

## 🔗 Related Projects

- [logseq-rdf-export](https://github.com/MathiasVDA/logseq-rdf-export) - Export tool for Logseq to RDF
- [Yasgui](https://github.com/Matdata-eu/Yasgui) - SPARQL GUI for querying the endpoint
- [RenderCV](https://github.com/sinaatalay/rendercv) - CV generation from YAML

# Open Biomedical Ontology Knowledge Graphs

Knowledge graphs derived from some Open Biomedical Ontologies have been generated to capture the subsumption hierarchy as well as relations between concepts. Concept categories and relations have been mapped to corresponding Biolink concepts/relations.

## Available KGs

| Ontology | Version  | Format | Location |
| -------- | -------  | ------ | -------- |
| PR       | 20200818 | KGX    | [nodes.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/ontologies/pr/current/pr.owl-subclass-hierarchy.nodes.kgx.tsv.gz) / [edges.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/ontologies/pr/current/pr.owl-subclass-hierarchy.edges.kgx.tsv.gz) |


### PR KG
| Relations | |
| --------- | ----- |
| biolink:subclass_of | biolink:in_taxon |
| biolink:capable_of | biolink:lacks_part* |
| biolink:derives_from | biolink:located_in |
| biolink:has_component* | biolink:non_covalently_bound_to |
| biolink:has_gene_template* | biolink:output_of* |
| biolink:has_part | biolink:part_of |
| biolink:has_quality* | biolink:participates_in |

\* denotes a relation is not formally in Biolink currently

## KGX format

*Nodes*

| id | name | category |
| -- | ---- | -------- |
| PR:000040728 | cytochrome P450 1B1 isoform 1 | biolink:GeneProduct |


*Edges*

| subject | edge_label | object | relation | id | association_type |
| ------- | ---------- | ------ | -------- | -- | ---------------- |
| PR:A0A0A0MS15 | biolink:has_gene_template* | HGNC:5607 | PR:has_gene_template | pSl12weN9bGVPOyTGNcnF9q0etQ | biolink:GeneToGeneProductRelationship |



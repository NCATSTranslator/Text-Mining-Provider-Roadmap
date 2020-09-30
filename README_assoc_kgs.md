# Targeted Biolink Association Knowledge Graphs

The Text Mining Provider provides KGs consisting of explicitly targeted Biolink Associations extracted from sentences in the scientific literature. The association extraction pipeline makes use of concept annotations created by the same concept recognition system used for other aspects of the Text Mining Provider. Association classification is facilitated via a custom-tuned BERT model, one model per association type.

There is potential to generate associations between concepts from the following ontologies:
* [Chemical Entities of Biological Interest (CHEBI)](http://obofoundry.org/ontology/chebi.html)
* [Cell Ontology (CL)](http://obofoundry.org/ontology/cl.html)
* [Gene Ontology Biological Process (GO_BP)](http://obofoundry.org/ontology/go.html)
* [Gene Ontology Cellular Component (GO_CC)](http://obofoundry.org/ontology/go.html)
* [Gene Ontology Molecular Function (GO_MF)](http://obofoundry.org/ontology/go.html)
* [Human Phenotype Ontology (HP)](https://hpo.jax.org/app/)
* [Molecular Process Ontology (MOP)](http://obofoundry.org/ontology/mop.html)
* [Monarch Disease Ontology (MONDO)](https://mondo.monarchinitiative.org/)
* [NCBI Taxonomy (NCBITaxon)](http://obofoundry.org/ontology/ncbitaxon.html)
* [Protein Ontology (PRO)](http://obofoundry.org/ontology/pr.html)
* [Sequence Ontology (SO)](http://obofoundry.org/ontology/so.html)
* [Uberon multi-species anatomy ontology (UBERON)](http://obofoundry.org/ontology/uberon.html)

Please feel free to submit requests (as GitHub issues) for new concepts and/or associations to be mined from the scientific literature. For details on concept and association systems that are in development, please see the relevant GitHub issues for [new concept request](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+concept+type+request%22) and [new association requests](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+association+request%22)). 


## Extracted Associations
To date, there is a single extracted association type available:
* ChemicalToGeneAssociation (CHEBI up/down-regulates PR)


### A note about concept recognition using the Protein Ontology
When using the cooccurrence KGs, it may be important to note that the concept recognition pipeline for Protein Ontology (PRO) concepts tends to annotate to higher-level, species non-specific PRO concepts. This is a result of how the training data has been annotated. It turns out that it is often very difficult to determine the species for a given protein in text (difficult even for human annotators) so our tools make use of the higher-level, species-non-specific concepts. There may, therefore, be added inference steps required to traverse a knowledge graph from a species-specific entity to the species-non-specific PRO concept used in the annotation. In an effort to aid in this traversal, we have build a [knowledge graph consisting of the PRO subsumption and relation hierarchies](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/README_ontology_kgs.md). 


## Available KGs

| Version | Association type(s) | Format | Location | Example query |
| ------- | ------------------- | ------ | -------- | ------- |
| SepRelay | ChemicalToGeneAssociation (CHEBI up/down-regulates PR) | KGX   | [nodes.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/text-mined/current/text-mined.nodes.current.kgx.tsv.gz) / [edges.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/text-mined/current/text-mined.edges.current.kgx.tsv.gz) ||
| SepRelay | ChemicalToGeneAssociation (CHEBI up/down-regulates PR) | BioThings API | [API](https://biothings.ncats.io/text_mining_targeted_association) | [Find chemicals that can up-regulate a gene/protein](https://biothings.ncats.io/text_mining_targeted_association/query?q=object.id:NCBIGene\:944%20AND%20association.edge_label:positively_regulates_entity_to_entity%20&size=400) |





## KGX format
The KGX format for the targeted association KG makes use of two kinds of nodes:
 1. Entity nodes (similar to the other KGs produced by the Text Mining Provider)
 2. Evidence nodes - these nodes are referenced by edges and include the sentence and other related information used to assert a given association. The score in the evidence node is provided by the classifer that asserted the association.

*Nodes* 

| id | name | category | publications | score | sentence | subject_spans | relation_spans | object_spans | provided_by |
| -- | ---- | -------- | ------------ | ----- | -------- | ------------- | -------------- | ------------ | ----------- |
| CHEBI:3215  | bupivacaine  | biolink:ChemicalSubstance | |||||||
| PR:000031567  | leucine-rich repeat-containing protein 3B | biolink:GeneOrGeneProduct | |||||||
| 02T60dgTsntC9kC4rqtr5lIN8n0 | Evidence: CHEBI:3215 -neg-reg-> PR:000031567 |  biolink:InformationContentEntity | PMID:29085514 |0.99956816 | The administration of 50 ?g/ml bupivacaine promoted maximum breast cancer cell invasion, and suppressed LRRC3B mRNA expression in cells. | start: 31, end: 42  |   |  start: 104, end: 110  |  TMProvider |

*Edges*
| subject | edge_label | object | relation | id | association_type | evidence_count | has_evidence |
| ------- | ---------- | ------ | -------- | -- | ---------------- | -------------- | ------------ |
| CHEBI:3215 | biolink:negatively_regulates_entity_to_entity | PR:000031567 | RO:0002212 |IjbFtUdgNQk-HHlsBju-I_jpSnA | biolink:ChemicalToGeneAssociation | 1 | 02T60dgTsntC9kC4rqtr5lIN8n0 |




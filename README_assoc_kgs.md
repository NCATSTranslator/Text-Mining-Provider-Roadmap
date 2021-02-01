# Targeted Biolink Association Knowledge Graphs

The Text Mining Provider provides KGs consisting of explicitly targeted Biolink Associations extracted from sentences in the scientific literature. The association extraction pipeline makes use of concept annotations created by the same concept recognition system used for other aspects of the Text Mining Provider. Association classification is facilitated via a custom-tuned BERT model, one model per association type.

## Extracted Associations
To date, there is a single extracted association type available:
* [biolink:ChemicalToGeneAssociation](https://biolink.github.io/biolink-model/docs/ChemicalToGeneAssociation.html)
  * **CHEBI** [biolink:negatively_regulates_entity_to_entity](https://biolink.github.io/biolink-model/docs/negatively_regulates_entity_to_entity.html) **PR**
  * **CHEBI** [biolink:positively_regulates_entity_to_entity](https://biolink.github.io/biolink-model/docs/positively_regulates_entity_to_entity.html) **PR**
  
*Associations under-construction*
* [biolink:GeneRegulatoryRelationship](https://biolink.github.io/biolink-model/docs/GeneRegulatoryRelationship.html)
  * **PR** [biolink:negatively_regulates_entity_to_entity](https://biolink.github.io/biolink-model/docs/negatively_regulates_entity_to_entity.html) **PR**
  * **PR** [biolink:positively_regulates_entity_to_entity](https://biolink.github.io/biolink-model/docs/positively_regulates_entity_to_entity.html) **PR**
* [biolink:ChemicalToDiseaseOrPhenotypicFeatureAssociation](https://biolink.github.io/biolink-model/docs/ChemicalToDiseaseOrPhenotypicFeatureAssociation.html)
  * **CHEBI** [biolink:treats](https://biolink.github.io/biolink-model/docs/treats.html) **MONDO**
* [biolink:GeneToDiseaseAssociation](https://biolink.github.io/biolink-model/docs/GeneToDiseaseAssociation.html)
  * **PR** [biolink:contributes_to](https://biolink.github.io/biolink-model/docs/contributes_to.html) **MONDO**
* [biolink:DiseaseToPhenotypicFeatureAssociation](https://biolink.github.io/biolink-model/docs/DiseaseToPhenotypicFeatureAssociation.html)
  * **MONDO** biolink:has_symptom **HP**
* [biolink:GeneToExpressionSiteAssociation](https://biolink.github.io/biolink-model/docs/GeneToExpressionSiteAssociation.html)
  * **PR** [biolink:expressed_in](https://biolink.github.io/biolink-model/docs/expressed_in.html) **UBERON**



### A note about concept recognition using the Protein Ontology
When using the cooccurrence KGs, it may be important to note that the concept recognition pipeline for Protein Ontology (PRO) concepts tends to annotate to higher-level, species non-specific PRO concepts. This is a result of how the training data has been annotated. It turns out that it is often very difficult to determine the species for a given protein in text (difficult even for human annotators) so our tools make use of the higher-level, species-non-specific concepts. There may, therefore, be added inference steps required to traverse a knowledge graph from a species-specific entity to the species-non-specific PRO concept used in the annotation. In an effort to aid in this traversal, we have built a [knowledge graph consisting of the PRO subsumption and relation hierarchies](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/README_ontology_kgs.md). 


## Available KGs

| Version | Association type(s) | Format | Location |
| ------- | ------------------- | ------ | -------- |
| SepRelay | ChemicalToGeneAssociation (CHEBI up/down-regulates PR) | KGX   | [nodes.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/text-mined/current/text-mined.nodes.current.kgx.tsv.gz) / [edges.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/text-mined/current/text-mined.edges.current.kgx.tsv.gz) |
| SepRelay | ChemicalToGeneAssociation (CHEBI up/down-regulates PR) | BioThings API | [API](https://biothings.ncats.io/text_mining_targeted_association) |
| SepRelay | ChemicalToGeneAssociation (CHEBI up/down-regulates PR) | TRAPI v1.0 | [API](https://smart-api.info/ui/978fe380a147a8641caf72320862697b) |


## Requesting extraction of Biolink associations
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


## TRAPI v1.0
This KG consists of Biolink associations that have been extracted from sentences in the literature. For each text-mined Biolink association, the sentence(s) that were observed to assert the association are included as evidence/provenance/confidence (EPC) information. Specifically, each extracted Biolink association is accompanied by the following EPC information:

* The sentence from which the assertion was mined
* An identifier for the document that contains the sentence, e.g. the PubMed identifier
* The character offsets (relative to the sentence) for the text mentions of the subject and object concept of the assertion
* A confidence score for this specific text-mined assertion (right now this is the score reported by the classifier that identified the sentence)

Currently, each packet of EPC information (one per sentence that was observed to assert the association) is stored as an edge attribute in the TRAPI knowledge representation model. Because there may be more than one sentence observed to assert a single association, separate arrays are used to store the different EPC values whereby the index in the array inherently connects the EPC values for a single sentence. The example below demonstrates the TRAPI representation of edge attributes for an extracted Biolink association supported by two sentences in the literature.

#### Two example EPC packets describing sentences that assert `bupivacaine --downregulates--> LRRC3B`
```yaml
# This assertion is supported by two sentences in the literature
      {
        'publication': 'PMID:29085514', 
        'score': '0.99956816', 
        'sentence': 'The administration of 50 µg/ml bupivacaine promoted maximum breast cancer cell invasion, and suppressed LRRC3B mRNA expression in cells.', 
        'subject_spans': 'start: 31, end: 42', 
        'object_spans': 'start: 104, end: 110', 
        'provided_by': 'TMProvider'
      }

      {
        'publication': 'PMID:12345678', 
        'score': '0.876', 
        'sentence': 'This is a second sentence indicating that bupivacaine negatively regulates LRRC3B.', 
        'subject_spans': 'start: 42, end: 53', 
        'object_spans': 'start: 75, end: 81', 
        'provided_by': 'TMProvider'
      }
```

#### TRAPI v1.0 representation of the two EPC packets shown above
```yaml
edges:
  - id: 9445e98f72ada21aa572559e303e4d5ac414650f
    predicate: biolink:negatively_regulates,
    subject: CHEBI:3215          # bupivacaine
    object: PR:000031567       # LRRC3B
    attributes:
      - type: biolink:provided_by
        name: provided_by
        value: Text Mining KP
      - type: bts:api
        name: api
        value: Text Mining Targeted Association API
      - type: bts:score
        name: score
        value: 
          - 0.99956816
          - 0.876
      - type: bts:sentence
        name: sentence
        value: 
          - "The administration of 50 µg/ml bupivacaine promoted maximum breast cancer cell invasion, and suppressed LRRC3B mRNA expression in cells."
          - "This is a second sentence indicating that bupivacaine negatively regulates LRRC3B."
      - type: bts:subject_spans
        name: subject_spans
        value: 
          - "31|42"
          - "42|53"
      - type: bts:object_spans
        name: object_spans
        value: 
          - "104|110"
          - "75|81"
      - type: bts:publications
        name: publications
        value: 
          - PMID:29085514
          - PMID:12345678  
```




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




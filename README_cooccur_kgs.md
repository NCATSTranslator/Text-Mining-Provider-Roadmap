# Ontology Concept Cooccurrence Knowledge Graph

Cooccurrence of biomedical concepts within a single document or sentence can serve as a proxy for a potential relationship between two concepts. The Ontology Concept Cooccurrence KG links concepts from a collection of ontologies (see below) that are observed to cooccur within the same Medline title/abstract. Edges are scored based on the [Normalized Google Distance](https://en.wikipedia.org/wiki/Normalized_Google_distance) (NGD) metric. An edge score of 0.0 indicates two concepts are always observed to appear together in text. As the score moves away from 0.0 towards 1.0 and beyond, then the concepts are judged as more distant. 

The Text Mining Provider automatically identifies mentions of concepts from the Open Biomedical Ontologies listed below. Performance of the individual concept recognition systems has been evaluated against the CRAFT corpus, and other corpora. For details on concept recognition system performance, see [this link](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap#evaluation-of-concept-recognition-on-the-craft-test-corpus).

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


### A note about concept recognition using the Protein Ontology
When using the cooccurrence KGs, it may be important to note that the concept recognition pipeline for Protein Ontology (PRO) concepts tends to annotate to higher-level, species non-specific PRO concepts. This is a result of how the training data has been annotated. It turns out that it is often very difficult to determine the species for a given protein in text (difficult even for human annotators) so our tools make use of the higher-level, species-non-specific concepts. There may, therefore, be added inference steps required to traverse a knowledge graph from a species-specific entity to the species-non-specific PRO concept used in the annotation. In an effort to aid in this traversal, we have built a [knowledge graph consisting of the PRO subsumption and relation hierarchies](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/README_ontology_kgs.md). 

## Available KGs

#### PubMed/Medline

The current KG comprises cooccurrence data from ~30M PubMed/Medline titles & abstracts (2019 and prior) using all of the ontologies listed above.

| Version | Format | Location | Example query |
| ------- | ------ | -------- | ------------- |
| FebRelay | KGX   | [nodes.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/concept-cooccurrence/current/ngd-concept-cooccur.current.nodes.kgx.tsv.gz) / [edges.tsv](https://storage.googleapis.com/translator-tm-provider-knowledge-graphs/concept-cooccurrence/current/ngd-concept-cooccur.current.edges.kgx.tsv.gz) | |
| FebRelay | BioThings API | [API](https://biothings.ncats.io/text_mining_co_occurrence_kp) | [Find phenotypes related to a specific disease](https://biothings.ncats.io/text_mining_co_occurrence_kp/query?q=object.MONDO:%22MONDO:0003150%22%20AND%20subject.type:PhenotypicFeature&size=200) |
| FebRelay | TRAPI v1.0 | [API](https://smart-api.info/ui/5be0f321a829792e934545998b9c6afe) | |



## TRAPI v1.0

Evidence indicating the NGD score is associated with each edge using the TRAPI attribute schema as indicated below:

```yaml
"edges": {
    "d0ea69d75a346678f086b4481339619f": {
          "predicate": "biolink:related_to",
          "subject": "MONDO:0003295",
          "object": "MONDO:0024477",
          "attributes": [
            {
              "name": "provided_by",
              "value": "Text Mining KP",
              "type": "biolink:provided_by"
            },
            {
              "name": "api",
              "value": "Text Mining CO-OCCURRENCE API",
              "type": "bts:api"
            },
            {
              "name": "ngd",
              "value": 0.5923831250297802,
              "type": "bts:ngd"
            }
          ]
        }
      }
```

## KGX format

*Nodes*

| id | name | category |
| -- | ---- | -------- |
| PR:000040728 | cytochrome P450 1B1 isoform 1 | biolink:GeneOrGeneProduct |


*Edges*

| subject | edge_label | object | relation | id | association_type | NGD score |
| ------- | ---------- | ------ | -------- | -- | ---------------- | --------- |
| HP:0011443 | biolink:related_to | PR:000006949 | SIO:000001 | 0022f6fea0fbcdacfed80906b0af34aa9b9fc38ace17162310c4de2f4836b319 | biolink:Association | 0.5118571069107639 |

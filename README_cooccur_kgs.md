# Ontology Concept Cooccurrence Knowledge Graph

Cooccurrence of biomedical concepts within a single document or sentence can serve as a proxy for a potential relationship between two concepts. The Text Mining Provider produces knowledge graphs consisting of biomedical entities that are linked based on their cooccurrence within the scientific literature. Cooccurrence is monitored at several different levels within a document, e.g. cooccurrence in the title, in a sentence, in the entire document, etc. A suite of cooccurrence metrics is computed for each pair of concepts that are observed together. Two different representations of protein/gene entities are made available, one using human UniProt identifiers and the other using species-non-specific Protein Ontology identifiers (see documentation on the gene/protein represenation below). The current knowledge graph has been generated based on analysis of Medline titles only.

## Availablility

Protein Representation | Format | Location | Description
---------------------- | ------ | -------- | -----------
UniProt | KGX | [Google Bucket](https://console.cloud.google.com/storage/browser/translator-text-workflow-dev-public/kgx/UniProt) | The `cooccurrence_nodes.tsv.gz` and `cooccurrence_edges.tsv.gz` are the KGX formatted files housing the concept cooccurrence knowledge graph. The files are also available as a single `cooccurrence.tar.gz` tarball
UniProt | KGX | [Translator KGE Archive](https://archive.translator.ncats.io/) | Knowledge graph name = Cooccurrence
UniProt | TRAPI | [TRAPI Endpoint](https://smart-api.info/ui/5be0f321a829792e934545998b9c6afe) | The referenced endpoint supports lookup queries over the UniProt version of the concept cooccurrence knowledge graph
Protein Ontology | KGX | [Google Bucket](https://console.cloud.google.com/storage/browser/translator-text-workflow-dev-public/kgx/PR) | The files prefixed `cooccurrence_nodes` and `cooccurrence_edges` are the KGX formatted files housing the concept cooccurrence knowledge graph. 


## Documentation

The Text Mining Provider automatically identifies mentions of concepts from the resources listed below. Performance of the individual concept recognition systems has been evaluated against the CRAFT corpus, and other corpora. For details on concept recognition system performance, see [this link](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/blob/master/README_concept_recognition.md).

* [Chemical Entities of Biological Interest (CHEBI)](http://obofoundry.org/ontology/chebi.html)
* [Cell Ontology (CL)](http://obofoundry.org/ontology/cl.html)
* [Drugbank](https://go.drugbank.com/)
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


#### KGX / TRAPI attribute documentation
For a detailed description and example of our KGX format (which includes the structure of our TRAPI attribute representation), please see [this GitHub issue](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues/93).

#### Cooccurrence metrics

Cooccurrence metric | Description
------ | -----------
Normalized Google Distance | The Normalized Google Distance (NGD) computed for the subject and object concepts of the assertion. NGD is a measure of semantic similarity between two concepts derived from counts of the number of times they appear in a corpus of text. Concepts with the same or similar meaning will have an NGD score close to 0, while completely dissimilar concepts (those that never appear together) will have an infinite NGD score. For details see [Wikipedia](https://en.wikipedia.org/wiki/Normalized_Google_distance).
Pointwise Mutual Information | Pointwise mutual information is an information theoretic measure of association between two concepts based on the probabilities of observing the concepts in isolation and together. Mathematically, pmi(x,y) = log(p(x,y)/(p(x)p(y))). For details see [Bouma, G. (2009). Normalized (pointwise) mutual information in collocation extraction. Proceedings of GSCL, 30, 31-40.](https://svn.spraakdata.gu.se/repos/gerlof/pub/www/Docs/npmi-pfd.pdf).
Normalized Pointwise Mutual Information | Normalized Pointwise Mutual Information (NPMI) is PMI normalized to the range [1, -1]. When two concepts only occur together, NPMI = 1. When two concepts are observed to occur separately but never together, NPMI = -1. For details see [Bouma, G. (2009). Normalized (pointwise) mutual information in collocation extraction. Proceedings of GSCL, 30, 31-40.](https://svn.spraakdata.gu.se/repos/gerlof/pub/www/Docs/npmi-pfd.pdf).
Normalized Pointwise Mutual Information Max | Normalized Pointwise Mutual Information Max is a variant of NPMI proposed by Bouma 2009 whereby the PMI is normalized by -ln(max(p(x),p(y))). Using this normalization factor will result in an asymmetric measure whereby NPMImax=1 when one concept is occurs only in the context of another, but not necessarily the other way around. For details see: [Bouma, G. (2009). Normalized (pointwise) mutual information in collocation extraction. Proceedings of GSCL, 30, 31-40](https://svn.spraakdata.gu.se/repos/gerlof/pub/www/Docs/npmi-pfd.pdf).
Mutual Dependence | Mutual Dependency (MD), often also known as PMI², is a variant of PMI that attempts to overcome PMI's preference for rare events. For details, see [Thanopoulos, A., Fakotakis, N., & Kokkinakis, G. (2002, May). Comparative Evaluation of Collocation Extraction Metrics. In LREC (Vol. 2, pp. 620-625)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.11.8101&rep=rep1&type=pdf)
Log-Frequency Biased Mutual Dependence | Log-Frequency-Biased Mutual Dependency is a variant of Mutual Dependency that results in favoring the more frequently occuring pairs when ranking. For details, see [Thanopoulos, A., Fakotakis, N., & Kokkinakis, G. (2002, May). Comparative Evaluation of Collocation Extraction Metrics. In LREC (Vol. 2, pp. 620-625)](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.11.8101&rep=rep1&type=pdf).



#### Gene / protein concept representation using the Protein Ontology & UniProt
Our tools make use of the Protein Ontology when extracting mentions of proteins from text, however we have released a version of the targeted association knowledge graph that maps to human UniProt identifiers in order to facilitate improved integration with the Translator community. It is the UniProt version which is hosted in the Translator infrastructure, however the Protein Ontology version is available via KGX download. If one decides to use the original Protein Ontology version, it may be important to note that the concept recognition pipeline for Protein Ontology (PRO) concepts tends to annotate to higher-level, species non-specific PRO concepts. This is a result of how the training data has been annotated. It turns out that it is often very difficult to determine the species for a given protein in text (difficult even for human annotators) so our tools make use of the higher-level, species-non-specific concepts. There may, therefore, be added inference steps required to traverse a knowledge graph from a species-specific entity to the species-non-specific PRO concept used in the annotation.


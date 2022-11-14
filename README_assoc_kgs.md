# Targeted Biolink Association Knowledge Graph

The Text Mining Provider produces knowledge graphs consisting of explicitly targeted Biolink Associations mined from sentences in the scientific literature. Two different representations of protein/gene entities are made available, one using human UniProt identifiers and the other using species-non-specific Protein Ontology identifiers (see documentation on the gene/protein represenation below). The current knowledge graph has been generated based on analysis of Medline titles & abstracts and full text articles from the Pubmed Central Open Access Subset.

The figure below details the associations that have been extracted from the scientific literature. 

![targeted-assoc-kg-diagram](https://user-images.githubusercontent.com/7217210/201738410-a80b1fdd-311a-4ae3-8690-b204268e19f5.png)




## Availablility

Protein Representation | Format | Location | Description
---------------------- | ------ | -------- | -----------
UniProt | KGX | [Google Bucket](https://console.cloud.google.com/storage/browser/translator-text-workflow-dev-public/kgx/UniProt) | The `nodes.tsv.gz` and `edges.tsv.gz` files are the KGX formatted files housing the targeted association knowledge graph; they are also available as the single `targeted_assertions.tar.gz` tarball. 
UniProt | KGX | [Translator KGE Archive](https://archive.translator.ncats.io/) | Knowledge graph name = `Targeted Assertions`
UniProt | TRAPI | [TRAPI Endpoint](https://smart-api.info/ui/978fe380a147a8641caf72320862697b) | The referenced endpoint supports lookup queries over the UniProt version of the targeted association knowledge graph
Protein Ontology | KGX | [Google Bucket](https://console.cloud.google.com/storage/browser/translator-text-workflow-dev-public/kgx/PR) | The `nodes.tsv.gz` and `edges.tsv.gz` files are the KGX formatted files housing the targeted association knowledge graph. 

## Documentation

#### KGX / TRAPI attribute documentation
For a detailed description and example of our KGX format (which includes the structure of our TRAPI attribute representation), please see [this GitHub issue](https://github.com/biolink/kgx/issues/174#issuecomment-898612984).


#### Gene / protein concept representation using the Protein Ontology & UniProt
Our tools make use of the Protein Ontology when extracting mentions of proteins from text, however we have released a version of the targeted association knowledge graph that maps to human UniProt identifiers in order to facilitate improved integration with the Translator community. It is the UniProt version which is hosted in the Translator infrastructure, however the Protein Ontology version is available via KGX download. If one decides to use the original Protein Ontology version, it may be important to note that the concept recognition pipeline for Protein Ontology (PRO) concepts tends to annotate to higher-level, species non-specific PRO concepts. This is a result of how the training data has been annotated. It turns out that it is often very difficult to determine the species for a given protein in text (difficult even for human annotators) so our tools make use of the higher-level, species-non-specific concepts. There may, therefore, be added inference steps required to traverse a knowledge graph from a species-specific entity to the species-non-specific PRO concept used in the annotation.



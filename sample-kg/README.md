# Sample Knowledge Graphs
The Text Mining KP provides two knowledge graphs. The text-mined KG consists of explicit Biolink associations that have been mined from the scientific literature. The cooccurrence KG links ontology concepts that are found to cooccur in a sentence in the scientific literature more often than by chance.

## Text-mined KG
The *text-mined KG* contains assertions between pairs of ontology concepts that have been mined from the biomedical literature. Work is underway to extract assertions that have been prioritized by the Translator community (for details please see the relevant GitHub issues for [new concept request](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+concept+type+request%22) and [new association requests](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+association+request%22)). Please feel free to submit requests (as GitHub issues) for new concepts and/or associations to be mined from the scientific literature.

While development continues for the full-scale text-mined KG, a sample text-mined KG is provided. This sample KG leverages the manual annotation effort of the [CRAFT corpus](https://github.com/UCDenver-ccp/craft) and consists of instances of Biolink associations extracted from the CRAFT corpus. 

| Version | Format | Description |
| ------- | ------ | ----------- |
| [CRAFT-sample-v0.1](https://raw.githubusercontent.com/NCATSTranslator/Text-Mining-Provider-Roadmap/master/sample-kg/text-mined/kgx/v0.1) | KGX TSV | This sample KG consists of instances of ([biolink:GeneToExpressionSiteAssociations](https://biolink.github.io/biolink-model/docs/GeneToExpressionSiteAssociation.html)) extracted from the manual assertion annotation available as part of the CRAFT corpus |

## Concept cooccurrence KG
The second knowledge graph provided by the Text Mining KP consists of a cooccurrence network where the nodes are ontology concepts and links between nodes indicate that the two concepts cooccur in the same sentence, and that these concepts cooccur together more often than by chance.

**Coming soon: Conversion of the cooccurrence KG to KGX format is underway**

The cooccurrence network is comprised of data from ~40k documents from the CORD19 corpus (this is a COVID19-specific collection of scientific papers) and makes use of ontology concept from 10 of the Open Biomedical Ontologies. The list of ontologies is available [here](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/blob/master/README.md).
# Sample Knowledge Graphs
The Text Mining KP provides two types of knowledge graphs. The text-mined KG consists of explicit Biolink associations that have been mined from the scientific literature. The cooccurrence KG links ontology concepts that are found to cooccur in a sentence in the scientific literature more often than by chance.

## Text-mined KG
The *text-mined KG* contains assertions between pairs of ontology concepts that have been mined from the biomedical literature. Work is underway to extract assertions that have been prioritized by the Translator community (for details please see the relevant GitHub issues for [new concept request](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+concept+type+request%22) and [new association requests](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+association+request%22)). Please feel free to submit requests (as GitHub issues) for new concepts and/or associations to be mined from the scientific literature.

While development continues for the full-scale text-mined KG, a sample text-mined KG is provided. This sample KG leverages the manual annotation effort of the [CRAFT corpus](https://github.com/UCDenver-ccp/craft) and consists of instances of Biolink associations extracted from the CRAFT corpus. 

| Version | Format | Description |
| ------- | ------ | ----------- |
| [CRAFT-sample-v0.1](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/tree/add-sample-text-mined-kg-in-kgx-format/sample-kg/text-mined/kgx/v0.1) | KGX TSV | This sample KG consists of instances of ([biolink:GeneToExpressionSiteAssociations](https://biolink.github.io/biolink-model/docs/GeneToExpressionSiteAssociation.html)) extracted from the manual assertion annotation available as part of the CRAFT corpus |

#### KGX format used for the text-mined KG
There are two types of nodes present in the text-mined KG:
1. Entity nodes
   * The entity nodes represent a concept from an ontology. These nodes have values for the *id* and *category* fields.
2. Evidence nodes
   * The evidence nodes are referenced by the edges. Each edge is supported by at least one evidence node. All fields except for *name* are populated for each evidence node.

#### KGX Node Schema

   | Node column | description |
   | ---------- | ----------- |
   | id | If an entity node, this value is the ontology CURIE; if an evidence node this value is a URL-safe unique ID for the node. |
   | name | Not used (this column is always empty) |
   | category | If an entity node, this column is the category for the entity; if an evidence node, this column is *biolink:InformationContentEntity* |
   | sentence | Only populated if an evidence node; this value is the sentence text from where the edge assertion was mined. |
   | subject_spans | Only populated if an evidence node; this string value indicates the zero-indexed character offsets for the subject entity of the text-mined association within the sentence. The value uses the following pattern: *start:## end:##*. If the entity is represented by multiple spans, the patterns will be pipe-delimited. |
   | relation_spans | Only populated if an evidence node; this string value indicates the zero-indexed character offsets for the relation of the text-mined association within the sentence. The value uses the following pattern: *start:## end:##*. If the entity is represented by multiple spans, the patterns will be pipe-delimited. |
   | object_spans | Only populated if an evidence node; this string value indicates the zero-indexed character offsets for the object entity of the text-mined association within the sentence. The value uses the following pattern: *start:## end:##*. If the entity is represented by multiple spans, the patterns will be pipe-delimited. |
   | publication | Only populated if an evidence node; this value is the document CURIE to which the evidence sentence belongs.
   | provided_by | Only populated if an evidence node; this string value indicates the source of the evidence asserting a given edge. |


   #### KGX Edge Schema
   | Edge column | description |
   | ---------- | ----------- |
   | subject | The subject CURIE for the Biolink association represented by this edge. |
   | edge_label | The Biolink predicate CURIE for the Biolink association represented by this edge. |
   | object | The object CURIE for the Biolink association represented by this edge. |
   | relation | The relation CURIE for the Biolink association represented by this edge. |
   | id | This string value is a URL-safe unique ID for the node. |
   | association_type | The Biolink association type for this edge. |
   | has_evidence | A pipe-delimited list of *evidence node* identifiers. Each evidence node asserts the existence of this edge. |


#### Example KGX edge with evidence support

Below is the representation in KGX format for a `biolink:GeneToExpressionSiteAssociation` asserting that `ERK5 (PR:000010159) is expressed in (RO:0002206) the first branchial arch (UBERON:0004362)`.

##### Edges
   | subject | edge_label | object | relation | id | association_type | has_evidence |
   | ------- | ---------- |------- |--------- |--- |----------------- |------------- |
   | PR:000010159 | biolink:expressed_in | UBERON:0004362 | RO:0002206 | 9Hy20FTWHEGsy5nIuUaHuHLhNk4 | biolink:GeneToExpressionSiteAssociation | xK4hbaevM6H9gBugVaY_C85QBtM |

##### Nodes
   | id | name | category | sentence | subject_spans | relation_spans | object_spans | publication | 
   | -- | ---- | -------- | -------- | ------------- | -------------- | ------------ | ----------- |
   | PR:000010159 |  | biolink:GeneProduct | | | | |
   | UBERON:0004362 |  | biolink:AnatomicalEntity | | | | |
   | xK4hbaevM6H9gBugVaY_C85QBtM | biolink:InformationContentEntity | PMCID:PMC324396 | At E9.5 ERK5 expression was seen in the first and second branchial arch, cephalic region, somites and lateral ridge along the body wall. | start: 8, end: 12 | start: 13, end: 23 | start: 40, end: 45\|start: 57, end: 71 | CRAFT |

## Concept cooccurrence KG
The second knowledge graph provided by the Text Mining KP consists of a cooccurrence network where the nodes are ontology concepts and links between nodes indicate that the two concepts cooccur in the same sentence, and that these concepts cooccur together more often than by chance.

**Coming soon: Conversion of the cooccurrence KG to KGX format is underway**

The cooccurrence network is comprised of data from ~40k documents from the CORD19 corpus (this is a COVID19-specific collection of scientific papers) and makes use of ontology concept from 10 of the Open Biomedical Ontologies. The list of ontologies is available [here](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/blob/master/README.md).
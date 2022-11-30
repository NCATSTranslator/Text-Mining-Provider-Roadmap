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

## Documentation

### KGX format documentation
The KGX format consists of two files, one containing a list of nodes and associated metadata (`nodes.tsv`), and one containing a list of edges (`edges.tsv`). These files are available in the Google Bucket linked above.

### Format of the nodes.tsv file

| *curie* | *name* | *category* |
| -- | ---- | -------- | 
| CHEBI:3215  | bupivacaine  | biolink:ChemicalEntity |
| PR:000031567  | leucine-rich repeat-containing protein 3B | biolink:Protein |


### Proposed Edge TSV (Note: scroll table to see all columns)
| *subject_curie* | *predicate* | *object_curie* | *id* | *association_type* | *confidence_score* | *supporting_study_result_identifiers* | *supporting_publication_identifiers* | *_attributes* |
| -- | -- | -- | -- | -- | -- | -- | -- | -- |
| CHEBI:3215 | biolink:entity_negatively_regulates_entity | PR:000031567 | hcR2-6QIJratLDFyFxwcSO6UW1M | biolink:ChemicalToGeneAssociation | 0.9378 | tmkp:HCX2k2hTBVNSoReGxxsGcL33jsg\|tmkp:6c9D9220faF116beFa1e80800D4 | PMID:29085514\|PMID:12345678 |  `ATTRIBUTE_JSON_BLOB` |

where the `ATTRIBUTE_JSON_BLOB` would be JSON represented by the following YAML:
```yaml
- attribute_type_id: biolink:original_knowledge_source
  value: infores:text-mining-provider-targeted
  value_type_id: biolink:InformationResource
  description: The Text Mining Provider Targeted Biolink Association KP from NCATS Translator provides text-mined assertions from the biomedical literature.
  attribute_source: infores:text-mining-provider-targeted

- attribute_type_id: biolink:supporting_data_source
  value: infores:pubmed
  value_type_id: biolink:InformationResource
  attribute_source: infores:text-mining-provider-targeted

- attribute_type_id: biolink:supporting_document    ## NOT CURRENTLY IN BIOLINK
   value: PMID:29085514|PMID:12345678
   value_type_id: biolink:Publication
   description: The documents that contain the sentences that assert the Biolink association represented by the parent edge
   attribute_source: infores:pubmed

- attribute_type_id: biolink:tmkp_confidence_score
  value: 0.9378
  value_type_id: biolink:ConfidenceLevel
  description: An aggregate confidence score that combines evidence from all sentences that support the edge
  attribute_source: infores:text-mining-provider-targeted

- attribute_type_id: biolink:supporting_study_result    ## NOT CURRENTLY IN BIOLINK
      value: tmkp:HCX2k2hTBVNSoReGxxsGcL33jsg 
      value_type_id: biolink:TextMiningResult    ## NOT CURRENTLY IN BIOLINK
      description: a single result from running NLP tool over a piece of text     
      attribute_source: infores:text-mining-provider-targeted    
      attributes: 
      
        - attribute_type_id: biolink:supporting_text    ## NOT CURRENTLY IN BIOLINK
          value: The administration of 50 µg/ml bupivacaine promoted maximum breast cancer cell invasion, and suppressed LRRC3B mRNA expression in cells.
          value_type_id: EDAM:data_3671   # EDAM:text
          description: The text that asserts the relationship between the subject and object entity
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_document    ## NOT CURRENTLY IN BIOLINK
          value: PMID:29085514
          value_type_id: biolink:Publication
          value_url: https://pubmed.ncbi.nlm.nih.gov/29085514/
          description: The document that contains the sentence that asserts the Biolink association represented by the parent edge
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_document_type    ## NOT CURRENTLY IN BIOLINK
          value: Journal Article
          value_type_id: MESH:U000020 # publication type
          description: The publication type(s) for the document in which the sentence appears, as defined by PubMed; pipe-delimited
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_document_year    ## NOT CURRENTLY IN BIOLINK
          value: 2017
          value_type_id: UO:0000036  # year
          description: The year the document in which the sentence appears was published
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_text_located_in    ## NOT CURRENTLY IN BIOLINK
          value: IAO:0000315 # abstract
          value_type_id: IAO_0000314 # document_part 
          description: The part of the document where the sentence is located, e.g. title, abstract, introduction, conclusion, etc.
          attribute_source: infores:pubmed
 
    	- attribute_type_id: biolink:extraction_confidence_score    ## NOT CURRENTLY IN BIOLINK  
          value: 0.9995681
          value_type_id: EDAM:data_1772     # EDAM:score 
          description: The score provided by the underlying algorithm that asserted this sentence to represent the assertion specified by the parent edge
          attribute_source: infores:text-mining-provider-targeted

    	- attribute_type_id: biolink:subject_location_in_text    ## NOT CURRENTLY IN BIOLINK
          value: '31|42'
          value_type_id: SIO:001056 # SIO:character_position
          description: The start and end character offsets relative to the sentence for the subject of the assertion represented by the parent edge; start and end offsets are pipe-delimited, discontinuous spans are delimited using commas
          attribute_source:  infores:text-mining-provider-targeted

    	- attribute_type_id: biolink:object_location_in_text    ## NOT CURRENTLY IN BIOLINK
          value: '104|110'
          value_type_id: SIO:001056 # SIO:character_position
          description: The start and end character offsets relative to the sentence for the object of the assertion represented by the parent edge; start and end offsets are pipe-delimited, discontinuous spans are delimited using commas
          attribute_source: infores:text-mining-provider-targeted 


- attribute_type_id: biolink:supporting_study_result   
      value: tmkp:6c9D9220faF116beFa1e80800D4
      value_type_id: biolink:TextMiningResult    ## NOT CURRENTLY IN BIOLINK
      description: a single result from running NLP tool over a piece of text     
      attribute_source: infores:text-mining-provider-targeted    
      attributes: 
      
        - attribute_type_id: biolink:supporting_text    ## NOT CURRENTLY IN BIOLINK
          value: This is a second sentence indicating that bupivacaine negatively regulates LRRC3B.
          value_type_id: EDAM:data_3671   # EDAM:text
          description: The text that asserts the relationship between the subject and object entity
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_document    ## NOT CURRENTLY IN BIOLINK
          value: PMID:12345678
          value_type_id: biolink:Publication
          value_url: https://pubmed.ncbi.nlm.nih.gov/12345678/
          description: The document that contains the sentence that asserts the Biolink association represented by the parent edge
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_document_type    ## NOT CURRENTLY IN BIOLINK
          value: Journal Article
          value_type_id: MESH:U000020 # publication type
          description: The publication type(s) for the document in which the sentence appears, as defined by PubMed; pipe-delimited
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_document_year    ## NOT CURRENTLY IN BIOLINK
          value: 2017
          value_type_id: UO:0000036  # year
          description: The year the document in which the sentence appears was published
          attribute_source: infores:pubmed

    	- attribute_type_id: biolink:supporting_text_located_in    ## NOT CURRENTLY IN BIOLINK
          value: IAO:0000315 # abstract
          value_type_id: IAO_0000314 # document_part 
          description: The part of the document where the sentence is located, e.g. title, abstract, introduction, conclusion, etc.
          attribute_source: infores:pubmed
 
    	- attribute_type_id: biolink:extraction_confidence_score    ## NOT CURRENTLY IN BIOLINK  
          value: 0.876
          value_type_id: EDAM:data_1772     # EDAM:score 
          description: The score provided by the underlying algorithm that asserted this sentence to represent the assertion specified by the parent edge
          attribute_source: infores:text-mining-provider-targeted

    	- attribute_type_id: biolink:subject_location_in_text    ## NOT CURRENTLY IN BIOLINK
          value: '42|53'
          value_type_id: SIO:001056 # SIO:character_position
          description: The start and end character offsets relative to the sentence for the subject of the assertion represented by the parent edge; start and end offsets are pipe-delimited, discontinuous spans are delimited using commas
          attribute_source:  infores:text-mining-provider-targeted

    	- attribute_type_id: biolink:object_location_in_text    ## NOT CURRENTLY IN BIOLINK
          value: '75|81'
          value_type_id: SIO:001056 # SIO:character_position
          description: The start and end character offsets relative to the sentence for the object of the assertion represented by the parent edge; start and end offsets are pipe-delimited, discontinuous spans are delimited using commas
          attribute_source: infores:text-mining-provider-targeted 


```




Relevant discussion of this KGX / TRAPI attribute structure can be found in [this GitHub issue](https://github.com/biolink/kgx/issues/174#issuecomment-898612984).


### Gene / protein concept representation using the Protein Ontology & UniProt
Our tools make use of the Protein Ontology when extracting mentions of proteins from text, however we have released a version of the targeted association knowledge graph that maps to human UniProt identifiers in order to facilitate improved integration with the Translator community. It is the UniProt version which is hosted in the Translator infrastructure, however the Protein Ontology version is available via KGX download. If one decides to use the original Protein Ontology version, it may be important to note that the concept recognition pipeline for Protein Ontology (PRO) concepts tends to annotate to higher-level, species non-specific PRO concepts. This is a result of how the training data has been annotated. It turns out that it is often very difficult to determine the species for a given protein in text (difficult even for human annotators) so our tools make use of the higher-level, species-non-specific concepts. There may, therefore, be added inference steps required to traverse a knowledge graph from a species-specific entity to the species-non-specific PRO concept used in the annotation.



# NCATS Text Mining Provider Roadmap
This repository serves as a centralized location for organizing and tracking the development of the NCATS Translator Text Mining Provider. The Text Mining Provider aims to provide an up-to-date, Biolink-compatible, knowledge graph composed of assertions mined from the available full-text biomedical literature.  

A [project board](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/projects/1) is available to monitor progress of the milestones from the initial Text Mining Provider proposal.


## Feature requests and issues


## Available Knowledge Graphs

## Concept Recognition

Currently, the Text Mining Provider extracts mentions of concepts from ten Biolink-compatible [Open Biomedical Ontologies](http://obofoundry.org/):
* [Chemical Entities of Biological Interest (CHEBI)](http://obofoundry.org/ontology/chebi.html)
* [Cell Ontology (CL)](http://obofoundry.org/ontology/cl.html)
* [Gene Ontology Biological Process (GO_BP)](http://obofoundry.org/ontology/go.html)
* [Gene Ontology Cellular Component (GO_CC)](http://obofoundry.org/ontology/go.html)
* [Gene Ontology Molecular Function (GO_MF)](http://obofoundry.org/ontology/go.html)
* [Molecular Process Ontology (MOP)](http://obofoundry.org/ontology/mop.html)
* [NCBI Taxonomy (NCBITaxon)](http://obofoundry.org/ontology/ncbitaxon.html)
* [Protein Ontology (PR)](http://obofoundry.org/ontology/pr.html)
* [Sequence Ontology (SO)](http://obofoundry.org/ontology/so.html)
* [Uberon multi-species anatomy ontology (UBERON)](http://obofoundry.org/ontology/uberon.html)


### Evaluation of concept recognition on the CRAFT test corpus 
The [CRAFT corpus](https://github.com/UCDenver-ccp/craft) contains an evaluation set of 30 full text articles that have been used to evaluate the concept recognition systems used by the Text Mining Provider as they have developed. Development of these concept recognition systems There is a balance between concept recognition performance and runtime
| Ontology | P | R | F | Ontology | P | R | F | 
| -------- | - | - | - | -------- | - | - | - |
| CHEBI OGER | 0.6997 | 0.6609 | 0.6797 | CL OGER | 0.7849 | 0.6712 | 0.7236 |
| **CHEBI OGER+CRF** | **0.8559** | 0.5536 | 0.6723 | **CL OGER+CRF** | **0.7862** | 0.6419 | 0.7067 
|  |  |  |  |  
| GO_BP OGER | 0.5137 | 0.2823 | 0.3644 | GO_CC OGER | 0.8004 | 0.8447 | 0.8220 |
| **GO_BP OGER+CRF** | **0.5863** | 0.2405 | 0.3411 | **GO_CC OGER+CRF** | **0.9712** | 0.7801 | 0.8652 |
|  |  |  |  |  |  
| GO_MF OGER | 0.7467 | 0.6127 | 0.6731 | MOP OGER | 0.3043 | 0.6306 | 0.4106 |
| **GO_MF OGER+CRF** | **0.8135** | 0.4956 | 0.6159 | **MOP OGER+CRF** | **0.6000** | 0.3243 | 0.4211 |
|  |  |  |  |  |
| SO OGER | 0.4096 | 0.5257 | 0.4604 | UBERON OGER | 0.8162 | 0.5842 | 0.6810 |
| **SO OGER+CRF** | **0.6554** | 0.5018 | 0.5684 | **UBERON OGER+CRF** | **0.9266** | 0.5062 | 0.6547 |
|  |  |  |  |  | 
| NCBITAXON OGER | 0.4861 | 0.7816 | 0.5994 |  PR OGER | 0.3433 | 0.8121 | 0.4826 |
| NCBITAXON OGER+CRF | 0.5749 | 0.7511 | 0.6513 |  PR OGER+CRF | 0.5097 | 0.6445 | 0.5693 |
| **NCBITAXON OGER+CRF+USE_GENERAL** | **0.9222** | 0.7511 | 0.8279 | **PR OGER+CRF+CAT=GENE** | **0.6690** | 0.6448 | 0.6567 |


## BioLink Association Extraction



## Associated Code Repositories







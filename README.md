# NCATS Text Mining Provider Roadmap
This repository serves as a centralized location for organizing and tracking the development of the NCATS Translator Text Mining Provider. The Text Mining Provider aims to provide an up-to-date, Biolink-compatible, knowledge graph composed of assertions mined from the available full-text biomedical literature. While tools are developed to extract Biolink associations from the literature, a knowledge graph based on the cooccurrence of concepts in sentences will be used as a proxy, indicating a related_to relation between concepts.

A [project board](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/projects/1) is available to monitor progress of the milestones from the initial Text Mining Provider proposal.

## Feature requests and issues
The Text Mining Provider aims to serve the needs of the NCATS Translator community, and thus development efforts are prioritized based on community input and feedback. If you have a specific target you would like the Text Mining Provider to address, or would like to report a text mining error [please submit an issue to this repository](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues/new/choose).

A [project board](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/projects/2) is available to monitor feature requests and issues as they migrate through the different stages of development.

## Available Knowledge Graphs

### Concept cooccurrence KG
| Version | Description |
| 1.0.2 | This initial KG is based on concept cooccurrence in sentences in the CORD-19 corpus. |
| 1.1 | (under construction) This KG will use the updated concept recognition systems over the CORD-19 corpus. |


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
The [CRAFT corpus](https://github.com/UCDenver-ccp/craft) contains an evaluation set of 30 full text articles that have been used to evaluate the concept recognition systems used by the Text Mining Provider as they have developed. There is a balance between concept recognition performance and runtime that must be maintained in order to achieve adequate performance, but be able to process documents at scale. Versions of the concept recognition systems used for available KGs and their respective performances are detailed below. 
| Ontology | Version | P | R | F | 
| -------- | - | - | - | - |
| CHEBI OGER | 1.0.2 | 0.6997 | 0.6609 | 0.6797 | 
| **CHEBI OGER+CRF** | 1.1 | **0.8559** | 0.5536 | 0.6723 |
|  |  |  |  |  | 
| CL OGER | 1.0.2 | 0.7849 | 0.6712 | 0.7236 |
| **CL OGER+CRF** | 1.1 | **0.7862** | 0.6419 | 0.7067 |
|  |  |  |  |  |
| GO_BP OGER | 1.0.2 | 0.5137 | 0.2823 | 0.3644 | 
| **GO_BP OGER+CRF** | 1.1 | **0.5863** | 0.2405 | 0.3411 |
|  |  |  |  |  |
| GO_CC OGER | 1.0.2 | 0.8004 | 0.8447 | 0.8220 |
| **GO_CC OGER+CRF** | 1.1 | **0.9712** | 0.7801 | 0.8652 |
|  |  |  |  |  |  
| GO_MF OGER | 1.0.2 | 0.7467 | 0.6127 | 0.6731 | 
| **GO_MF OGER+CRF** | 1.1 | **0.8135** | 0.4956 | 0.6159 | 
|  |  |  |  |  |  
| MOP OGER | 1.0.2 | 0.3043 | 0.6306 | 0.4106 |
| **MOP OGER+CRF** | 1.1 | **0.6000** | 0.3243 | 0.4211 |
|  |  |  |  |  |
| NCBITAXON OGER | 1.0.2 | 0.4861 | 0.7816 | 0.5994 |  
| NCBITAXON OGER+CRF | n/a | 0.5749 | 0.7511 | 0.6513 | 
| **NCBITAXON OGER+CRF+USE_GENERAL** | 1.1 | **0.9222** | 0.7511 | 0.8279 |
|  |  |  |  |  | 
| PR OGER | 1.0.2 | 0.3433 | 0.8121 | 0.4826 |
| PR OGER+CRF | n/a | 0.5097 | 0.6445 | 0.5693 |
| **PR OGER+CRF+CAT=GENE** | 1.1 | **0.6690** | 0.6448 | 0.6567 |
|  |  |  |  |  | 
| SO OGER | 1.0.2 | 0.4096 | 0.5257 | 0.4604 | 
| **SO OGER+CRF** | 1.1 | **0.6554** | 0.5018 | 0.5684 | 
|  |  |  |  |  | 
| UBERON OGER | 1.0.2 | 0.8162 | 0.5842 | 0.6810 |
| **UBERON OGER+CRF** | 1.1 | **0.9266** | 0.5062 | 0.6547 |


## BioLink Association Extraction
Initial development of tools to extract explicit Biolink associations is underway. For details, please see [these issues](https://github.com/NCATSTranslator/Text-Mining-Provider-Roadmap/issues?q=is%3Aissue+is%3Aopen+label%3A%22new+association+request%22).


## Associated Code Repositories
* [Translator TM Provider Infrastructure Modules](https://github.com/UCDenver-ccp/Translator-TM-Provider-Infrastructure-Modules)
  * Kubernetes cluster configuration files (Terraform)
  * Kubernetes service configuration files (Helm)
* [Translator TM Provider Infrastructure Live](https://github.com/UCDenver-ccp/Translator-TM-Provider-Infrastructure-Live)
  * Facilitates staging and production environments
* [Translator TM Provider Pipelines](https://github.com/UCDenver-ccp/Translator-TM-Provider-Pipelines)
 * Apache Beam pipelines used to populate 
* [Translator NLP Evaluation Service](https://github.com/UCDenver-ccp/Translator-nlp-eval-service)






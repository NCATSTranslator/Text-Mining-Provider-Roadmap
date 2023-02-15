# Relation Classification
Performance of the tuned BERT models used to classify sentences for particular relations between entities are shown in the table below. 

Note that the predicates shown below are shortcuts for the qualified predicates used in the KG knowledge representation.

## Biolink:Chemical To Disease Or Phenotypic Feature Association
| relation                 |  TP  |  TN  |  FP  |  FN  | Precision | Recall | Fscore |
| ------------------------ | ---- | ---- | ---- | ---- | --------- | ------ | ------ |
| causes_or_contributes_to |  126    |  1965    |  37    |  34    |   0.773        |  0.787      |  0.780      |
| treats                   |  327    |  1694    |  90    |  51    |   0.784        | 0.865       |  0.823      |
| no_relation              |  1510    |  466    |  72    |  114    |  0.954         | 0.930       | 0.942       |


## Biolink:Chemical to Gene Association
| relation                | TP   |  TN  |   FP  |  FN  | Precision | Recall | Fscore |
| ----------------------- | ---- | ---- |---- | ---- | --------- | ------ | ------ |
| negatively_regulates    | 944     |  8355   | 97    |  89    |  0.907         |  0.914      |  0.910      |
| positively_regulates    | 323     |  9038    | 59    |  65    |  0.846         |  0.832      |  0.839      |
| no_relation             | 7926     |  1285    | 136    | 138     |  0.983         | 0.983       | 0.983       |

## Biolink:Gene Regulatory Relationship Association
| relation                 | TP   |  TN  |   FP  |  FN  | Precision | Recall | Fscore |
| ------------------------ | ---- | ---- |---- | ---- | --------- | ------ | ------ |
|  negatively_regulates    |  45    |   991   |  9   |  13    |  0.833         | 0.776       | 0.804       |
|  positively_regulates    |  76    |  962    |  7   |   13   |  0.916         | 0.854       |  0.884      |
|  no_relation             |   901   |  127    |  20   |  10    |   0.978        |  0.989      |  0.984      |


## Biolink:Gene to Disease Association
| relation           | TP   |  TN  |   FP  |  FN  | Precision | Recall | Fscore |
| ------------------ | ---- | ---- |---- | ---- | --------- | ------ | ------ |
| contributes_to     |  122    |  42    | 26    |  20    |   0.824        |  0.859      |  0.841      |
| false              |  42    |  122    |  20   |  26    |    0.677       |   0.618     |   0.646     |


## Biolink:Gene to Disease Association (Loss/Gain of Function)
| relation                                | TP   |  TN  |   FP  |  FN  | Precision | Recall | Fscore |
| --------------------------------------- | ---- | ---- |---- | ---- | --------- | ------ | ------ |
| contributes_to_via_gain_of_function     |   7   | 391     |  3   |  0    |    0.700       |  1.000      |  0.824      |
| contributes_to_via_loss_of_function     |  43    |  305    |  16   |  37    |    0.729       |  0.537      |  0.619      |
| no_relation                             |  296    |  51    |  36   |  18    |    0.892       |  0.943      |  0.916      |


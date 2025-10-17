# Drug-likeness scoring based on unsupervised learning

Unsupervised RNN-based language model trained only on known drugs, predicting drug-likeness scores that reflect progression through drug development stages, without relying on negative samples or overconfident binary outputs.

This model was incorporated on 2025-07-09.


## Information
### Identifiers
- **Ersilia Identifier:** `eos5pt8`
- **Slug:** `druglikeness-unsupervised`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Drug-likeness`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** The higher the score, the higher the drug-likeness. FDA average value is 79.4. ChEMBL average value is 64.1. GDB-17 average value is 39.4.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| drug_likeness | float | high | Predicted drug-likeness score |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5pt8](https://hub.docker.com/r/ersiliaos/eos5pt8)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5pt8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5pt8.zip)

### Resource Consumption
- **Model Size (Mb):** `98`
- **Environment Size (Mb):** `7227`
- **Image Size (Mb):** `5793.76`

**Computational Performance (seconds):**
- 10 inputs: `27.91`
- 100 inputs: `19.99`
- 10000 inputs: `236.54`

### References
- **Source Code**: [https://github.com/SeonghwanSeo/drug-likeness](https://github.com/SeonghwanSeo/drug-likeness)
- **Publication**: [https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc05248a](https://pubs.rsc.org/en/content/articlehtml/2022/sc/d1sc05248a)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [arnaucoma24](https://github.com/arnaucoma24)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5pt8
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5pt8
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!

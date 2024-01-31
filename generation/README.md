# Code migration using Azure OpenAI

### Introduction
This repository contains the code for the Azure OpenAI code migration project. The project aims to migrate code that might contain legacy componets to a new version based on provided API documentation using RAG techniques. The project is built using the Azure OpenAI API and the Azure Functions framework.

### Python Setup

1. Install Python 3.8 or later. You can download Python from the [official Python website](https://www.python.org/downloads/).

2. Create Conda environment using the following command:
```bash
conda create -n code-migration python=3.10
```
3. Activate conda environment and install the required packages using the following command:
```bash
pip install -r requirements.txt
```
4. Rename secrets.env.rename to secrets.env and fill in the required values.
4. Open vectordb_builder.ipynb notebook and attach the conda environment to the notebook.
5. Once the vector database is built, run the code_gen_with_rag.ipynb notebook to generate the code.
6. Review the generated code and make any necessary changes.



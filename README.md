# QM-GRUNGE

```text
                 /\ 
                /  \        /\ 
           /\  / /\ \      /  \ 
          /  \/ /  \ \    / /\ \ 
         / /\  / /\ \ \  / /  \ \ 
        /_/  \/_/  \_\_\/_/    \_\_

           Quantitative Modelling — Notebooks, Data, Experiments
```

## Overview

**QM-GRUNGE** is the working repository for our group project in **BASc0005: Quantitative Methods 2 – Data Science and Visualisation** at UCL.  

This repository contains all datasets, analysis notebooks, figures, and intermediate outputs used to build our final **group website**, which analyses and visualises a real-world dataset in its wider social, political, or cultural context.

The project follows the structure of a data-driven research workflow taught in the module, using Python to support:

- Data cleaning and manipulation  
- Statistical and exploratory analysis  
- Visualisation and mapping  
- Interpretation of results in relation to context and literature  

The notebooks in this repository are used to develop, test, and document the analysis that is ultimately presented on the website, including the methods, visualisations, and conclusions required for the final assessment.

---

## Repository Structure

```
QM-GRUNGE/
│
├── weather_becky1.ipynb      # Example notebook
│
├── Datasets/                 # Raw and processed datasets
├── Factors/                  # Factor data and intermediate results
├── Graphs/                   # Generated figures and plots
├── Regression/               # Regression experiments and outputs
└── Rough_Work/               # Scratch work and exploratory notebooks
```

Most content is stored in Jupyter notebooks (`.ipynb`).

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/snig-17/QM-GRUNGE.git
cd QM-GRUNGE
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate the environment:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```bash
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

If not, install a minimal scientific stack:

```bash
pip install --upgrade pip
pip install jupyterlab notebook numpy scipy pandas matplotlib seaborn scikit-learn ipywidgets
```

### 4. Launch Jupyter

```bash
jupyter lab
```

or

```bash
jupyter notebook
```

Then open `weather_becky1.ipynb` or any other notebook and run the cells.

---

## Suggested requirements.txt

For reproducible installs, create `requirements.txt` with:

```
jupyterlab
notebook
numpy
scipy
pandas
matplotlib
seaborn
scikit-learn
ipywidgets
```

---

## Usage Notes

### Data

Place external data files under:

```
Datasets/
```

Update notebook paths as needed.

### Kernels and Package Requirements

Notebooks assume a Python kernel. If a notebook requires specific packages or versions, document that in the notebook and/or in `requirements.txt` or `environment.yml`.

### Large Files

If large datasets or generated outputs are added, consider Git LFS or linking to external storage.

---

## Recommended Workflow

- Use JupyterLab or VS Code for interactive development.
- Commit notebooks regularly.
- Clear notebook outputs before committing to keep diffs smaller:

```bash
jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace your_notebook.ipynb
```

- Use feature branches for experimental work and open pull requests for review.

---

## Contributing

1. Open an issue describing a bug or feature request.
2. Fork the repository and create a branch.
3. Make changes and commit them.
4. Open a pull request with a clear description.

If you add new notebooks, include a short README in the folder describing purpose and dependencies.

---

## Issues and Support

For questions or problems, open an issue on GitHub:
https://github.com/snig-17/QM-GRUNGE/issues

---

## License

No license file is currently included. Add a LICENSE file (e.g. MIT, Apache-2.0, or CC-BY for notebooks/data) to specify reuse terms.

---

## Authors

- Alice Caiger - https://github.com/alicecaiger
- Becky Redmayne  
- Claire Tu - https://github.com/claire-tu314
- Shayna Gail Velasquez - https://github.com/shynnnexe
- Snigdha Tiwari - https://github.com/snig-17
- Rania Harryanto - 

---

## Acknowledgements and Citation

If this repository supports a paper or academic project, add citation information here (BibTeX, DOI, or reference).

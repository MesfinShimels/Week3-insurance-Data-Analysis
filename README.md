 AlphaCare Insurance Solutions (ACIS) Data Analysis Project

 Business Objective
AlphaCare Insurance Solutions (ACIS) aims to leverage cutting-edge risk and predictive analytics to optimize car insurance marketing strategies in South Africa. This project analyzes historical insurance claim data to identify opportunities for targeting "low-risk" customers with reduced premiums to attract new clients.

 Key Deliverables
- Conduct exploratory data analysis (EDA) to uncover actionable insights.
- Implement a robust machine learning pipeline to predict key factors influencing insurance claims.
- Provide recommendations based on data analysis to refine insurance products and strategies.
- Deliver modular, version-controlled, and reproducible code with CI/CD.

 Project Structure
```plaintext
.
├── .dvc/               DVC configuration and cache files
├── Data/              Raw and processed datasets
│   └── Data.csv           Original dataset
│   └── processed_Data.csv  Preprocessed dataset
│   └── cleaned_Data.csv    Cleaned dataset
│   └── final_Data.csv      Dataset after outlier removal
├── src/               Source code for data processing and modeling
│   └── preprocess.py      Preprocessing script
│   └── clean_data.py      Cleaning script
│   └── remove_outliers.py  Outlier removal script
│   └── evaluate.py        Model evaluation script
├── scripts/           Additional scripts for analysis
│   └── data_analysis.py   Exploratory Data Analysis script
├── notebook/          Jupyter notebooks for interactive analysis
├── .github/           CI/CD workflows
│   └── workflows/
│       └── unittests.yml   GitHub Actions workflow
├── README.md          Project documentation
├── dvc.yaml           DVC pipeline configuration
├── dvc.lock           DVC lock file
├── requirements.txt   Python dependencies
```

 Pipeline Overview
The project pipeline is managed using DVC and consists of the following stages:

 1. Preprocessing
Script: `src/preprocess.py`
- Cleans the raw data and generates `processed_Data.csv`.
- Command: `python src/preprocess.py --input Data/Data.csv --output Data/processed_Data.csv`

 2. Cleaning
Script: `src/clean_data.py`
- Further cleans the preprocessed data to produce `cleaned_Data.csv`.
- Command: `python src/clean_data.py --input Data/processed_Data.csv --output Data/cleaned_Data.csv`

 3. Outlier Removal
Script: `src/remove_outliers.py`
- Removes outliers from the cleaned data and outputs `final_Data.csv`.
- Command: `python src/remove_outliers.py --input Data/cleaned_Data.csv --output Data/final_Data.csv`

 4. Evaluation
Script: `src/evaluate.py`
- Evaluates the data pipeline and generates insights.
- Command: `python src/evaluate.py --input Data/final_Data.csv --model model.pkl`

 Tasks Completed

 Task 1: Git and GitHub
- Initialized a Git repository and implemented version control.
- Set up CI/CD pipelines using GitHub Actions.
- Created descriptive commit messages and maintained a clean Git history.

 Task 2: Exploratory Data Analysis (EDA)
- Performed data summarization, univariate and bivariate analysis.
- Generated visualizations to highlight key insights, including outlier detection and correlation analysis.

 Task 3: Data Version Control
- Installed and configured DVC for data versioning.
- Tracked and managed dataset versions through DVC commands.
- Stored datasets in a local remote storage setup.

 Data Insights
- Total Premium vs. Total Claims: Identified correlations and outlier patterns.
- Geographical Trends: Explored trends across provinces and postal codes.
- Vehicle Features: Analyzed the impact of vehicle specifications (e.g., engine capacity) on claim patterns.

 Learning Outcomes
- Data Engineering: Enhanced skills in data filtering, transformation, and versioning.
- Predictive Analytics: Gained insights into insurance risk factors using statistical and machine learning models.
- Software Development: Developed modular Python code adhering to best practices.
- Collaboration: Applied CI/CD for smooth team collaboration and reproducibility.

 Key Dates
- Challenge Introduction: 25 Dec 2024
- Interim Submission: 27 Dec 2024
- Final Submission: 31 Dec 2024

 Contributors
- Facilitator: Mahlet
- Team Members: Kerod, Rediet, Elias, Rehmet, Emtinan

 Requirements
Install project dependencies:
```bash
pip install -r requirements.txt
```

 Running the Pipeline
Execute the DVC pipeline:
```bash
dvc repro
```

Push data to remote storage:
```bash
dvc push
```


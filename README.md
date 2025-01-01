AlphaCare Insurance Solutions (ACIS) Data Analysis Project
Business Objective
AlphaCare Insurance Solutions (ACIS) aims to leverage advanced risk and predictive analytics to optimize car insurance marketing strategies in South Africa. This project focuses on analyzing historical insurance claim data to identify opportunities for targeting "low-risk" customers with reduced premiums to attract new clients.

Key Deliverables
•	Comprehensive Exploratory Data Analysis (EDA): Uncover actionable insights from historical data.
•	Machine Learning Pipeline: Develop a robust system to predict key factors influencing insurance claims.
•	Data-Driven Recommendations: Refine insurance products and marketing strategies based on analytical insights.
•	Reproducible Code: Deliver modular, version-controlled, and reproducible code integrated with CI/CD workflows.

Project Structure
.
├── .dvc/               # DVC configuration and cache files
├── Data/               # Raw and processed datasets
│   ├── Data.csv           # Original dataset
│   ├── processed_Data.csv # Preprocessed dataset
│   ├── cleaned_Data.csv   # Cleaned dataset
│   └── final_Data.csv     # Dataset after outlier removal
├── src/                # Source code for data processing and modeling
│   ├── preprocess.py      # Preprocessing script
│   ├── clean_data.py      # Cleaning script
│   ├── remove_outliers.py # Outlier removal script
│   ├── evaluate.py        # Model evaluation script
│   └── train.py           # Model training script
├── scripts/            # Additional scripts for analysis
│   ├── data_analysis.py   # Exploratory Data Analysis script
│   └── ab_hypothesis_testing.py # Hypothesis testing script
├── notebook/           # Jupyter notebooks for interactive analysis
│   ├── AB_hypothesis.ipynb      # Hypothesis testing notebook
│   ├── Data_Version_Control(DVC).ipynb # DVC pipeline walkthrough
│   └── training.ipynb           # Model training notebook
├── .github/            # CI/CD workflows
│   ├── workflows/
│   │   └── unittests.yml   # GitHub Actions workflow
├── README.md           # Project documentation
├── dvc.yaml            # DVC pipeline configuration
├── dvc.lock            # DVC lock file
├── requirements.txt    # Python dependencies
└── tests/              # Unit tests for pipeline and models
    ├── __init__.py
    ├── test_preprocess.py  # Tests for preprocessing
    ├── test_clean_data.py  # Tests for cleaning
    └── test_evaluate.py    # Tests for evaluation

Image Description
Below is a conceptual diagram illustrating the data pipeline stages:
Data Analysis Workflow:
•	Raw Data Collection
•	Data Preprocessing
•	Cleaning and Outlier Removal
•	Machine Learning Model Training
•	Insights and Visualization
Included Diagram:
(Refer to the attached image for a detailed visual representation of the pipeline.)

Pipeline Overview
The project pipeline is managed using DVC and consists of the following stages:
1. Preprocessing
•	Script: src/preprocess.py
•	Purpose: Cleans the raw data and generates processed_Data.csv.
•	Command: 
•	python src/preprocess.py --input Data/Data.csv --output Data/processed_Data.csv
2. Cleaning
•	Script: src/clean_data.py
•	Purpose: Further cleans the preprocessed data to produce cleaned_Data.csv.
•	Command: 
•	python src/clean_data.py --input Data/processed_Data.csv --output Data/cleaned_Data.csv
3. Outlier Removal
•	Script: src/remove_outliers.py
•	Purpose: Removes outliers from the cleaned data and outputs final_Data.csv.
•	Command: 
•	python src/remove_outliers.py --input Data/cleaned_Data.csv --output Data/final_Data.csv
4. Model Training
•	Script: src/train.py
•	Purpose: Trains machine learning models using the prepared data.
•	Command: 
•	python src/train.py --input Data/final_Data.csv --model_output models/model.pkl
5. Evaluation
•	Script: src/evaluate.py
•	Purpose: Evaluates the trained model and generates insights.
•	Command: 
•	python src/evaluate.py --input Data/final_Data.csv --model models/model.pkl

Key Insights
Claim-to-Premium Ratios
•	Identified significant variations in claim-to-premium ratios across provinces, highlighting regional risk differences.
Vehicle Features
•	Analyzed the impact of vehicle specifications such as engine capacity, registration year, and kilowatts on claim frequencies.
Gender Trends
•	Examined gender-based patterns in claims to tailor marketing strategies.

Recommendations
1.	Regional Focus: Target regions like Mpumalanga and Northern Cape with low claim-to-premium ratios to attract "low-risk" customers.
2.	Vehicle-Based Segmentation: Offer premium discounts for vehicles with features associated with lower claims.
3.	Gender-Based Marketing: Use gender insights to craft targeted campaigns.
4.	Continuous Monitoring: Regularly update models and datasets to reflect evolving trends.

How to Run the Project
Install Dependencies
Ensure all required Python libraries are installed. Run:
pip install -r requirements.txt
Main Libraries Used
•	aiohttp (3.11.11): Asynchronous HTTP client/server framework.
•	celery (5.4.0): Task queue for distributed systems.
•	dvc (3.58.0): Data version control.
•	matplotlib (3.10.0): Visualization library.
•	numpy (2.0.2): Fundamental package for numerical computation.
•	pandas (2.2.3): Data manipulation and analysis.
•	scikit-learn (1.6.0): Machine learning framework.
•	seaborn (0.13.2): Statistical data visualization.
•	xgboost (2.1.3): Gradient boosting framework.
Execute the DVC Pipeline
Run the complete pipeline:
dvc repro
Push Data to Remote Storage
To ensure data consistency and versioning:
dvc push

Contributors
•	Developed by Mesfin Shimels

Results Documentation
All the results and plots generated during this project are saved as screenshots in the screenshots directory within the project. This includes every diagram and chart mentioned in the report, ensuring all visual insights are readily accessible for reference.
Note: For a complete understanding of the project's flow and its insights, please refer to the attached pipeline diagram and analysis results.


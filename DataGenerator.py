import pandas as pd
import numpy as np
from faker import Faker

def generate_synthetic_medical_data(num_records=1000):
    """
    Copy the following prompt and paste it into an LLM (eg, ChatGPT, Gemini) to generate fake data about anything. Mentioning why you need it may not be necessary. If you improve the quality of the prompt, You might get an even better result
    Write a Python script that generates Synthetic medical data about a patient's history. 
    The data should contain variables that can be used to Build a machine learning model to predict healthcare costs based on patient demographics, previous claims, and medical history.
    """

    fake = Faker()

    data = {
        'PatientID': [fake.uuid4() for _ in range(num_records)],
        'Age': np.random.randint(18, 90, size=num_records),
        'Gender': np.random.choice(['Male', 'Female'], size=num_records),
        'Race': np.random.choice(['White', 'Black', 'Asian', 'Hispanic', 'Other'], size=num_records),
        'Location': [fake.city() for _ in range(num_records)],
        'Diagnoses': [fake.text(max_nb_chars=50) for _ in range(num_records)],
        'Procedures': [fake.text(max_nb_chars=50) for _ in range(num_records)],
        'Medications': [fake.text(max_nb_chars=50) for _ in range(num_records)],
        'Claims': [fake.text(max_nb_chars=100) for _ in range(num_records)],
        'Charges': np.random.uniform(100, 10000, size=num_records),
        'Payments': np.random.uniform(50, 8000, size=num_records),
        'InsuranceType': np.random.choice(['Private', 'Medicaid', 'Medicare', 'Self-Pay'], size=num_records),
        'ChronicConditions': np.random.choice(['Yes', 'No'], size=num_records),
        'VisitType': np.random.choice(['Inpatient', 'Outpatient', 'Emergency'], size=num_records),
        'LengthOfStay': np.random.randint(0, 10, size=num_records),  # 0 for outpatient and emergency
        'IncomeLevel': np.random.choice(['Low', 'Medium', 'High'], size=num_records),
        'DateOfService': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_records)]
    }

    df = pd.DataFrame(data)
    return df

synthetic_data = generate_synthetic_medical_data(1000)

synthetic_data.to_csv('patient_medical_History.csv',index=False)
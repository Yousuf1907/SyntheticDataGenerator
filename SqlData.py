import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Parameters for generating data
NUM_PATIENTS = 1000  # Number of patients
NUM_DOCTORS = 50  # Number of doctors
NUM_VISITS = 5000  # Number of hospital visits
SPECIALIZATIONS = ['Cardiology', 'Neurology', 'Pediatrics', 'Orthopedics', 'General Medicine']
DIAGNOSES = ['Hypertension', 'Diabetes', 'Asthma', 'Flu', 'COVID-19', 'Fracture', 'Migraine']

# Function to generate a random date within the past year
def random_date():
    start_date = datetime.now() - timedelta(days=365)
    return fake.date_between(start_date=start_date, end_date='today')

# Generate random patients data
def generate_patients(num_patients):
    patients = []
    for _ in range(num_patients):
        patient_id = fake.uuid4()
        name = fake.name()
        age = random.randint(1, 100)
        gender = random.choice(['Male', 'Female'])
        address = fake.address().replace('\n', ', ')
        contact = fake.phone_number()
        patients.append([patient_id, name, age, gender, address, contact])
    return patients

# Generate random doctors data
def generate_doctors(num_doctors):
    doctors = []
    for _ in range(num_doctors):
        doctor_id = fake.uuid4()
        name = fake.name()
        specialization = random.choice(SPECIALIZATIONS)
        contact = fake.phone_number()
        doctors.append([doctor_id, name, specialization, contact])
    return doctors

# Generate random visits data
def generate_visits(num_visits, patients, doctors):
    visits = []
    for _ in range(num_visits):
        visit_id = fake.uuid4()
        patient_id = random.choice(patients)[0]
        doctor_id = random.choice(doctors)[0]
        visit_date = random_date()
        diagnosis = random.choice(DIAGNOSES)
        treatment_cost = round(random.uniform(50, 5000), 2)
        visits.append([visit_id, patient_id, doctor_id, visit_date, diagnosis, treatment_cost])
    return visits

# Save data to CSV file
def save_to_csv(filename, headers, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# Generate and save synthetic healthcare data
def main():
    # Generate synthetic data
    patients = generate_patients(NUM_PATIENTS)
    doctors = generate_doctors(NUM_DOCTORS)
    visits = generate_visits(NUM_VISITS, patients, doctors)

    # Save to CSV
    save_to_csv('patients.csv', ['Patient_ID', 'Name', 'Age', 'Gender', 'Address', 'Contact'], patients)
    save_to_csv('doctors.csv', ['Doctor_ID', 'Name', 'Specialization', 'Contact'], doctors)
    save_to_csv('visits.csv', ['Visit_ID', 'Patient_ID', 'Doctor_ID', 'Visit_Date', 'Diagnosis', 'Treatment_Cost'], visits)

    print("Synthetic healthcare data generated and saved to CSV files.")

if __name__ == "__main__":
    main()

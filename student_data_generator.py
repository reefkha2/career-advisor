import json
import random
from faker import Faker

fake = Faker()

def generate_student():
    majors = ['Computer Science', 'Engineering', 'Business', 'Biology', 'Psychology']
    skills = ['Python', 'Java', 'C++', 'JavaScript', 'Data Analysis', 'Machine Learning', 
              'Project Management', 'Communication', 'Leadership', 'Problem Solving']
    
    return {
        'id': fake.uuid4(),
        'name': fake.name(),
        'email': fake.email(),
        'major': random.choice(majors),
        'year': random.randint(1, 4),
        'gpa': round(random.uniform(2.0, 4.0), 2),
        'skills': random.sample(skills, random.randint(2, 5))
    }

def generate_students(num_students):
    return [generate_student() for _ in range(num_students)]

if __name__ == "__main__":
    num_students = 100  # You can change this number
    students = generate_students(num_students)
    
    # Print the first few students as a sample
    print(json.dumps(students[:5], indent=2))
    
    # Save to a local file
    with open('synthetic_students.json', 'w') as f:
        json.dump(students, f, indent=2)
    
    print(f"{num_students} synthetic student records generated and saved to synthetic_students.json")
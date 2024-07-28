import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import pywraplp

# Fanction to xtract keywrds from the student's input
def extract_keywords(student_input):
    # Tokenize the input
    tokens = word_tokenize(student_input)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [t for t in tokens if t.lower() not in stop_words]
    
    # Return the keywords
    return tokens

# Function to match the student with a mentor from the CSV database
def match_mentor(student_keywords, mentors_csv):
    # Read the mentors CSV file
    with open(mentors_csv, 'r') as f:
        reader = csv.DictReader(f)
        mentors = [row for row in reader]
    
    # Create a dictionary to store the mentor-student pairsr
    pairs = {}
    
    # Iterate over the mentors
    for mentor in mentors:
        # Extract the mentor's keywords
        mentor_keywords = [k for k in mentor['keywords'].split(',')]
        
        # Calculate the similarity between the student's keywords and the mentor's keywords
        similarity = len(set(student_keywords) & set(mentor_keywords))
        
        # Add the mentor-student pair to the dictionary
        pairs[mentor['name']] = similarity
    
    # Create a linear programming model to maximize the matches
    solver = pywraplp.Solver.CreateSolver("GLOP")
    matchV = [solver.IntVar(0, 1, p) for p in pairs.keys()]
    
    # Set the objective to maximize the matches
    objective = solver.Objective()
    for m in matchV:
        objective.SetCoefficient(m, pairs[m.name()])
    objective.SetMaximization()
    
    # Add constraints to ensure each mentor is only assigned to one student
    Mentor_constraints = {d: solver.RowConstraint(0, 1, d) for d in pairs.keys()}
    for m in matchV:
        mentor = m.name()
        Mentor_constraints[mentor].SetCoefficient(m, 1)
    
    # Solve the model
    status = solver.Solve()
    
    # Return the matched mentor
    if status == pywraplp.Solver.OPTIMAL:
        for m in matchV:
            if m.solution_value() > 0.001:
                return m.name()
    else:
        return None

# Main function to run the profile matcher
def profile_matcher():
    # Ask the student about themselves IDK MAN this is the only way 
    student_input = input("Please tell me about yourself: ")
    
    # Extract keywords from the student's input
    student_keywords = extract_keywords(student_input)
    
    # Match the student with a mentor from the CSV database (for now)w
    mentor = match_mentor(student_keywords, 'mentorsLOLweneedafindthisman.csv')
    
    # Print the matched mentor
    if mentor:
        print(f"Your matched mentor is: {mentor}")
    else:
        print("Sorry, no mentor match found.")

# Run the profile matcher :)
profile_matcher()
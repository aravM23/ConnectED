class FinancialAidCalculator:
    def __init__(self):
        self.family_income = 0
        self.family_assets = 0
        self.family_expenses = 0
        self.student_assets = 0
        self.student_expenses = 0
        self.scholarships = 0
        self.grants = 0
        self.loans = 0
        self.work_study = 0
        self.family_size = 0
        self.dependents = 0
        self.other_income = 0
        self.parent_contribution = 0
        self.student_contribution = 0

    def calculate_Expected_Family_Contribution(self):
        # Calculate Expected Family Contribution (EFC) based on family income, assets, expenses, family size, and dependents
        efc = (self.family_income * 0.2) + (self.family_assets * 0.1) - (self.family_expenses * 0.1)
        efc = efc / (self.family_size + 0.5 * self.dependents)
        return efc

    def calculate_Student_Need(self):
        # Calculate student need based on student assets, expenses, scholarships, and other income
        student_need = (self.student_assets * 0.1) + (self.student_expenses * 0.1) - (self.scholarships * 0.1) - (self.other_income * 0.1)
        return student_need

    def calculate_Parent_Contribution(self):
        # Calculate parent contribution based on family income, assets, expenses, and family size
        parent_contribution = (self.family_income * 0.1) + (self.family_assets * 0.05) - (self.family_expenses * 0.05)
        parent_contribution = parent_contribution / (self.family_size + 0.5 * self.dependents)
        return parent_contribution

    def calculate_Student_Contribution(self):
        # Calculate student contribution based on student assets, expenses, scholarships, and other income
        student_contribution = (self.student_assets * 0.05) + (self.student_expenses * 0.05) - (self.scholarships * 0.05) - (self.other_income * 0.05)
        return student_contribution

    def calculate_Financial_Aid(self):
        # Calculate financial aid based on EFC, student need, parent contribution, student contribution, grants, loans, and work-study
        financial_aid = self.calculate_Student_Need() - self.calculate_Expected_Family_Contribution() + self.grants + self.loans + self.work_study
        financial_aid = financial_aid - self.calculate_Parent_Contribution() - self.calculate_Student_Contribution()
        return financial_aid

    def get_user_input(self):
        # Get user input for family income, assets, expenses, student assets, expenses, scholarships, grants, loans, work-study, family size, dependents, and other income
        self.family_income = float(input("Enter family income: $"))
        self.family_assets = float(input("Enter family assets: $"))
        self.family_expenses = float(input("Enter family expenses: $"))
        self.student_assets = float(input("Enter student assets: $"))
        self.student_expenses = float(input("Enter student expenses: $"))
        self.scholarships = float(input("Enter scholarships: $"))
        self.grants = float(input("Enter grants: $"))
        self.loans = float(input("Enter loans: $"))
        self.work_study = float(input("Enter work-study: $"))
        self.family_size = int(input("Enter family size: "))
        self.dependents = int(input("Enter number of dependents: "))
        self.other_income = float(input("Enter other income: $"))

    def display_results(self):
        # Display results, including EFC, student need, parent contribution, student contribution, and financial aid
        print("Expected Family Contribution (EFC): $", round(self.calculate_Expected_Family_Contribution(), 2))
        print("Student Need: $", round(self.calculate_Student_Need(), 2))
        print("Parent Contribution: $", round(self.calculate_Parent_Contribution(), 2))
        print("Student Contribution: $", round(self.calculate_Student_Contribution(), 2))
        print("Financial Aid: $", round(self.calculate_Financial_Aid(), 2))

def main():
    calculator = FinancialAidCalculator()
    calculator.get_user_input()
    calculator.display_results()

if __name__ == "__main__":
    main()
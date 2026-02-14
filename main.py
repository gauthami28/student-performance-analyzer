# Student Performance Analyzer

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # dictionary of subject: marks
        self.total = sum(marks.values())
        self.percentage = self.total / len(marks)
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 80:
            return "A"
        elif self.percentage >= 70:
            return "B"
        elif self.percentage >= 60:
            return "C"
        elif self.percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print(f"\nName: {self.name}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Total: {self.total}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")


def class_analysis(students):
    class_average = sum(s.percentage for s in students) / len(students)
    top_student = max(students, key=lambda s: s.percentage)
    lowest_student = min(students, key=lambda s: s.percentage)

    print("\n--- Class Analysis ---")
    print(f"Class Average: {class_average:.2f}%")
    print(f"Top Performer: {top_student.name} ({top_student.percentage:.2f}%)")
    print(f"Lowest Performer: {lowest_student.name} ({lowest_student.percentage:.2f}%)")


# Example Usage
if __name__ == "__main__":
    students = [
        Student("Alice", {"Math": 85, "Science": 90, "English": 88}),
        Student("Bob", {"Math": 70, "Science": 75, "English": 72}),
        Student("Charlie", {"Math": 95, "Science": 92, "English": 96})
    ]

    print("=== Student Performance Report ===")
    for student in students:
        student.display()

    class_analysis(students)

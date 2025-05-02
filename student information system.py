import datetime
import json

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = {}  # date: status ("Present"/"Absent")

    def mark_attendance(self, date=None, status="Present"):
        if date is None:
            date = datetime.date.today()
        if date in self.attendance:
            print(f"Attendance already marked for {self.name} on {date}.")
        else:
            self.attendance[date] = status
            print(f"{status} marked for {self.name} on {date}.")

    def get_attendance_report(self):
        total_days = len(self.attendance)
        present_days = sum(1 for status in self.attendance.values() if status == "Present")
        percentage = (present_days / total_days) * 100 if total_days else 0

        return {
            "student_id": self.student_id,
            "name": self.name,
            "attendance": {str(k): v for k, v in self.attendance.items()},
            "total_days": total_days,
            "present_days": present_days,
            "attendance_percentage": round(percentage, 2)
        }

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id in self.students:
            print(f"Student ID {student_id} already exists.")
        else:
            self.students[student_id] = Student(student_id, name)
            print(f"Student {name} added successfully.")

    def remove_student(self, student_id):
        if student_id in self.students:
            removed = self.students.pop(student_id)
            print(f"Removed student: {removed.name}")
        else:
            print("Student not found.")

    def edit_student(self, student_id, new_name):
        if student_id in self.students:
            self.students[student_id].name = new_name
            print(f"Student ID {student_id} name updated to {new_name}.")
        else:
            print("Student not found.")

    def mark_attendance(self, student_id, date=None, status="Present"):
        if student_id in self.students:
            self.students[student_id].mark_attendance(date, status)
        else:
            print(f"Student ID {student_id} not found.")

    def generate_report(self):
        report = []
        for student in self.students.values():
            report.append(student.get_attendance_report())
        return report

    def search_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(student.get_attendance_report())
        else:
            print("Student not found.")

    def export_report(self, filename="attendance_report.json"):
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4)
        print(f"Report exported to {filename}")

# Example usage
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.add_student(1, "Alice")
    system.add_student(2, "Bob")

    system.mark_attendance(1)
    system.mark_attendance(2, datetime.date(2023, 10, 1), status="Absent")

    system.edit_student(2, "Bobby")
    system.search_student(2)

    report = system.generate_report()
    for student_report in report:
        print(student_report)

    system.export_report()

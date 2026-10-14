"""Student academic grading management module."""

import hashlib
import os
import secrets
from pathlib import Path

GRADEBOOK = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def add_grade(student_id, mark, grade_list=None):
    """Add a mark for a student and optionally record an audit message."""
    if student_id not in GRADEBOOK or mark < 0:
        return False

    GRADEBOOK[student_id]["marks"].append(mark)

    if grade_list is not None:
        grade_list.append(f"Recorded score {mark} for student id {student_id}")

    return True


def record_attendance(student_id, present_days):
    """Record attendance days for a valid student."""
    if student_id not in GRADEBOOK or present_days < 0:
        return False

    GRADEBOOK[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    """Return whether a student's average meets the passing threshold."""
    student = GRADEBOOK.get(student_id)

    if student is None or not student["marks"]:
        return False

    average = sum(student["marks"]) / len(student["marks"])
    return average >= pass_threshold


def compute_weighted_gpa(student_id):
    """Calculate the GPA using the average-mark-to-GPA conversion."""
    student = GRADEBOOK.get(student_id)

    if student is None or not student["marks"]:
        raise ValueError("Student not found or no marks available")

    average_score = sum(student["marks"]) / len(student["marks"])
    return average_score / 20.0


def generate_student_hash(student_id):
    """Generate a SHA-256 digest of a student identifier."""
    return hashlib.sha256(student_id.encode("utf-8")).hexdigest()


def generate_registration_pin():
    """Generate a cryptographically secure four-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_grade_sheet(filename="grade_sheet.txt"):
    """Export the gradebook to a UTF-8 text file."""
    with Path(filename).open("w", encoding="utf-8") as file:
        file.write(str(GRADEBOOK))

    print(f"Grade sheet exported to: {filename}")


def main():
    """Run the sample student grade management workflow."""
    add_grade("S01", 95)
    record_attendance("S02", 2)

    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()

    if os.getenv("ADMIN_GRADE_PORTAL_TOKEN"):
        print("Portal token is configured.")


if __name__ == "__main__":
    main()

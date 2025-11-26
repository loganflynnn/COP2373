#Logan Flynn
#Grade analysis program
#11/23/2025
import numpy as np

PASSING_GRADE = 60
def load_grades(filename):
   """
   Load grades from the CSV file into a NumPy array.
   Assumes:
       - First row is a header
       - First column is a name/ID
       - Remaining columns are numeric grades
   """

   # Load full file as strings to detect number of columns
   raw = np.genfromtxt(filename, delimiter=",", dtype=str)
   num_cols = raw.shape[1]


   # Load numeric columns only
   grades = np.genfromtxt(
       filename,
       delimiter=",",
       dtype=float,
       skip_header=1,
       usecols=range(1, num_cols)
   )

   return grades

def analyze_grades(grades):
   """
   Perform all required statistical analysis and print results.
   """
   print("First few rows of the dataset:")
   print(grades[:5])
   print()


   # PER-EXAM STATISTICS
   print("Per-exam statistics:\n")


   exam_means = np.mean(grades, axis=0)
   exam_medians = np.median(grades, axis=0)
   exam_stds = np.std(grades, axis=0)
   exam_mins = np.min(grades, axis=0)
   exam_maxs = np.max(grades, axis=0)


   num_exams = grades.shape[1]


   for i in range(num_exams):
       print(f"Exam {i + 1}:")
       print(f"  Mean:   {exam_means[i]:.2f}")
       print(f"  Median: {exam_medians[i]:.2f}")
       print(f"  Std:    {exam_stds[i]:.2f}")
       print(f"  Min:    {exam_mins[i]:.2f}")
       print(f"  Max:    {exam_maxs[i]:.2f}")
       print()


   # OVERALL STATISTICS
   all_grades = grades.flatten()
   print("Overall statistics across all exams:")
   print(f"  Mean:   {np.mean(all_grades):.2f}")
   print(f"  Median: {np.median(all_grades):.2f}")
   print(f"  Std:    {np.std(all_grades):.2f}")
   print(f"  Min:    {np.min(all_grades):.2f}")
   print(f"  Max:    {np.max(all_grades):.2f}")
   print()


   # PASS/FAIL COUNT FOR EACH EXAM
   print(f"Pass/fail per exam (passing = {PASSING_GRADE} or above):\n")
   num_students = grades.shape[0]
   total_passes = 0
   total_grades = num_students * num_exams

   for i in range(num_exams):
       exam = grades[:, i]
       passed = np.sum(exam >= PASSING_GRADE)
       failed = num_students - passed
       total_passes += passed


       print(f"Exam {i + 1}:")
       print(f"  Passed: {passed}")
       print(f"  Failed: {failed}")
       print()


   # OVERALL PASS PERCENTAGE
   overall_pass_percent = (total_passes / total_grades) * 100
   print("Overall pass percentage across all exams:")
   print(f"  {overall_pass_percent:.2f}%")
   print()


# MAIN PROGRAM
if __name__ == "__main__":
   filename = "grades.csv"
   grades_array = load_grades(filename)
   analyze_grades(grades_array)

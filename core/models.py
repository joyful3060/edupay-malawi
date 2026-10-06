from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade_level = models.CharField(max_length=20)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"

class FeeStructure(models.Model):
    grade_level = models.CharField(max_length=20)
    term = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=10)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.grade_level} - {self.term} ({self.academic_year})"

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_paid = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=[("cash", "Cash"), ("bank", "Bank Transfer"), ("mobile", "Mobile Money")], default="cash")
    receipt_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.student} - {self.amount_paid} on {self.date_paid}"
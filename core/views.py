from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Student, FeeStructure
from .forms import PaymentForm

def student_list(request):
    students = Student.objects.all()
    data = []
    for student in students:
        total_paid = student.payments.aggregate(total=Sum('amount_paid'))['total'] or 0
        total_due = FeeStructure.objects.filter(grade_level=student.grade_level).aggregate(
            total=Sum('amount_due')
        )['total'] or 0
        balance = total_due - total_paid
        data.append({
            'student': student,
            'total_paid': total_paid,
            'total_due': total_due,
            'balance': balance,
        })
    return render(request, 'core/student_list.html', {'data': data})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = PaymentForm()
    return render(request, 'core/add_payment.html', {'form': form})
'''
1) write a program to compute the payment for a freelancer.
The program asks the user to enter hours and rate.
The payment will be 1.5 times the hourly rate for
hours worked above 40 hours. Write a function called
computepay to compute the payment.

2) rewrite the program using try and except so that your
program handles non-numeric input.
'''


def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
        return pay
    else:  # hours > 40:
        extra_hours = hours - 40
        extra_rate = rate * 1.5
        pay = 40 * rate + extra_hours * extra_rate
        return pay


try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print('payment: ', computepay(hours, rate))
except:
    print("Please, enter numeric input !")

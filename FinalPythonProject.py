
Header = ('Name','Hours Worked','Rate','Regular Pay','Overtime Pay','Gross Pay','Fed_Tax','State Tax','Fica','Net_pay')

print(" Payroll Calculator")
emp_list = 0
while emp_list < 11 :
#Calculate gross income with and without overtime.#
    name = input("Please enter employee's name:")
    hours = int(input("What is their hourly wage?"))
    rate = int(input("How many hours did they work for the week?"))
    if hours <= 40 :
        regular_pay = rate * hours
        ot_pay= 0
        gross_pay = regular_pay + ot_pay
    elif  hours > 40 :
        regular_pay = rate * 40
        ot_pay = (hours - 40)* 1.5
        gross_pay = regular_pay + ot_pay
        print (gross_pay,regular_pay,ot_pay)
# Calculate Taxes and Deductions
    fed_tax = round(gross_pay * 10)/100
    state_tax = round(gross_pay * 6)/100
    fica = round (gross_pay * 3)/100
    deductions = fed_tax + state_tax + fica
    net_pay = gross_pay - deductions
    print (name, hours ,rate, regular_pay, ot_pay,gross_pay,fed_tax,state_tax,fica, net_pay)








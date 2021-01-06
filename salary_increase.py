#Salary increase based on the salary range.

print('\033[0;30;43m SALARY INCREASE \033[m')
print(' ')

#Establish the percentage of each salary range.
min_s_increase = 15
med_s_increase = 10
max_s_increase = 5

salary = float(input('Insert the salary of employee € '))

#For Minimum Salary.
if salary <= 1480:
    salary_min_new = ((salary / 100) * min_s_increase) + salary
    print('The new salary is \033[0;30;43m € {:.2f} \033[m ({}% increased).'.format(salary_min_new, min_s_increase))
else:
#For Medium Salary.
    if salary <=2000:
        salary_med_new = ((salary / 100) * med_s_increase) + salary
        print('The new salary is \033[0;30;43m € {:.2f} \033[m ({}% increased).'.format(salary_med_new, med_s_increase))
    else:
#For Maximum Salary.
        if salary > 2000:
            salary_max_new = ((salary / 100) * max_s_increase) + salary
            print('The new salary is \033[0;30;43m € {:.2f} \033[m ({}% increased).'.format(salary_max_new, max_s_increase))
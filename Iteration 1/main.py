#!/usr/bin/env python
# Created by James Upton


from random import gauss, randint
from keith import Process
from Employee import Employee, SalaryEmployee, BookEmployee
import time
import Queue
import Manager

Process.chgProcessName('simulate') # sets the process name


def biased_random(minimum, mean, maximum, stdev): # returns a float based on a gaussian
                                                  # distribution around an average
                                                  # between a min and max
    value = gauss(mean, stdev)
    if minimum < value < maximum:
        return value
    else: value = gauss(mean, stdev)
    return value

def phone_time(): # generates inbound telephone call time stamps
    import phonecall
    return phonecall.gen_call_time()

def main():
    employees = list()
    employees.append(SalaryEmployee("Clay", [1, 2, 3, 4], 23.14))
    employees.append(SalaryEmployee("Karen", [1, 2, 3, 4], 15.43))
    employees.append(Employee("Mary", [1, 2, 3, 4], 9))
    employees.append(BookEmployee("Joe", [5, 8], 18.5, eff_rate=1.1, error_rate=4))
    employees.append(BookEmployee("Scott", [5, 8], 18.5, eff_rate=2.1, error_rate=3))
    employees.append(BookEmployee("Eddie", [5, 8], 18.5, eff_rate=1.5, error_rate=2))
    employees.append(Employee("Brandi", [6], 12))
    employees.append(BookEmployee("Ronnie", [7, 9], 18.5, eff_rate=0.4))
    employees.append(Employee("Porter", [10], 8))
    manager = Manager.Manager(employees)

    manager.dtime = 10000
    manager.debug = False
    run_time = 720   #720 makes a year

    stime = time.time() # time stamp for begining 
    start_time = time.time() # time the program started
    end_time = start_time +  run_time 
    call = time.time() + (phone_time()/manager.dtime)
    try:
        while time.time() < end_time:
            if time.time() >= call: # ring phone at times
                stime += call # 
                manager.ringPhone()
                call = time.time() + (phone_time()/manager.dtime)
            else:
                manager.check()

    except(KeyboardInterrupt):
        pass
    except:
        # Check new errors here
        print("Exception!!")
        raise
    finally:
        manager.close()
        print(manager.Queues)
        hours = round((float((time.time() - start_time) * manager.dtime) / 3600), 2)
        summary = """Hours Open = {hours}
Total Calls = {calls}
Total Estimates = {estimates}
Total Repair Orders = {orders}
Total Completed Orders = {completed}
Estimate Per Calls = {estimates_per_calls}%
Repair per Estimates = {ro_per_estimates}%
""".format(hours=hours,
           calls=manager.totalPhoneCalls,
           estimates=manager.totalEstimates,
           orders=manager.totalRepairOrders,
           completed=manager.totalCompletedRepairOrders,
           estimates_per_calls = round(float(manager.totalEstimates) / float(manager.totalPhoneCalls) * 100, 2),
           ro_per_estimates = round(float(manager.totalRepairOrders) / float(manager.totalEstimates) * 100, 2),
           )
        employee_summary = "\nEmployee\tWorking\tIdle\tCost\n"
        employee_cost = 0
        total_idle = []
        for employee in sorted(manager.employees, key=lambda x: x.name):
            worked = round(float(employee.worked * manager.dtime) / 3600, 2)
            idle = round(float((hours - worked) / hours * 100), 2)
            total_idle.append(idle)
            cost = employee.calculateCost(hours)
            employee_cost += cost
            employee_summary += """{name}\t\t{worked}\t{idle}\t${cost}\n""".format(name=employee.name, worked=worked, idle=idle, cost=cost)
        with open("it1out.txt", 'a') as f:
            f.write('\n\n')
            f.write(summary)
            f.write(employee_summary)
            f.write('\tAverage idle time: {}%\n'.format(round(sum(total_idle)/len(total_idle), 2)))
            f.write("\tTotal Cost of Employees: ${}\n".format(employee_cost))
            job_cost = manager.totalCompletedRepairOrders * 2346.54
            f.write("\tGross Profit : ${}\n".format(job_cost))
            f.write("\tActual Profit : ${}\n".format(job_cost - employee_cost))

if __name__ == '__main__':
    with open('it1out.txt', 'w') as f:
        f.write("")
    for _ in xrange(10):
        main()
    

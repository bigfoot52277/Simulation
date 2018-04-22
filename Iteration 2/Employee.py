import threading
import time


class Employee(object):
    def __init__(self, name, job_types, pay_rate, error_rate=0):
        self.name = name
        self.job_types = job_types
        self.pay_rate = pay_rate
        self.error_rate = error_rate
        self.manager = None

        self.started_working = 0
        self.working = False
        self.worked = 0

    def calculateCost(self, hours_open):
        # Calculate regular Employee Cost
        pay = hours_open * self.pay_rate
        return round(pay, 2)
      
    def startJob(self):
        self.started_working = time.time()
        self.working = True

    def finishJob(self):
        self.working = False
        self.worked += time.time() - self.started_working

    def finishPhoneCall(self):
        self.finishJob()
        if self.manager.totalPhoneCalls % 8 == 0:
            self.manager.makeEstimate()
            
    def finishEstimate(self):
        self.finishJob()
        if not self.manager.totalEstimates % 8 == 0:
            self.manager.partsOrder()

    def finishPartsOrder(self):
        self.finishJob()
        import partsorder
        job_time = partsorder.order() / self.manager.dtime
        t = threading.Timer(job_time, self.manager.doBodyWork)
        t.start()
        self.manager.timers.append(t)

    def finishBodyWork(self):
        self.finishJob()
        self.manager.doInspectWork()
            
    def finishInspection(self):
        # tear down estimates eliminate repeat parts orders
        self.finishJob()
        if self.manager.totalRepairOrders % 8 == 0: # inspections force tech to do better quality work
            self.manager.doBodyWork(repeat=True)
        else:
            self.manager.doPrepWork()

    def finishPrepWork(self):
        self.finishJob()
        self.manager.doPaintWork()

    def finishPaintWork(self):
        self.finishJob()
        self.manager.doAssemblyWork()

    def finishAssemblyWork(self):
        self.finishJob()
        self.manager.doBuffWork()

    def finishBuffingWork(self):
        self.finishJob()
        self.manager.doCleanUpWork()

    def finishCleanUpWork(self):
        self.finishJob()
        self.manager.doDeliveryWork()

    def finishDeliveryWork(self):
        self.finishJob()
        self.manager.totalCompletedRepairOrders += 1

    def work(self, job_type):
        if job_type == 1: # phone call
            import phonecall
            if self.manager.debug:
                print('{} Answering phone'.format(self.name))
            self.manager.totalPhoneCalls += 1
            job_time = phonecall.gen_call_length() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishPhoneCall)
            t.start()
            self.manager.timers.append(t)

        elif job_type == 2: # estimate
            import estimate
            if self.manager.debug:
                print('{} Writing Estimate'.format(self.name))
            job_time = estimate.tdestimate() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishEstimate)
            t.start()
            self.manager.timers.append(t)
            
        elif job_type == 3: # parts
            import partsorder
            if self.manager.debug:
                print('{} Ordering Parts'.format(self.name))
            job_time = partsorder.process_parts() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishPartsOrder)
            t.start()
            self.manager.timers.append(t)
            
        elif job_type == 4: # delivery
            import delivery
            if self.manager.debug:
                print('{} Delivering car'.format(self.name))
            if not self.manager.totalRepairOrders % 3 == 0:
                job_time = delivery.deliver() / self.manager.dtime
            else:
                job_time = delivery.deliver(cash=True) / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishDeliveryWork)
            t.start()
            self.manager.timers.append(t)
            
        elif job_type == 5: # bodywork (tech)
            import bodywork
            if self.manager.debug:
                print('{} Repairing car'.format(self.name))
            job_time = (bodywork.repair() / self.manager.dtime) * self.eff_rate
            self.startJob()
            t = threading.Timer(job_time, self.finishBodyWork)
            t.start()
            self.manager.timers.append(t)

        elif job_type == 6: # prep
            import prep
            if self.manager.debug:
                print('Prepping car')
            if self.manager.totalRepairOrders % 2 == 0:
                job_time = prep.prepare(Primer=True) / self.manager.dtime
            else:
                job_time = prep.prepare() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishPrepWork)
            t.start()
            self.manager.timers.append(t)

        elif job_type == 7: # paint
            import paint
            if self.manager.debug:
                print('Painting car')
            job_time = paint.spray() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishPaintWork)
            t.start()
            self.manager.timers.append(t)

        elif job_type == 8: # assembly
            import assemble
            if self.manager.debug:
                print('{} Assembling car'.format(self.name))
            job_time = assemble.Assemble() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishAssemblyWork)
            t.start()
            self.manager.timers.append(t)
            
        elif job_type == 9: # Buff
            import buffing
            if self.manager.debug:
                print('Buffing car')
            job_time = buffing.buff() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishBuffingWork)
            t.start()
            self.manager.timers.append(t)

        elif job_type == 10: # cleanup
            import cleanup
            if self.manager.debug:
                print('Cleaning Car')
            job_time = cleanup.port() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishCleanUpWork)
            t.start()
            self.manager.timers.append(t)

        elif job_type == 11: # inspection
            import qa                     
            if self.manager.debug:
                print('Inspecting Bodywork')
            job_time = qa.check() / self.manager.dtime
            self.startJob()
            t = threading.Timer(job_time, self.finishInspection)
            t.start()
            self.manager.timers.append(t)

class SalaryEmployee(Employee):
    def __init__(self, name, job_types, pay_rate, error_rate=0):
        super(SalaryEmployee, self).__init__(name, job_types, pay_rate, error_rate)

    def calculateCost(self, hours_open):
        # Calculate regular Employee Cost
        pay = float(self.pay_rate * hours_open)
        #calculate bonues based on profits
        return round(pay, 2)
    
class BookEmployee(Employee):
    def __init__(self, name, job_types, pay_rate, eff_rate=1, error_rate=0):
        super(BookEmployee, self).__init__(name, job_types, pay_rate, error_rate)
        self.eff_rate = eff_rate
        
    def calculateCost(self, hours_open):
        # Calculate regular Employee Cost
        time_in = (float(self.worked * self.manager.dtime) / self.eff_rate) / 3600
        pay = time_in * self.pay_rate
        return round(pay, 2)

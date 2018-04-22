import threading
from random import shuffle


class Manager(object):
    def __init__(self, employees):
        self.employees = employees
        for employee in self.employees:
            employee.manager = self

        self.officeQueue = list()
        self.techQueue = list()
        self.inspectionQueue = list()
        self.prepQueue = list()
        self.paintQueue = list()
        self.porterQueue = list()

        self.Queues = [self.officeQueue, self.techQueue, self.inspectionQueue, self.prepQueue, self.paintQueue, self.porterQueue]
        self.timers = list()
        self.dtime = None
        self.debug = False
        self.call_drop = 0

        self.totalPhoneCalls = 0
        self.totalEstimates = 0
        self.totalRepairOrders = 0
        self.totalCompletedRepairOrders = 0

    def check(self):
        shuffle(self.employees)
        for Q in self.Queues:
            if not len(Q):
                continue
            job_type = Q[0]
            for employee in self.employees:
                if job_type in employee.job_types and not employee.working:
                    del Q[0]
                    employee.work(job_type)
                    break
                elif job_type == 1:
                    self.call_drop += 1
                    del Q[0]
                    break

    def close(self):
        for timer in self.timers:
            timer.cancel()

    def ringPhone(self):
        job_type = 1
        self.officeQueue.append(job_type)

    def makeEstimate(self):
        job_type = 2
        self.totalEstimates += 1
        self.inspectionQueue.append(job_type)

    def partsOrder(self):
        job_type = 3
        self.officeQueue.append(job_type)

    def doDeliveryWork(self):
        job_type = 4
        self.officeQueue.insert(0, job_type)

    def doBodyWork(self, repeat=False):
        job_type = 5
        if not repeat:
            self.totalRepairOrders +=1
            self.techQueue.append(job_type)
        else:
            self.techQueue.insert(0, job_type)

    def doInspectWork(self):
        job_type = 11
        self.inspectionQueue.append(job_type)

    def doPrepWork(self):
        job_type = 6
        self.prepQueue.append(job_type)

    def doPaintWork(self):
        job_type = 7
        self.paintQueue.append(job_type)

    def doAssemblyWork(self):
        job_type = 8
        self.techQueue.insert(0, job_type)

    def doBuffWork(self):
        job_type = 9
        self.porterQueue.append(job_type)

    def doCleanUpWork(self):
        job_type = 10
        self.porterQueue.append(job_type)

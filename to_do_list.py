class Task():
    def __init__(self,name,date):
        self.name=name
        self.date=date
        self.is_done=False
    


class TaskManagement():
    def __init__(self):
       self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)


    def check_done_status(self,done):
        self.done=done
        for task in self.tasks:
            print(f"{task.name} , {task.date}" )
         
                











t=Task("python","today")    

manag=TaskManagement()  
manag.add_task(t)
manag.check_done_status()



    


from threading import Thread, current_thread, Lock


# Function Based Thread
"""
def DisplayName(name, no_to_print):
    # print("Display Name "+ name + " Default Thread Name "+ current_thread().name)
    current_thread().setName(" Running Child Thread")
    for a in range(1, no_to_print):
        print("Display Name "+ name + " " + str(a) + " Default Thread Name "+ current_thread().name)

t = Thread(target=DisplayName, args=("Ram",4))
t.start()

t1 = Thread(target=DisplayName, args=("Avtar",6))
t1.start()

for i in range(1,10):
    # print("Run Main Thread Value "+ str(i) + " Default Thread Name "+ current_thread().name)
    current_thread().setName(" RunningFirstThread")
    print("Run Main Thread Value "+ str(i) + " New Thread Name "+ current_thread().name)

"""



class AirTicket():
    def __init__(self, availbaleSheat):
        self.AvailbaleSheat = availbaleSheat
        self.l = Lock()
        
    def BookSheet(self, nameofPerson, needSheet):
        self.l.acquire()
        print(current_thread().name + " Availble Seat " + str(self.AvailbaleSheat))
        if needSheet <= self.AvailbaleSheat:
             print(current_thread().name + " Seat Booked {0} for {1} ".format(
                 str(needSheet) , nameofPerson 
             ))
             self.AvailbaleSheat -= 1
        else:
            print(current_thread().name + " Seat Not Availble")

        self.l.release()

obj = AirTicket(2)
t1 = Thread(target=obj.BookSheet, args= ("Ram", 1), name="thrdRam")
t2 = Thread(target=obj.BookSheet, args= ("Avtar", 1), name="thrdAvtar")
t3 = Thread(target=obj.BookSheet, args= ("Shivam", 1), name="thrdShivam")
t1.start()
t2.start()
t3.start()
        
for i in range(1,10):
    current_thread().setName(" RunningFirstThread")
    print("Run Main Thread Value "+ str(i) + " New Thread Name "+ current_thread().name)        

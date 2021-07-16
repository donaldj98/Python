# Breaking a big task into multiple tasks (simliar to multitasking )

from time import sleep      # to get sleep timer
from threading import *     # importing threading function

class Hello(Thread):        # passing thread as sub class to the main class Hello - splits into multiple threads
  def run(self):
    for i in range(10):
      print("Hello")
      sleep(1)

class Hi(Thread):
  def run(self):
    for i in range(10):     
      print("Hi")
      sleep(1)
      
t1=Hello()
t2=Hi()

t1.run()          
t2.run()

# instead of the above run method we should use the start method to work it's a prebuild function

t1.start()        # this method will only work on run method it indirectly call run method 
sleep(0.2)        # sleep will help in giving a time interval for both the threads
t2.start()

t1.join()     # wait till t1 join # So that the main thread will wait till the t1 completes
t2.join()     # wait till t2 join

print("Bye")        # main thread 

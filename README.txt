This is a zoomeye SDK to make you use zoomeye easily.

You can install using pip like this:
pip install zoomeye

You can use it to search some hosts like this:
from zoomeye import zoomeye

z = zoomeye.Zoomeye("your email", "your password")
z.search("port:23")
while not z.queue.empty():
    print z.queue.get()['ip']

You can use search_type parameter to search hosts or websites, the default is host: 
z.search("port:80", search_type = "web")
while not z.queue.empty():
    print z.queue.get()['site']

You can use facets parameter to decide what do you want to return:
z.search("port:23", facets = "os,device,service")
while not z.queue.empty():
    result = z.queue.get()
    print result['ip']
    print result['os']
    print result['device']
    print result['service']

You can use pages parameter to decide how many pages do you want to return, the default is 10:
z.search("port:23", pages = 20)
while not z.queue.empty():
    print z.queue.get()['ip']

You can use port parameter to decide whether the port is bind with ip while searching for hosts, the default is False:
z.search("port:23", pages = 20, port = True)
while not z.queue.empty():
    print z.queue.get()['ip']  # this will return xxx.xxx.xxx.xxx:23

You can use run function to run your functions with the returned data, it's usage is same with search function:
def testFun(zoo):      # need to accept a parameter of Zoomeye type
    while zoo.isReady():    # using isReady function to make sure zoomeye is running
        if not zoo.queue.empty():     # to make sure there are datas in queue
            print "hello: %s" % zoo.queue.get()['ip']

z = zoomeye.Zoomeye("your email", "your password")
z.run(testFun, "port:80")

You can use accountInfo function to get some infomation about your account:
info = z.accountInfo()
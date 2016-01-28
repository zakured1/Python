#!/usr/bin/python
import os
print 'Process %s is running..' % os.getpid()
p=os.fork()
print p
if p==0:
	print 'I\'m a child process ,my pid:%s    my father\'s pid:%s' %(os.getpid(),os.getppid())
else:
	print 'I\'m a father process,my pid:%s    my child\'s pid:%s' %(os.getpid(),p)



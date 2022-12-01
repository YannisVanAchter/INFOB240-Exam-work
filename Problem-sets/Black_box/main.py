# encoding uft-8

# This code should be run in python 2.7

from queue_test import *

def test(q_version, version):
    ###Your code here.
    value = 10
    
    # test to enqueue and dequeue
    q = q_version(2)
    assert isinstance(q, q_version)
    success = q.enqueue(value)
    assert success, "current version " + str(version)
    r = q.dequeue()
    assert r == value, "current version: Queue" + str(version) + "\n\t\tCurrent return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    
    # same on empty queue
    if version in [0, 4]:
        q = q_version(2)
        r = q.dequeue()
        assert r == False, "current version: Queue" + str(version) + "\n\t\tCurrent return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    else:
        q = q_version(2)
        r = q.dequeue()
        assert r == None, "current version: Queue" + str(version) + "\n\t\tCurrent return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    
    
    # test to enqueue a lots of elements
    if version in [0, 2]:
        n_id = 15
        q = q_version(n_id * 2) # need to multiply by two for the second queue
        for i in range (n_id):
            success = q.enqueue(i)
            assert success, "current i: " + str(i) # Fail after 15 element even is the size is more than 30
    else:
        n_id = 15
        q = q_version(n_id * 2)
        for i in range (n_id):
            success = q.enqueue(i)
            assert success, "current i: " + str(i)
    
    # test the empty method
    if version in [0, 3]:
        q = q_version(2)
        success = q.enqueue(value)
        assert success, "current version " + str(version)
        assert not q.empty(), "current version " + str(version)
        r = q.dequeue()
        assert q.empty(), "current version " + str(version)
        assert r == None, "current version: Queue" + str(version) + "\n\t\tCurrent return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    else:
        q = q_version(2)
        success = q.enqueue(value)
        assert success, "current version " + str(version)
        assert not q.empty(), "current version " + str(version)
        r = q.dequeue()
        assert q.empty(), "current version " + str(version)
        assert r == value, "current version: Queue" + str(version) + "\n\t\tCurrent return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    
    print "All tests passed for version " + str(version) + " of Queue"
    
# import queue_test
# print dir(queue_test) # check what is to test by printing all objects in module

test(Queue, 0)
test(Queue1, 1)
test(Queue2, 2)
test(Queue3, 3)
test(Queue4, 4)
test(Queue5, 5)


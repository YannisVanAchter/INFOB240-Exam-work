# encoding uft-8

# This code should be run in python 2.7

from queue_test import Queue

def test():
    ###Your code here.
    value = 10
    
    # test to enqueue and dequeue
    q = Queue(2)
    assert isinstance(q, Queue)
    success = q.enqueue(value)
    assert success, "Enqueued failled, value=%s" % value
    r = q.dequeue()
    assert r == value, "Current return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    
    # dequeue on empty queue
    q = Queue(2)
    r = q.dequeue()
    assert r == False, "Current return " + str(r) + "\n\t\tCurrent attent: " + str(value)
    
    # test to enqueue a lots of elements
    n_id = 15
    q = Queue(n_id * 2) # need to multiply by two for the second queue
    for i in range (n_id):
        success = q.enqueue(i)
        assert success, "current i: " + str(i) # Fail after 15 element even is the size is more than 30
        # second enqueue
        success = q.enqueue(i)
        assert success, "current i': " + str(i) # Fail after 15 element even is the size is more than 30
    
    # test the empty method
    q = Queue(2)
    success = q.enqueue(value)
    assert success, "Enqueued failled, value=%s" % value
    assert not q.empty(), "Test queue is not empty failed"
    r = q.dequeue()
    assert q.empty(), "Test queue is empty failed"
    assert r == value, "Current return " + str(r) + "\n\t\tCurrent attent: " + str(value) # return None
    
    print "All tests passed for Queue"
    
if __name__ == "__main__":
    test()

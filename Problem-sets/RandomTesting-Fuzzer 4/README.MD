# Problem set 4

Create an fuzzer to test an application on your personal desktop

``` python
for test_id in range(nb_tests):
    file = random.choice(file_list)
    # generate list of each bytes composing the file
    f = open(file, "rb")
    buffer_ = bytearray(f.read())
    f.close()
    
    nb_writtings = random.randrange(math.ceil((float(len(buffer_)) / factor ))) + 1
    
    # charlie miller's algorithm
    for _ in range(nb_writtings):
        rbyte = random.randrange(256) # select an random value for 1 byte
        byte_id = random.choice(buffer_) # select a random place where put the rbyte choosed
        buffer_[byte_id] = rbyte
        
    open(fuzz_output, "wb").write(buffer_)
    
    process = subprocess.Popen([app, fuzz_output])
    
    time.sleep(0.1)
    
    crash = process.poll()
    
    if not crash:
        process.terminate()
```
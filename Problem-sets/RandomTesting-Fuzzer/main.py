#  encoding uft-8

import math
import random
import subprocess
import time
import os.path as pt

from cs50 import get_int

def fuzzer(app: str, nb_tests: int, fuzz_output: str, file_list: list, factor: int):
    for file_id, file in enumerate(file_list):
        for test_id in range(nb_tests):
            print((file_id + test_id), "on", nb_tests * len(file_list), "this means we are at", ((test_id + file_id) /(nb_tests* len(file_list))) * 100, "%")
            # generate list of each bytes composing the file
            f = open(file, "rb")
            buffer_ = bytearray(f.read())
            f.close()
            
            nb_writtings = random.randrange(math.ceil((float(len(buffer_)) / factor ))) + 1
            
            for _ in range(nb_writtings):
                rbyte = random.randrange(256)
                byte_id = random.choice(buffer_)
                buffer_[byte_id] = rbyte
                
            with open(fuzz_output, "wb") as f:
                f.write(buffer_)
            
                process = subprocess.Popen([app, fuzz_output])
                
                time.sleep(0.001)
                
                crash = process.poll()
                
                if not crash:
                    process.terminate()
                else:
                    yield buffer_, file, test_id
  
def get_argv():
    from sys import argv 
    def get_file_list(start: int):
        if argv.__len__() == start + 1 and argv[start].startswith("-"):
            f = open(argv[start][1:], "r")
            arguments_ = f.readlines()
            f.close()
        else:
            arguments_ = argv[start:]
        file_list = []
        for file_path in arguments_:
            if pt.isfile(file_path):
                file_list.append(file_path)
        
        if len(file_list) == 0:
            exit("You did not enter any file for tests")
        return file_list
            
    if len(argv) == 1:
        exit("You did not enter an factor or an list of file for tests")
    
    try:
        factor = int(argv[1])
        file_list = get_file_list(2)
    except ValueError:
        factor = get_int("Enter the factor you want for fuzzing: ")
        file_list = get_file_list(1)
        
    return factor, file_list

def main(): 
    apps = ["C:\\Users\\yanni\\OneDrive\\Bureau\\ALL\\Tor Browser\\Browser\\firefox.exe"]
    # ["C:\\Users\\yanni\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\DB-Main 11.0.2\\DB-Main 11.0.2.lnk"]
    factor, file_list_name = 250, [
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\istockphoto-451623157-612x612.jpg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\istockphoto-451623157-612x612_meme.jpg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\\MOOC\\image_présentation\\main-qimg-ad7927067e4500cd9301160b11095dc0-lq.jpeg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\maxresdefault.jpg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\Software-tester-—-kopia.jpeg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\software-testing.jpg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\testing_meme3.png",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\Two_red_dice_01.svg.png",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\whitebox_example.png",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\blackbox_example.png",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\Dragons_Battles_Knight_446264.jpg",
        "C:\\Users\\yanni\\OneDrive\\Documents\\unif\\Bac 2\\Q1\\MOOC\\image_présentation\\Dragons_Battles_Knight_446264_meme.jpg"
    ]
    with open("fuzzer_repporting.txt", "w+") as file:
        for app in apps:
            nb_tests = random.randint(10000, 100000)
            for crasher_data, file_name, test_id_crash in fuzzer(app, nb_tests, "temp.fuzzer.out.subprocessData.txt", file_list_name, factor):
                to_insert = f"""\n
                On test of {app}:\n
                \tWith file: {file_name}\n
                \tOn test id: {test_id_crash}, for a total test at this exécution of {nb_tests}\n
                \tUpdate as those bytes: {crasher_data}\n
                """ + ("=" * 200) + "\n"
                file.write(to_insert)


if __name__ == "__main__":
    main()


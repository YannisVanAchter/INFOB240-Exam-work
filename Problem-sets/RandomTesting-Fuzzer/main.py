#  encoding uft-8

import math
import random
import subprocess
import time
import os.path as pt

from cs50 import get_int

def fuzzer(app: str, nb_tests: int, fuzz_output: str, file_list: list, factor: int):
    for test_id in range(nb_tests):
        file = random.choice(file_list)
        print((test_id), "on", nb_tests , "this means we are at", (test_id /nb_tests) * 100, "%")
        # generate list of each bytes composing the file
        f = open(file, "rb")
        buffer_ = bytearray(f.read())
        f.close()
        
        nb_writtings = random.randrange(math.ceil((float(len(buffer_)) / factor ))) + 1
        
        for _ in range(nb_writtings):
            rbyte = random.randrange(256)
            byte_id = random.choice(buffer_)
            buffer_[byte_id] = rbyte
            
        open(fuzz_output, "wb").write(buffer_)
            
        process = subprocess.Popen([app, fuzz_output])
        # process = subprocess.Popen([app, buffer_])
        # process = subprocess.Popen(buffer_, len(buffer_), app)
        
        time.sleep(0.001)
        
        crash = process.poll()
        
        if not crash:
            process.terminate()
        else:
            yield buffer_, file, test_id


def main(): 
    apps = [
            "C:\\Program Files\\paint.net\\paintdotnet.exe",
            "C:\\Program Files\\GIMP 2\\bin\\gimp-2.10.exe",
            "C:\\Users\\yanni\\OneDrive\\Bureau\\ALL\\Tor Browser\\Browser\\firefox.exe",
            ]
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
    nb_tests = random.randint(1000, 10000)
    with open("fuzzer_repporting.txt", "w+") as file:
        for app in apps:
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


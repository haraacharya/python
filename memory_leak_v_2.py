import subprocess
import os
from subprocess import Popen
import re

def main():
    print (wait_for_process("cat /proc/slabinfo > slabinfo.txt", "radix_tree_node"))	
    os.remove("slabinfo.txt")

#Use this function If you want to Wait for a command to get executed and also expect a pass fail result from it
def wait_for_process(command, search_text):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # output = ();
    output = p.stdout.read()
    find_text = False
    retval = p.wait()

    if retval==0:
        i = 0
        with open('slabinfo.txt', 'r') as f:
            for line in f:
                if re.search(search_text, line.lower()):
                    #print (line)
                    mem_leak_string = line
                    mem_leak_list = mem_leak_string.split()     
                    #print (mem_leak_list)
                    find_text = True
                    return(mem_leak_list[1])

        if find_text == False:        
            print ("Memory leak object not found, PASS")
            return(0)
    else:
        return(False)

if __name__ == "__main__":main()

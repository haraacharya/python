import subprocess
from subprocess import Popen
import re

def main():
    #wait_for_process("cat /proc/slabinfo", "posix_timers_cache")	
    wait_for_process("cat /proc/slabinfo", False)		

#Use this function If you want to Wait for a command to get executed and also expect a pass fail result from it
def wait_for_process(command, search_text):
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # output = ();
    output = p.stdout.read()
    #lineOutput = str( output, encoding='utf8' )
    lineOutput = str(output)
    #print (lineOutput)
    for line in output:
        print (line)
        #output = output + tuple(line)
	
    retval = p.wait()
    if retval == 0:
        if search_text:
        #if search_text in lineOutput.lower():
            #print ( lineOutput.lower())
            if re.search(search_text, lineOutput.lower()):
                print ("%s TEST PASSED." % command)
                return (True, "MESG: %s TEST PASSED." % command)
            else:
                result = command + " :Test FAILED"
                print (result)
                return (False, "Couldn't find: %s"% search_text)
        else:
            result = command + ":command executed successfully"			
            print (result)
            return (True, result)
    else:
        result = "ERROR: The Command " + command + " was not executed successfully"
        print (result)
        return (False, result)
    


if __name__ == "__main__":main()

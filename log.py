__logFile = "/tmp/nostratv_app.log"

def __writeToFile(message):
    with open(__logFile, "a") as myfile:
        myfile.writelines(message + '\n')

def e(message):
    __writeToFile("[ERROR]: " + str(message) )

def w(message):
    __writeToFile("[WARNING]: " + str(message) )

def i(message):
    __writeToFile("[INFO]: " + str(message) )

def d(message):
    __writeToFile("[DEBUG]: " + str(message) )
import tkinter.filedialog
import tkinter.messagebox
import cryptography.fernet
import websockets.sync.server as webse
import websockets, cryptography, logging, datetime, os, yaml, subprocess, tkinter

# cryptography.fernet.Fernet.generate_key()

try:
    os.mkdir("logs")
except:
    pass
try:
    f = open("config.yml", "x")
    f.write(
        f"""#Simple File Transfer config
#@mas6y6 (on github) - 2024

#Config Verison
configversion: "v1"

#Whether to server should be enabled
enabled: true

config:
    #Transfer Location
    logslocation: {os.path.join(os.getcwd(),"logs")}

    #Request the user to accept the SFT request
    autoaccept: false
    
    #The port where the SFT server is hosted
    port: 9302

    #The server where the SFT server is hosted
    host: localhost
    
transferlocation:
    #Ask user where transfered files go
    autolocate: true

    #Location where all files that have been trasfered go
    location: {os.path.join(os.getcwd(),"box")}
"""
    )
    f.close()
except:
    pass
config = yaml.safe_load(open("config.yml"))

if not config["enabled"]:
    exit()

try:
    if not os.path.exists(config["config"]["loglocation"]):
        os.mkdir(config["config"]["loglocation"])
    else:
        pass
except:
    pass

if config["transferlocation"]["autolocate"]:
    try:
        if not os.path.exists(config["transferlocation"]["location"]):
            os.mkdir(config["transferlocation"]["location"])
        else:
            pass
    except:
        pass

logdate = datetime.datetime.now()

logfile = os.path.join(
    config["config"]["logslocation"],
    str(logdate.day)
    + "-"
    + str(logdate.month)
    + "-"
    + str(logdate.year)
    + " "
    + str(logdate.hour)
    + "."
    + str(logdate.minute)
    + "."
    + str(logdate.second)
    + ".log"
)
logging.basicConfig(level=logging.INFO, filename=logfile)
serverlogger = logging.getLogger("Simple File Trasfer")

def handle(websockets: websockets.server.WebSocketServerProtocol):
    def send(data: str):
        websockets.send(crpt.encrypt(data.encode()))

    def recv():
        return crpt.decrypt(websockets.recv()).decode()

    # Accept the decrypion key
    crpt = cryptography.fernet.Fernet(websockets.recv())
    send("accepted")
    if config["config"]["autoaccept"]:
        send("autoaccept_enabled")
    else:
        send("autoaccept_disabled")
        if (
            tkinter.messagebox.askquestion(
                "Simple File Transfer - Request to trasfer",
                f'A client "" has requested to trasfer a file to your system.\nDo you want to accept?',
            )
            == "yes"
        ):
            if not config["transferlocation"]["autolocate"]:
                location = tkinter.filedialog.askdirectory()
            else:
                location = config["transferlocation"]["location"]
        else:
            send("abort")
            websockets.close()
    send("start")
    


server = webse.serve(
    handle,
    logger=serverlogger,
    port=config["config"]["port"],
    host=config["config"]["host"],
)
serverlogger.info("Server started on *:9302")
server.serve_forever()

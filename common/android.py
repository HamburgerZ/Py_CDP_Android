from pychrome import Tab
from subprocess import Popen, PIPE
from typing import List
import re
from common.util import free_port


class Android:

    def __init__(self, deviceSerial: str = ""):
        self._deviceSerial = deviceSerial
        self._remoteDebuggingPort = 0
        self._socketNames = []
        self._deviceCmd = ""
        if self._deviceSerial == "":
            self._deviceCmd = "adb"
        else:
            self._deviceCmd = "adb -s {0} ".format(self._deviceSerial)
        
    def forward(self, socketName: str):
        self._remoteDebuggingPort = free_port()
        self.remove_forward(socketName)
        Popen("{0} forward tcp:{1} localabstract:{2}".format(self._deviceCmd, 
                                    self._remoteDebuggingPort, socketName[1:]))

    def remove_forward(self, socketName: str):
        if self.ishad_forward(socketName):
            responses = Popen("{0} forward --list".format(self._deviceCmd),
                shell=False, stdout=PIPE).stdout.readlines()
            for i in responses:
                if re.search(socketName[1:],i.decode("utf8")):
                    localTCP = re.search('tcp:[0-9]+',i.decode("utf8")).group()
                    Popen("{0} forward --remove {1}".format(self._deviceCmd, localTCP))
    
    @property
    def socketNames(self) -> List[str]:
        responses = Popen('{0} shell grep -a "@*devtools_remote_*" /proc/net/unix'.format(self._deviceCmd), 
                        shell=False, stdout=PIPE).stdout.readlines()
        for i in responses:
            socketName =  re.search('@.+devtools_remote_[0-9]+',i.decode("utf8"))
            if socketName:
                self._socketNames.append(socketName.group())
        return self._socketNames

    def ishad_forward(self, socketName: str) -> bool:
        ishadForward = False
        responses = Popen("{0} forward --list".format(self._deviceCmd),
            shell=False, stdout=PIPE).stdout.readlines()
        for i in responses:
            if re.search(socketName[1:],i.decode("utf8")):
                ishadForward = True
        return ishadForward

    @property
    def ishave_socketName(self, socketName: str) -> bool:
        if socketName in self._socketNames:
            return True
        else:
            return False

    @property
    def is_adr_online(self) -> bool:
        return False

    @property
    def remoteDebuggingPort(self) -> int:
        return self._remoteDebuggingPort

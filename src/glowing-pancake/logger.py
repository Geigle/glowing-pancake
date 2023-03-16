from enum import Enum
from io import TextIOWrapper

import os, sys, time

class Flags(Enum):
    # ENUMS
    INFO = 0 # For mundane runtime information.
    WARN = 1 # For hazardous but valid situations.
    ERR = 2 # For erros and Exceptions.
    CRIT = 3 # For unacceptable situations.

class Logger:
    def __init__(self, s_dir, s_name, b_console):
        self.console = b_console
        self.s_dir = s_dir
        self.s_name = s_name
        self.s_loc = self.s_dir + os.path.sep + self.s_name + ".log"
        self.t_start = time.asctime()        
        self.fs_out = open(self.s_loc, "w")

        self.cprint("Log location: \"" + self.s_loc + "\"")
        try:
            os.makedirs(self.s_dir)
        except FileExistsError:
            self.cprint("Directory already exists.")
        finally:
            s_out = "[Log " + self.t_start + " " + s_name + "]"
            self.cprint(s_out)
            self.fs_out.write(s_out + os.linesep)

    def close(self):
        self.fs_out.close()

    def Log(self, s_msg, e_lvl):
        s_out = "";
        match e_lvl:
            case Flags.INFO:
                s_out = "[INFO] " + time.asctime() + "- " + s_msg
            case Flags.WARN:
                s_out = "[WARNING] " + time.asctime() + "- " + s_msg
            case Flags.ERR:
                s_out = "[ERROR] " + time.asctime() + "- " + s_msg
            case Flags.CRIT:
                s_out = "[CRITICAL] " + time.asctime() + "- " + s_msg
            case _:
                s_out = "[LOGGER_ERROR] " + time.asctime() + "- Invalid match case."
        self.cprint(s_out)
        self.fs_out.write(s_out + os.linesep)
        self.fs_out.flush()

    def Info(self, s_msg):
        self.Log(s_msg, Flags.INFO)

    def Warn(self, s_msg):
        self.Log(s_msg, Flags.WARN)

    def Err(self, s_msg):
        self.Log(s_msg, Flags.ERR)

    def Crit(self, s_msg):
        self.Log(s_msg, Flags.CRIT)

    def cprint(self, s_msg):
        if(self.console):
            print(s_msg)

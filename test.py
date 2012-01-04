#!/usr/bin/python

import NUC1XX
import PirateSWD
import serial
import SWDCommon
import sys
import time


if __name__ == '__main__':
  filename = sys.argv[1]
  flash_data = NUC1XX.readFlashFile(filename)
  pirate = PirateSWD.PirateSWD('/dev/ttyUSB0')
  debugport = SWDCommon.DebugPort(pirate)
  nuc1xx = NUC1XX.NUC1XX(debugport)
  nuc1xx.halt()
  nuc1xx.changeBS()
  nuc1xx.reset()
  nuc1xx.flashUnlock()
  nuc1xx.writeBinToFlash(flash_data)
  #nuc1xx.readAllRom()
  #nuc1xx.readConfig()
  #nuc1xx.eraseFlash()
  #nuc1xx.readFlash(0x00000000)
  #nuc1xx.writeFlash(0x00000000, 0xdeadbeef)
  nuc1xx.readFlash(0x00100000, len(flash_data))
  #nuc1xx.readFlash(0x00000000)

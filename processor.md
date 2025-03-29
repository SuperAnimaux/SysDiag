# CPU diagnostic information
Read this documentation, to learn more about processor diagnostic with SysDiag.

## Architecture codes:

CPU, can have various architectures. The architectures defined the way that the CPU manage instructions. 

* x86 : Code 0
* MIPS : Code 1
* Alpha : Code 2
* PowerPC : Code 3
* ARM : Code 5
* ia64 : Code 6
* itanium system : Code 7-8
* x64 : Code 9
* ARM64 : Code 12

## Availability codes:

* Other : Code 1
* Unknown : Code 2
* Running/Full Power : Code 3
  (*Running or Full Power*)
* Warning : Code 4
* In Test : Code 5
* Not Applicable : Code 6
* Power Off : Code 7
* Off Line : Code 8
* Off Duty : Code 9
* Degraded : Code 10
* Not Installed : Code 11
* Install Error : Code 12
* Power Save - Unknown : Code 13
  (*The device is known to be in a power save state, but its exact status is unknown.*)
* Power Save - Low Power Mode : Code 14
  (*The device is in a power save state, but is still functioning, and may exhibit decreased performance.*)
* Power Save - Standby : Code 15
  (*The device is not functioning, but can be brought to full power quickly.*)
* Power Cycle : Code 16
* Power Save - Warning : Code 17
  (*The device is in a warning state, though also in a power save state.*)
* Paused : Code 18
  (*The device is paused.*)
* Not Ready : Code 19
  (*The device is not ready.*)
* Not Configured : Code 20
  (*The device is not configured.*)
* Quiesced : Code 21
  (*The device is quiet*)
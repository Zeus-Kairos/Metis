# ENR File Management Example

* * *

This VB Script program illustrates ENR file management using COM commands.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as Calibrate.vbs. Learn how to setup and run the macro.

[See Other COM Example Programs](COM_Example_Intro.md)

' Sample VBS program illustrating COM commands for ENR file management. option
explicit dim pna ' application dim enr ' ENRFile object dim scpi, hostname set
pna=CreateObject("agilentpna835x.application") set scpi = pna.ScpiStringParser
set enr = pna.ENRFile ' Generate data to put in ENR file Dim vdata(3) vdata(0)
= 100E6 ' first frequency point vdata(1) = 14.532 ' first ENR value vdata(2) =
20E9 ' second frequency point vdata(3) = 15.731 ' second ENR value ' send data
to ENRFile object enr.PutENRData(vdata) ' Set noise source serial number
enr.ENRSN = "ABCD1234" ' Write ENR file to disk enr.SaveENRFile("C:\Program
Files(x86)\Keysight\Network Analyzer\Documents\sample.enr")  
---  
  
The contents of the file created by this program are shown below.

[Filetype ENR]

[Version 1.0]

[Serialnumber ABCD1234]

! Frequency ENR

! Hz dB

100000000 14.53200

2e+010 15.73100

* * *


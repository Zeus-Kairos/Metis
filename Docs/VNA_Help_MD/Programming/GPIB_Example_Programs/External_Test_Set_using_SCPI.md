# External Test Set Control using SCPI

* * *

This program demonstrates the use of several External Test Set Control
commands.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as ExtTS.vbs. [Learn how to setup and run the
macro](../Using_Macros.htm).

' Demonstrate some SCPI commands for external testsets. Dim pna Set pna =
CreateObject("AgilentPNA835x.Application") Set scpi = pna.ScpiStringParser '
The K64 testset is only usable on a 4-port VNA If (pna.NumberOfPorts <> 4)
Then MsgBox("This program only runs on 4-port analyzers.") Else 'If Help is
active, show the measurement window and help scpi.Execute("DISP:ARR TILE")
'Return the list of supported test sets
list=scpi.Execute("SENS:MULT:CATalog?") MsgBox(list) '************* K64
***************** 'The K64 is connected using the Testset I/O 'connector.
There is no handshake information. 'Therefore, a testset need not be
connected. ' Load a configuration file. scpi.Execute("SENS:MULT1:TYPE
'Z5623AK64'") scpi.Execute("SENS:MULT1:ADDR 0") 'return stuff about the test
set ' Returns number of input ports
Inports=scpi.Execute("SENS:MULT1:INCount?") MsgBox("Input Ports: " &
CStr(Inports)) ' Returns number of output ports
ports=scpi.Execute("SENS:MULT1:COUNt?") MsgBox("Output Ports: " & CStr(ports))
' Returns valid output ports for each input port For portNum = 1 To Inports
ports=scpi.Execute("SENS:MULT1:PORT" & CStr(portNum) & ":CAT?") MsgBox("Port "
& CStr(portNum) & " catalog: " & (ports)) Next 'Set different port mapping
scpi.Execute("SENS:MULT1:ALLPorts '1 ext R,2 ext R,3 ext R,4 ext R'") 'Return
port mapping portMap=scpi.Execute("SENS:MULT1:ALLPorts?") MsgBox("Ports will
be mapped to " & CStr(portMap)) ' Enable external testset control and execute
port mapping. This automatically enables status bar display as well.
scpi.Execute("SENS:MULT1:STATe 1") MsgBox("Z5623A K64 Enabled") End If  
---


# Create an iTMSA Measurement

* * *

This example program does the following:

  * Create an iTMSA Balanced Sdd21 measurement

  * Set sweep type = power

  * Set phase offset on balanced port 1=180 degrees

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Balanced.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser '
Reset the system scpi.Parse("SYST:FPRESET") ' This example uses DUT topology
Bal-Bal -  
' a DUT with a True-mode balanced input and balanced output.  
'  
' Port mapping for our DUT:  
' logical port 1 = physical ports 1 and 3  
' logical port 2 = physical ports 2 and 4  
'  
' logical 1 logical 2  
' ___________  
' 1 ------| |------ 2 +  
' | DUT |  
' 3 ------|___________|------ 4 -  
' Turn on a window scpi.Parse("DISP:WIND1:STATe ON") ' Create a trace called
"sdd21", and for that trace turn on the balanced ' transformation and set the
balanced transformation to BBAL SDD21. scpi.Parse("CALC:PAR:DEF:EXT
""sdd21"",S11") ' Feed the sdd21 trace to window 1, trace 1
scpi.Parse("DISP:WIND1:TRAC1:FEED ""sdd21""") scpi.Parse("CALC:PAR:SEL
""sdd21""") ' Set the topology of measurement scpi.Parse("CALC:FSIM:BAL:DEVice
BBALanced") scpi.Parse("CALC:FSIM:BAL:TOPology:BBAL:PPORts 1,3,2,4") ' Set up
stimulus scpi.Parse("SENS:SWE:POINts 801") scpi.Parse("SENS:FREQ:STARt 10e6")
scpi.Parse("SENS:FREQ:STOP 1e9") scpi.Parse("CALC:FSIM:BAL:PAR:STATe ON")
scpi.Parse("CALC:FSIM:BAL:PAR:BBAL:DEF SDD21") ' Recall a 4-port Cal Set or
perform a 4-port Cal here ' Set the sweep type to power sweep
scpi.Parse("SENS:SWE:TYPE POWer") ' Set iTMSA parameters
scpi.Parse("CALC:FSIM:BAL:BPOR1:OFFS:PHAS 180")
scpi.Parse("CALC:FSIM:BAL:FIXT:OFFS:PHAS ON")
scpi.Parse("CALC:FSIM:BAL:STIM:MODE TM")  
---  
  
* * *


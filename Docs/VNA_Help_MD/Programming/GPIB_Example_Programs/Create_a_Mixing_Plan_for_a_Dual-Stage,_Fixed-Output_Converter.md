# Create a Mixing Plan for a Dual-Stage, Fixed-Output Converter

* * *

This VB Script example creates a dual-stage mixer with a fixed output. While
all the frequency ranges are explicitly programmed, the analyzer needs the
calculate command at the end to satisfy the setup.

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example. However, some modification is necessary to make the program run on a
traditional GPIB Interface. For example, during the power meter portion of
this calibration, scpi.Parse will not process a command until the power meter
routine has completed. Traditional GPIB would require a [serial polling
technique](Status_Reporting.htm) to ensure the routine has completed before
proceeding.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SMC.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
scpi.Parse "SYSTem:PRESet" ' Create a Scalar Mixer Measurement 'First, delete
all measurements on the channel scpi.Parse "CALC:PAR:DEL:ALL" 'Create a
forward scalar mixer measurement and configure it in 'channel 1. The first
parameter is a unique 'identifying string (specified by the user) to allow
subsequent 'commands to be directed at this specific measurement. scpi.Parse
"CALC:CUST:DEF 'My SC21', 'Scalar Mixer/Converter', 'SC21'" 'Setup the new
measurement as the 2nd trace in the active window scpi.Parse
"DISP:WIND:TRAC2:FEED 'My SC21'" ' Setup Stimulus ' Points and IFBW are
channel settings scpi.Parse "SENS:SWEep:POINts 21" scpi.Parse "SENS:BANDwidth
1e3" ' Mixer settings scpi.parse "SENS:MIX:STAG 2" scpi.parse
"SENS:MIX:INP:FREQ:MODE SWEPT" scpi.parse "SENS:MIX:INP:FREQ:STAR 170e6"
scpi.parse "SENS:MIX:INP:FREQ:STOP 210e6" scpi.parse "SENS:MIX:LO:FREQ:MODE
SWEPT" scpi.parse "SENS:MIX:LO:FREQ:STAR 3.89e9" scpi.parse
"SENS:MIX:LO:FREQ:STOP 3.93e9" scpi.parse "SENS:MIX:LO:FREQ:ILTI 0" scpi.parse
"SENS:MIX:IF:FREQ:SID LOW" scpi.parse "SENS:MIX:LO2:FREQ:MODE FIXED"
scpi.parse "SENS:MIX:LO2:FREQ:FIX 3.56e9" scpi.parse "SENS:MIX:LO2:FREQ:ILTI
1" scpi.Parse "SENS:MIX:OUTP:FREQ:SID LOW" scpi.parse "SENS:MIX:OUTP:FREQ:MODE
FIXED" scpi.parse "SENS:MIX:OUTP:FREQ:FIX 160e6" scpi.Parse "SENS:MIX:CALC
Input"  
---  
  
* * *


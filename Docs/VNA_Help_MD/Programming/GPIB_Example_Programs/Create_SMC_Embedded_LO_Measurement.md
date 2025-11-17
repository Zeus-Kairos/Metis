# Create an SMC Embedded LO Measurement

* * *

This VB Script example creates a SC21 SMC measurement for a mixer with an
Embedded LO.

To make an embedded LO measurement:

  * Set the LO frequency for each stage to the nominal frequency of the embedded LO. Set the LO source to "Not Controlled".

  * Calibrate as usual at the end of the measurement setup. To do this, copy the Calibration section from [Create and Cal an SMC Measurement](Create_and_Cal_an_SMC_Measurement.md).

The following are the mixer settings:

  * Single-stage Fixed LO's - Uncomment the Blue lines to measure DUAL stage mixers.

  * Swept Input and Output

  * Set Input and LO frequencies - Calculate the Output frequencies

The SCPI commands in this example are sent over a COM interface using the
SCPIStringParser object. You do NOT need a GPIB connection to run this
example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as SMC.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

Dim app Dim scpi ' Create / Get the VNA application. Set app =
CreateObject("AgilentPNA835x.Application") Set scpi = app.ScpiStringParser
scpi.Parse "SYSTem:PRESet" ' Create a Scalar Mixer Forward Measurement 'First,
delete all measurements on the channel scpi.Parse "CALC:PAR:DEL:ALL" 'Create a
forward scalar mixer measurement and configure it in 'channel 1. The first
parameter is a unique 'identifying string (specified by the user) to allow
subsequent 'commands to be directed at this specific measurement. scpi.Parse
"CALC:CUST:DEF 'My SC21', 'Scalar Mixer/Converter', 'SC21'" 'Setup the new
measurement as the 2nd trace in the active window scpi.Parse
"DISP:WIND:TRAC2:FEED 'My SC21'" 'Make the new trace the active measurement
scpi.Parse "CALC:PAR:SEL 'My SC21'" ' Setup Stimulus \- Points and IFBW are
channel settings scpi.Parse "SENS:SWEep:POINts 21" scpi.Parse "SENS:BANDwidth
1e3" 'Perform single sweep scpi.Parse "SENS:SWE:MODE SING;*OPC?" ' Mixer
settings ' Input settings (swept) scpi.Parse "SENS:MIX:INPut:FREQ:MODE SWEPt"
scpi.Parse "SENS:MIX:INPut:FREQ:STAR 3.6e9" scpi.Parse
"SENS:MIX:INPut:FREQ:STOP 3.9e9" ' LO1 settings (fixed) scpi.Parse
"SENS:MIX:LO1:FREQ:MODE FIXED" scpi.Parse "SENS:MIX:LO1:FREQ:FIX 500e6"
scpi.Parse "SENS:MIX:LO1:NAME 'Not controlled'" ' Dual-stage - LO2 settings
(fixed) ' Uncomment these lines for dual stage mixer 'scpi.Parse
"SENS:MIX:STAGE 2" 'scpi.Parse "SENS:MIX:LO2:FREQ:MODE FIXED" 'scpi.Parse
"SENS:MIX:LO2:FREQ:FIX 500e6" 'scpi.Parse "SENS:MIX:LO2:NAME 'Not controlled'"
' Output settings (calculated) scpi.Parse "SENS:MIX:OUTP:FREQ:SID LOW"
scpi.Parse "SENS:MIX:CALC Output" scpi.Parse "SENS:MIX:APPLY" ' Changing the
following default settings is usually not necessary scpi.Parse
"SENS:MIX:ELO:TUN:MODE BROadband" scpi.Parse "SENS:MIX:ELO:TUN:IFBW 30e3"
scpi.Parse "SENS:MIX:ELO:TUN:INT 1" scpi.Parse "SENS:MIX:ELO:TUN:ITER 5"
scpi.Parse "SENS:MIX:ELO:TUN:SPAN 3e6" scpi.Parse "SENS:MIX:ELO:TUN:TOL 1" '
Enable embedded LO scpi.Parse "SENS:MIX:ELO:STAT 1" 'Single sweep does the
same as "Find Now" 'from the ELO dialog scpi.Parse "SENS:SWE:MODE SING;*OPC?"
'Perform Calibration here as usual  
---  
  
* * *

* * *


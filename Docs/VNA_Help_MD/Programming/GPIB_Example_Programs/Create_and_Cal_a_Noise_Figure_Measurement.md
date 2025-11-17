# Create and Cal a Noise Figure Measurement

* * *

This example program creates a Noise Figure measurement, then calibrates the
measurement.

You MUST change the ECal Identification strings (in Blue font).

Optional: Uncomment the following lines (in Blue font) to change these
settings:

  * Noise Receiver = Noise Receiver to Std (VNA) Receiver

  * Cal Method = "Vector" to "Scalar"

  * Receiver Characterization Method = "NoiseSource" to "PowerMeter"

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
NF.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See the Noise figure commands.](../GP-IB_Command_Finder/Sense/Noise.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' This section gets the VNA application ' starts the scpi parser, and presets
the VNA windowNum = 1 channelNum = 1 set
pna=CreateObject("AgilentPNA835x.Application") set scpi = pna.ScpiStringParser
' Create noise figure measurement scpi.Parse "SYST:FPR" scpi.Parse "DISP:WIND
ON" scpi.Parse "CALC:CUST:DEF 'noiseFig', 'Noise Figure Cold Source', 'NF'"
scpi.Parse "DISP:WIND:TRAC:FEED 'noiseFig'" scpi.Parse "CALC:PAR:SEL
'noiseFig'" ' Substitute appropriate Ecal identification strings here
tunerEcal = "N4691-60004 ECal 02821" pullEcal = "N4691-60004 ECal 02297" '
configure channel ConfigureChannel ConfigureNoiseSettings ' perform
calibration SetupNoiseSource SetupCalAttributes_Insertable FinishCalibration '
\----- Support subroutines ------ ' Configure noise channel sub
ConfigureChannel scpi.Parse "SENS:FREQ:START 750MHz" scpi.Parse
"SENS:FREQ:STOP 5.0GHz" scpi.Parse "SENS:SWEEP:POINTS 401" scpi.Parse
"SENS:BWID 1.0E3" end sub ' Configure noise-specific channel settings sub
ConfigureNoiseSettings scpi.Parse "SENS:NOIS:REC NOISe" 'Use noise receivers '
scpi.Parse "SENS:NOIS:REC NORM" 'Use std PNA receiver scpi.Parse
"SENS:NOIS:AVER:STAT ON" ' turn averaging ON scpi.Parse "SENS:NOIS:AVER 40" '
noise averaging  scpi.Parse "SENS:NOIS:BWID 8MHz" ' noise bandwidth scpi.Parse
"SENS:NOIS:GAIN 30" ' gain of noise receiver scpi.Parse "SENS:NOIS:TEMP:AMB
301" ' ambient temperature, in Kelvin scpi.Parse "SENS:NOIS:IMP:COUN 5" '
number of tuner impedance states scpi.Parse "SENS:NOIS:TUN:ID '" & tunerEcal &
"'" ' set ID of tuner Ecal module scpi.Parse "SENS:NOIS:TUN:INP 'B'" '
orientation of tuner input port scpi.Parse "SENS:NOIS:TUN:OUTP 'A'" '
orientation of tuner output port scpi.Parse "SENS:CORR:TCOL:USER:VAL 300" '
noise source cold temperature end sub sub SetupCalAttributes_Insertable
scpi.Parse "SENS:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 female'" scpi.Parse
"SENS:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'" scpi.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT1 '" & pullEcal & "'" ' port 1 calkit scpi.Parse
"SENS:CORR:COLL:GUID:CKIT:PORT2 '" & pullEcal & "'" ' port 2 calkit scpi.Parse
"SENS:NOIS:SOUR:CONN 'APC 3.5 male'" ' noise source connector type scpi.Parse
"SENS:NOIS:SOUR:CKIT '" & pullEcal & "'" ' noise source calkit scpi.Parse
"SENS:NOISE:CAL:METHOD 'Vector'" ' cal method ' scpi.Parse
"SENS:NOISE:CAL:METHOD 'Scalar'" scpi.Parse "SENS:NOISE:CAL:RMEThod
'NoiseSource'" 'Receiver Characterization method ' scpi.Parse
"SENS:NOISE:CAL:RMEThod 'PowerMeter'" scpi.Parse "SENS:CORR:COLL:GUID:INIT"
end sub sub SetupNoiseSource ' specify the ENR file for the noise source
enrfile = "C:\Program Files(x86)\Keysight\Network
Analyzer\Noise\346C_MY44420454.enr" scpi.Parse "SENS:NOIS:ENR:FILENAME '" &
enrfile & "'" ' set noise source cold temperature scpi.Parse
"SENS:CORR:TCOLd:USER:VAL 301.1" end sub sub FinishCalibration ' Build the
connection list and acquire the calibration steps =
scpi.Parse("SENS:CORR:COLL:GUID:STEPS?") for i = 1 to steps str =
scpi.Parse("SENS:CORR:COLL:GUID:DESC? " & i) msgbox str scpi.Parse
"SENS:CORR:COLL:GUID:ACQ STAN" & i next scpi.Parse "SENS:CORR:COLL:GUID:SAVE
0" wscript.echo "Calibration complete" end sub  
---  
  
* * *

* * *


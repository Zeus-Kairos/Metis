# Create a Spectrum Analyzer Measurement

This example program creates a Spectrum Analyzer measurement setup.

This VBScript program can be run as a macro in the VNA. To do this, copy the
code into a text editor file such as Notepad and save on the VNA hard drive as
SA.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

[See the Spectrum Analyzer commands.](../GP-IB_Command_Finder/Sense/SA.md)

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

' Demonstration of basic Spectrum Analyzer measurement setup. set
pna=CreateObject("AgilentPNA835x.Application","hostname") set scpi =
pna.ScpiStringParser CreateSAMeasurement SetupLinearSweep
ConfigureAdvancedSettings ' Create a Spectrum Analyzer measurement Sub
CreateSAMeasurement ' Create a B measurement on channel 1 scpi.Parse
"SYST:FPR" scpi.Parse "DISP:WIND ON" scpi.Parse "CALC:CUST:DEF 'sa_meas',
'Spectrum Analyzer', 'B'" scpi.Parse "DISP:WIND:TRAC:FEED 'sa_meas'"
scpi.Parse "CALC:PAR:SEL 'sa_meas'" ' Set frequency range scpi.Parse
"SENS:FREQ:CENTER 3 GHz" scpi.Parse "SENS:FREQ:SPAN 2 GHz" ' Center frequency
step size ' Set to Auto mode with SENS:FREQ:CENTER:STEP:AUTO ON scpi.Parse
"SENS:FREQ:CENTER:STEP:SIZE 20 MHz" ' RBW filter shape ' Choices are
GAUSsian|FLATtop|KAISer|BLACkman|NONe scpi.Parse "SENS:SA:BAND:SHAPE KAIS" '
RBW and VBW values scpi.Parse "SENS:SA:BAND:RES 100 kHz" scpi.Parse
"SENS:SA:BAND:VID 10 kHz" ' Detector type ' Choices are
AVERage|SAMPle|PEAK|NORMal|NEGPeak|PSAMple|PAVerage scpi.Parse
"SENS:SA:DET:FUNC PEAK" ' Video averaging type ' Choices are
POWer|LOG|VOLTage|VMAX|VMIN scpi.Parse "SENS:SA:BAND:VID:AVER:TYPE VMAX"
scpi.Parse "SENS:SA:BAND:VID:AVER:COUNT?" ' RBW/VBW and Span/RBW ratios
scpi.Parse "SENS:SA:BAND:VID:RAT 1.23" scpi.Parse "SENS:SA:FREQ:SPAN:BAND:RAT
134" ' ADC Filter ' Choices are 11MHz|38MHz ' Enable auto mode with
SENS:SA:ADC:FILT:AUTO. scpi.Parse "SENS:SA:ADC:FILTer 38MHz" End Sub '
Configure a Spectrum Analyzer measurement for Linear sweep mode on Port 1. Sub
SetupLinearSweep ' Turn Port 1 ON scpi.Parse "SOURCE:POW:MODE ON" ' Set Port 1
sweep type to Linear scpi.Parse "SENS:SA:SOURCE1:SWEEP:TYPE LIN" ' Set start
and stop frequencies scpi.Parse "SENS:SA:SOURCE1:FREQ:START 2E9" scpi.Parse
"SENS:SA:SOURCE1:FREQ:STOP 4E9" ' Set 'Source Number of Steps'. This is the
number of frequencies to use between start and stop (inclusive). ' This
setting is channel-wide. scpi.Parse "SENS:SA:SOUR:SWEEP:POINT:COUNT 5" ' Set
'SA Sweeps per Source Steps'. This is the number of sweeps to take at each
measurement frequency. ' This setting is also channel-wide. scpi.Parse
"SENS:SA:SOUR:SWEEP:REPEAT:COUNT 2" End Sub ' Configure a few of the Advanced
Settings for SA. Sub ConfigureAdvancedSettings ' Set the 'Image Reject'
selection. ' Choices are MIN MAX NORM NLOW NHIGH scpi.Parse "SENS:SA:IMAGE:REJ
MAX" ' Enable display of ImageReject traces. scpi.Parse
"SENS:SA:TRACE:IMAGE:STATE ON" ' Enable point mode. ' This forces the number
of display points to match the FFT point count. scpi.Parse "SENS:SA:DET:BYPASS
ON" End Sub  
---


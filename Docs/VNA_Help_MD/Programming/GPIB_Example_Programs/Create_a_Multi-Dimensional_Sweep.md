# Create a Multi-Dimensional Sweep

* * *

This program can be run as a macro in the PNA. To do this, copy the code into
a text editor file such as Notepad and save on the PNA hard drive as
<filename>.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

Multi-Dimensional Sweep Commands

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

'Demonstration of multi-dimensional sweep setup.  
set pna = CreateObject("AgilentPNA835x.Application","A-N5242A-10096")  
set scpi = pna.ScpiStringParser  
CreateSAMeasurement  
SetupMultiSweep Sub CreateSAMeasurement  
scpi.Parse "SYST:FPR"  
scpi.Parse "DISP:WIND ON"  
scpi.Parse "CALC:CUST:DEF 'sa_meas', 'Spectrum Analyzer', 'R1'"  
scpi.Parse "DISP:WIND:TRAC:FEED 'sa_meas'"  
scpi.Parse "CALC:PAR:SEL 'sa_meas'"  
scpi.Parse "SENS:SWE:MODE HOLD"  
End Sub Sub SetupMultiSweep 'Turn Port 1 ON  
scpi.Parse "SOUR:POW1:MODE ON"  
'Configure Port 1 frequency start/stop range  
scpi.Parse "SOUR:FREQ1:START 2E9"  
scpi.Parse "SOUR:FREQ1:STOP 4E9"  
'Set Port 1 frequency domain's order to 3  
scpi.Parse "SOUR:FREQ1:DIM:ORDER 3"  
'Enable Port 1 frequency domain in multi-dimensional sweep  
scpi.Parse "SOUR:FREQ1:DIM:STAT ON"  
'Configure Port 1 power start/stop range  
scpi.Parse "SOUR:POW1:START -5"  
scpi.Parse "SOUR:POW1:STOP 5"  
'Set Port 1 power domain's order to 5  
scpi.Parse "SOUR:POW1:DIM:ORDER 5"  
'Enable Port 1 power domain in multi-dimensional sweep  
scpi.Parse "SOUR:POW1:DIM:STAT ON"  
'Configure Port 1 phase start/stop range  
scpi.Parse "SOUR:PHAS1:START 0"  
scpi.Parse "SOUR:PHAS1:STOP 270"  
'Set Port 1 phase domain's order to 4  
scpi.Parse "SOUR:PHAS1:DIM:ORDER 4"  
'Enable Port 1 phase domian in multi-dimensional sweep  
scpi.Parse "SOUR:PHAS1:DIM:STAT ON" 'Turn Port 3 ON  
scpi.Parse "SOUR:POW3:MODE ON"  
'Configure Port 3 frequency start/stop range  
scpi.Parse "SOUR:FREQ3:START 2E9"  
scpi.Parse "SOUR:FREQ3:STOP 4E9"  
'Set Port 3 frequency domain's order to 3  
scpi.Parse "SOUR:FREQ3:DIM:ORDER 3"  
'Enable Port 3 frequency domain in multi-dimensional sweep  
scpi.Parse "SOUR:FREQ3:DIM:STAT ON"  
'Configure Port 3 power start/stop range  
scpi.Parse "SOUR:POW3:START -5"  
scpi.Parse "SOUR:POW3:STOP 5"  
'Set Port 3 power domain's order to 5  
scpi.Parse "SOUR:POW3:DIM:ORDER 5"  
'Enable Port 3 power domain in multi-dimensional sweep  
scpi.Parse "SOUR:POW3:DIM:STAT ON"  
'Configure Port 3 phase start/stop range  
scpi.Parse "SOUR:PHAS3:START 0"  
scpi.Parse "SOUR:PHAS3:STOP 270"  
'Set Port 3 phase domain's order to 4  
scpi.Parse "SOUR:PHAS3:DIM:ORDER 4"  
'Enable Port 3 phase domain in multi-dimensional sweep  
scpi.Parse "SOUR:PHAS3:DIM:STAT ON" 'Turn AO1 ON  
scpi.Parse "SOUR:DC:STAT 'AO1', ON"  
'Configure AO1 start/stop range  
scpi.Parse "SOUR:DC:START 'AO1', 0"  
scpi.Parse "SOUR:DC:STOP 'AO1',2"  
'Set AO1's order to 2  
scpi.Parse "SOUR:DC:DIM:ORDER 'AO1', 2"  
'Enable AO1 in multi-dimensional sweep  
scpi.Parse "SOUR:DC:DIM:STAT 'AO1', ON" 'Set dimension order 3's point count
to 3  
scpi.Parse "SOUR:DIM3:POIN 3"  
'Set dimension order 3's repeat count to 1  
scpi.Parse "SOUR:DIM3:REP:COUN 1"  
'Set dimension order 4's point count to 4  
scpi.Parse "SOUR:DIM4:POIN 4"  
'Set dimension order 4's repeat count to 1  
scpi.Parse "SOUR:DIM4:REP:COUN 1"  
'Set dimension order 5's point count to 5  
scpi.Parse "SOUR:DIM5:POIN 5"  
'set dimension order 5's repeat count to 1  
scpi.Parse "SOUR:DIM5:REP:COUN 1" End Sub  
---


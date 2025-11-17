# Noise Power Ratio (NPR) Correction Example

The following example uses port 4 and port 1, and a MXG named "MyMXG". The MXG
is connected to port 4's rear panel. It uses a NPR modulation file
"D:\ModulationFile\npr.csv" and saves the corrected modulation file into
"D:\ModulationFile\npr.mdx".

[See Other SCPI Example Programs](SCPI_Example_Programs.md)

*IDN? SYST:FPR DISP:WIND1:STAT ON CALC:CUST:DEF 'CH1_A','Spectrum Analyzer','A' DISP:WIND1:TRAC1:FEED 'CH1_A' SENS:PATH:CONF:ELEM 'Port4Bypass', 'RearPanel' SYST:CONF:EDEV:STATe 'MyMxg', ON SOUR:MOD6:LOAD 'D:\ModulationFile\npr.csv' SENS:SA:COH:DIST:MOD:STAT ON SOUR:POW6:MODE ON SOUR:MOD6:CORR:COLL:POW:ENAB 1 SOUR:MOD6:CORR:COLL:POW:REC "A" SOUR:MOD6:CORR:COLL:FLAT:ENAB 1 SOUR:MOD6:CORR:COLL:FLAT:REC "R4" SOUR:MOD6:CORR:COLL:NOTCh:ENAB 1 SOUR:MOD6:CORR:COLL:NOTCh:REC "R4" SOUR:MOD6:CORR:COLL:ACP:ENAB 1 SOUR:MOD6:CORR:COLL:ACP:SPAN 30e6 SOUR:MOD6:CORR:COLL:ACP:REC "R4" SOUR:MOD6:CORR:COLL:FAST:ENAB 1 SOUR:MOD6:CORR:COLL:ACQ *OPC? SOUR:MOD6:CORR:COLL:ACQ:STAT? SOUR:MOD6:CORR:STAT ON  
---


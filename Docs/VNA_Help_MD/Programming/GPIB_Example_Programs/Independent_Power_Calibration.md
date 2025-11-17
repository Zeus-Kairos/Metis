# Independent Power Calibration

* * *

The following program creates an independent power calibration over a
specified frequency span when performing a Cal All.

This VBScript (*.vbs) program can be run as a macro in the PNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the PNA hard drive as BalancedCOM.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

SYST:PRESET sens:freq:start 1e9 sens:freq:stop 2e9 calc2:par:def "S22Ch2",S22
disp:wind:trac2:feed "S22Ch2" sens2:freq:start 5e9 sens2:freq:stop 7e9
SYST:CAL:ALL:RESet syst:cal:all:sel 1,2 syst:cal:all:chan1:port:sel 1,2
syst:cal:all:mcl:prop:val "Include Power Calibration","true"
syst:cal:all:mcl:prop:val "Enable Extra Power Cals","Port 2,Port 3"
SYST:CAL:ALL:GUID:CHAN? syst:cal:all:ind:sour:cal:cat?
syst:cal:all:ind:sour3:cal:range:add syst:cal:all:ind:sour3:cal:range1:start
3e9 syst:cal:all:ind:sour3:cal:range1:stop 4e9
syst:cal:all:ind:sour3:cal:range1:points 21
syst:cal:all:ind:sour3:cal:range:add syst:cal:all:ind:sour3:cal:range2:start
20e9 syst:cal:all:ind:sour3:cal:range2:stop 21e9
syst:cal:all:ind:sour3:cal:range2:points 7
syst:cal:all:ind:sour2:cal:range:add syst:cal:all:ind:sour2:cal:range1:start
3e9 syst:cal:all:ind:sour2:cal:range1:stop 4e9
syst:cal:all:ind:sour2:cal:range1:points 21
syst:cal:all:ind:sour2:cal:rang:count? syst:cal:all:ind:sour3:cal:rang:count?
syst:cal:all:ind:sour2:cal:rang:clear syst:cal:all:ind:sour2:cal:range:count?
syst:cal:all:ind:sour3:cal:range1:start?
syst:cal:all:ind:sour3:cal:range1:stop?
syst:cal:all:independent:source3:cal:range1:points?
syst:cal:all:ind:sour3:cal:range2:start?
syst:cal:all:ind:sour3:cal:range2:stop?
syst:cal:all:ind:sour3:cal:range2:points? SYST:CAL:ALL:PORT1:SOUR:POW:ATT 0
SYST:CAL:ALL:PORT1:REC:ATT 0 SENS500:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 male'
SENS500:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 female' SYST:CAL:ALL:GUID:PORT?
SENS500:CORR:COLL:GUID:CKIT:PORT1 'N4691-61004 ECal 13442'
SENS500:CORR:COLL:GUID:CKIT:PORT2 'N4691-61004 ECal 13442'
SENS500:CORR:COLL:GUID:PSEN1:POW:LEV -5 SENS500:CORR:COLL:GUID:INIT
SENS500:CORR:COLL:GUID:STEP? SENS500:CORR:COLL:GUID:DESC? 1 **PAUSE**
SENS500:CORR:COLL:GUID:ACQ STAN1 SENS500:CORR:COLL:GUID:DESC? 2 **PAUSE**
SENS500:CORR:COLL:GUID:ACQ STAN2 SENS500:CORR:COLL:GUID:DESC? 3 **PAUSE**
SENS500:CORR:COLL:GUID:ACQ STAN3 SENS500:CORR:COLL:GUID:SAVE  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


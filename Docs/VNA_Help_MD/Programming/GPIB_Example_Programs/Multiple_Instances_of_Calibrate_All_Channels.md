# Multiple Instances of Calibrate All Channels

Note: **You can assign a single client channel to multiple cal all instances.
However, care should be taken here. If you create user calests, all calsets
will be created but only the last one will be applied. If you are only using a
cal register, only the last cal all will be written to the cal register (only
supports one claibration). The order that the cal alls are created should be
the order in which they are saved ([SENS200:CORR:COLL:GUID:SAVE)](../GP-
IB_Command_Finder/Sense/CorrGuided.htm#gSave). This ensures that the client
channel imports the proper ETerms.**

#create 4 total channels: #does one calall on channels 1/2 with ports 1/2
selected and power cal on P1 #does another calall on channels 3/4 with ports
3/4 selected and no power cal syst:preset calc2:par:ext 'ch2_s11','S11'
DISPlay:WINDow1:TRACe2:FEED "ch2_s11" calc3:par:ext 'ch3_s11','S11'
DISPlay:WINDow1:TRACe3:FEED "ch3_s11" calc4:par:ext 'ch4_s11','S11'
DISPlay:WINDow1:TRACe4:FEED "ch4_s11" SYST:CAL:ALL:RESet
SYST:CAL:ALL:CHAN1:PORT:SEL 1,2 SYST:CAL:ALL:CHAN2:PORT:SEL 1,2
SYST:CAL:ALL:CSET:PREFIX 'firstCal' SYST:CAL:ALL:GUID:CHAN? #returns 200
SYST:CAL:ALL2:RESet SYST:CAL:ALL2:SEL 3,4 SYST:CAL:ALL2:CSET:PREFIX
'secondCal' SYST:CAL:ALL2:CHAN3:PORT:SEL 3,4 SYST:CAL:ALL2:CHAN4:PORT:SEL 3,4
SYST:CAL:ALL2:GUID:CHAN? #returns 500 #do power cal for first
SYST:CAL:ALL:MCL:PROP:VAL 'Include Power Calibration', 'True' #but not on the
second SYST:CAL:ALL2:MCL:PROP:VAL 'Include Power Calibration', 'False'
SENS200:corr:coll:guid:conn:port1 "APC 3.5 male"
SENS200:corr:coll:guid:conn:port2 "APC 3.5 male"
SENS200:CORR:COLL:GUID:CKIT:PORT1 '85052D' SENS200:CORR:COLL:GUID:CKIT:PORT2
'85052D' SENS200:CORR:COLL:GUID:INIT SENS200:CORR:COLL:GUID:STEP?
SENS500:corr:coll:guid:conn:port3 "APC 3.5 male"
SENS500:corr:coll:guid:conn:port4 "APC 3.5 male"
SENS500:CORR:COLL:GUID:CKIT:PORT3 '85052D' SENS500:CORR:COLL:GUID:CKIT:PORT4
'85052D' SENS500:CORR:COLL:GUID:INIT SENS500:CORR:COLL:GUID:STEP? #in this
case, cals are totally different (different ports) #just do one and then the
other #first step for first cal is the power step:
SENS200:CORR:COLL:GUID:DESC? 1 SENS200:CORR:COLL:GUID:ACQ STAN1; *OPC?
SENS200:CORR:COLL:GUID:DESC? 2 SENS200:CORR:COLL:GUID:ACQ STAN2; *OPC?
SENS200:CORR:COLL:GUID:DESC? 3 SENS200:CORR:COLL:GUID:ACQ STAN3; *OPC?
SENS200:CORR:COLL:GUID:DESC? 4 SENS200:CORR:COLL:GUID:ACQ STAN4; *OPC?
SENS200:CORR:COLL:GUID:DESC? 5 SENS200:CORR:COLL:GUID:ACQ STAN5; *OPC?
SENS200:CORR:COLL:GUID:DESC? 6 SENS200:CORR:COLL:GUID:ACQ STAN6; *OPC?
SENS200:CORR:COLL:GUID:DESC? 7 SENS200:CORR:COLL:GUID:ACQ STAN7; *OPC?
SENS200:CORR:COLL:GUID:DESC? 8 SENS200:CORR:COLL:GUID:ACQ STAN8; *OPC? #now do
second cal: SENS500:CORR:COLL:GUID:DESC? 1 SENS500:CORR:COLL:GUID:ACQ STAN1;
*OPC? SENS500:CORR:COLL:GUID:DESC? 2 SENS500:CORR:COLL:GUID:ACQ STAN2; *OPC?
SENS500:CORR:COLL:GUID:DESC? 3 SENS500:CORR:COLL:GUID:ACQ STAN3; *OPC?
SENS500:CORR:COLL:GUID:DESC? 4 SENS500:CORR:COLL:GUID:ACQ STAN4; *OPC?
SENS500:CORR:COLL:GUID:DESC? 5 SENS500:CORR:COLL:GUID:ACQ STAN5; *OPC?
SENS500:CORR:COLL:GUID:DESC? 6 SENS500:CORR:COLL:GUID:ACQ STAN6; *OPC?
SENS500:CORR:COLL:GUID:DESC? 7 SENS500:CORR:COLL:GUID:ACQ STAN7; *OPC? #SAVE!!
SENS200:CORR:COLL:GUID:SAVE SENS500:CORR:COLL:GUID:SAVE  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


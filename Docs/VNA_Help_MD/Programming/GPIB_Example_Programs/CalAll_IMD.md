# Cal All - IMD

'\---------------------------------------- ' CHANNEL 1: IMD
'\---------------------------------------- disp:wind:state on CALC:CUST:DEF
'PwrMain1', "Swept IMD", "PwrMain" DISP:WIND:TRAC1:FEED 'PwrMain1'
SENS:SWE:POIN 11 SENS:FREQ:START 4E9 SENS:FREQ:STOP 8E9 SENS:IMD:FREQ:DFR:CW
2E6 CALC:PAR:CAT? '\---------------------------------------- ' CAHNNEL 2: imd
'\---------------------------------------- DISP:WIND2:STATE ON CALC2:CUST:DEF
'PwrMain2', "Swept IMD", "PwrMain" SYST:ERR? DISP:WIND2:TRAC1:FEED 'PwrMain2'
SENS2:SWE:POIN 21 SENS2:FREQ:START 18E9 SENS2:FREQ:STOP 20E9
SENS2:IMD:FREQ:DFR:CW 100E3 SYST:ERR?
'\---------------------------------------- ' configure the power sensor for
cal '\---------------------------------------- SYST:COMM:PSEN USB, "Agilent
Technologies,U8485A,my53470003" '\---------------------------------------- '
configure calibrate all '\----------------------------------------
SYST:CAL:ALL:CSET:PREFIX "imdcalall" SYST:CAL:ALL:RESET SYST:CAL:ALL:SEL 1,2
SYST:CAL:ALL:CHAN1:PORTS:SEL 1,2 SYST:CAL:ALL:CHAN2:PORTS:SEL 1,2
'\---------------------------------------------------------- ' we want to
calibrate for 2nd order products on channel 1 ' but not on channel 2. Here's
how to do it. '\----------------------------------------------------------
SYST:CAL:ALL:MCLASS:PROP:VAL:STATE "Max Product Order", "5"
SYST:CAL:ALL:MCLASS:PROP:VAL:STATE "Include 2nd Order", "True"
SYST:CAL:ALL:MCLASS:PROP:VAL:STATE "Exclude Channels From 2nd Order", "2"
'\---------------------------------------- ' retrieve the guided cal channel
number '\---------------------------------------- SYST:CAL:ALL:GUIDED:CHAN?
'\------------------------------------------------- ' configure a calibration
for the cal all channel '\-------------------------------------------------
SENS200:CORR:COLL:GUID:CONN:PORT1:SEL "APC 3.5 male"
SENS200:CORR:COLL:GUID:CONN:PORT2:SEL "APC 3.5 female"
SENS200:CORR:COLL:GUID:ckit:port2:SEL "N4691-60004 ECal"
SENS200:CORR:COLL:GUID:ckit:port1:SEL "N4691-60004 ECal"
sens200:CORR:COLL:GUID:INIT SYST:ERR?
'\---------------------------------------- ' acquire teh cal
'\---------------------------------------- sens200:CORR:COLL:GUID:STEPS?
sens200:CORR:COLL:GUID:ACQ STAN1 SENS200:CORR:COLL:GUID:ACQ STAN2
SENS200:CORR:COLL:GUID:SAVE  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


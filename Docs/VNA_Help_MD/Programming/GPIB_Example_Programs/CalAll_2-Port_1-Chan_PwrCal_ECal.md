# Cal All - 2-Port, 1-Channel, Power Cal, with ECal

' ' calibrate 2 ports, power cal, ECal ' system:preset; SYST:COMM:PSEN USB,
"Agilent Technologies,U2002A,my51240006" CALC:PAR:DEF "S11", S11 CALC2:PAR:DEF
"S22", S22 SYST:CAL:ALL:RESet SYST:CAL:ALL:SEL 1 SYST:CAL:ALL:CHAN1:PORT:SEL
1,2 SYST:CAL:ALL:MCL:PROP:VAL "Include Power Calibration","true"
SYST:CAL:ALL:GUID:CHAN? SENS200:CORR:COLL:GUID:PSEN1:CONN 'Ignored'
SENS200:CORR:COLL:GUID:PSEN1:CKIT 'Not used' SENS200:corr:coll:guid:conn:port1
"APC 3.5 male" SENS200:corr:coll:guid:conn:port2 "APC 3.5 female"
SENS200:corr:coll:guid:ckit:port1 "N4691-60004 ECal"
SENS200:corr:coll:guid:ckit:port2 "N4691-60004 ECal"
SENS200:CORR:COLL:GUID:INIT SENS200:CORR:COLL:GUID:STEPs?
SENS200:corr:coll:guid:acq stan1 SENS200:corr:coll:guid:acq stan2
SENS200:corr:coll:guid:save  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


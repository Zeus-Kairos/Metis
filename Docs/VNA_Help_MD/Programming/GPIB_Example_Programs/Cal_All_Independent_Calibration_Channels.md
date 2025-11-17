# Cal All Independent Calibration Channels

Set pna = CreateObject("AgilentPNA835x.Application") Set scpi =
pna.ScpiStringParser scpi.Parse "SYST:PRESET" scpi.Parse "SYST:CAL:ALL:RES"
scpi.Parse "SYST:CAL:ALL:GUID:CHAN?" scpi.Parse "SYST:CAL:ALL:SEL?" scpi.Parse
"SYST:CAL:ALL:MCL:PROP:VAL 'Include Power Calibration', 'True'" 'The following
SCPI will request Channel 1 to do its own calibration: scpi.Parse
"SYST:CAL:ALL:MCL:PROP:VAL 'Independent Calibration Channels', '1'" scpi.Parse
"SYST:CAL:ALL:CHAN1:PORT 1,2" scpi.Parse "SYST:CAL:ALL:CHAN1:PORT:SEL?"
scpi.Parse "SENS200:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 male'" scpi.Parse
"SENS200:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'" scpi.Parse
"SYST:CAL:ALL:GUID:PORT?" scpi.Parse "SENS200:CORR:COLL:GUID:CKIT:PORT1
'85052D'" scpi.Parse "SENS200:CORR:COLL:GUID:CKIT:PORT2 '85052D'" scpi.Parse
"SENS200:CORR:COLL:GUID:PSEN1:POW:LEV -5" 'Even though Ch1 is performing its
own calibration, interface through CalAll is the same: scpi.Parse
"SYST:CAL:ALL:GUID:CHAN?" scpi.Parse "SENS200:CORR:COLL:GUID:INIT" scpi.Parse
"SENS200:CORR:COLL:GUID:STEP?" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 1"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 2" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 3" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 5"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 4" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 6" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 7"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 8" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN1;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN2;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN3;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN4;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN5;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN6;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN7;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN8;" scpi.Parse "SENS200:CORR:COLL:GUID:SAVE:CSET 'exampleIndependentCal'"  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


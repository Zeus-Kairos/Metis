# Cal All SMC Split Cal

Set pna = CreateObject("AgilentPNA835x.Application") Set scpi =
pna.ScpiStringParser scpi.Parse "SYST:PRESET" scpi.Parse "calc:par:del:all"
scpi.Parse "calc:cust:def 'sc12','Scalar Mixer/Converter','SC12'" scpi.Parse
"disp:wind:trac1:feed 'sc12'" scpi.Parse "*OPC?" scpi.Parse
"SYST:CAL:ALL:RESet" scpi.Parse "syst:cal:all:sel 1" scpi.Parse
"SYST:CAL:ALL:CSET:PREFix 'smcSplit'" scpi.Parse "syst:cal:all:chan1:port:sel
1,2" scpi.Parse "syst:cal:all:mcl:prop:val 'Include Power Calibration','true'"
'Split Cal attribute MUST be sent before setting connectors & kits scpi.Parse
"SYST:CAL:ALL:MCL:PROP:VAL 'Split Cal', 'True'" scpi.Parse
"SYST:CAL:ALL:GUID:CHAN?" scpi.Parse "SENS200:CORR:COLL:GUID:CONN:PORT1 'APC
3.5 male'" scpi.Parse "SENS200:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'"
scpi.Parse "SENS200:CORR:COLL:GUID:CKIT:PORT1 '85052D'" scpi.Parse
"SENS200:CORR:COLL:GUID:CKIT:PORT2 '85052D'" scpi.Parse
"SENS200:CORR:COLL:GUID:INIT" scpi.Parse "SENS200:CORR:COLL:GUID:STEP?" 'Note
that Step 1 is to connect Power Sensor to Port 1 'And Step 2 is to connect
Power Sensor to Port 2 'Performing two 1-Port calibrations instead of a 2-port
calibration scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 1" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 2" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 3"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 4" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 5" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 6"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 7" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 8" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN1;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN2;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN3;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN4;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN5;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN6;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN7;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN8;" scpi.Parse
"sens200:corr:coll:guid:save;*opc?"  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


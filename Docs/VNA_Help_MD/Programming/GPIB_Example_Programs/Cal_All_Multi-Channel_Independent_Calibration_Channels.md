# Cal All Multi-Channel Independent Calibration Channels

Set pna = CreateObject("AgilentPNA835x.Application") Set scpi =
pna.ScpiStringParser scpi.Parse "SYST:PRESET" scpi.Parse "calc:par:del:all"
scpi.Parse "calc1:cust:def 'CompS11','Gain Compression Converters','CompS11'"
scpi.Parse "calc2:cust:def 'S11','Standard','S11'" scpi.Parse "calc3:cust:def
'b1','Spectrum Analyzer','b1'" scpi.Parse "calc4:cust:def
'S11_1','Standard','S11'" scpi.Parse "calc5:cust:def 'S22','Standard','S22'"
scpi.Parse "calc6:cust:def 'S44','Standard','S44'" scpi.Parse
"display:wind1:trace1:feed 'CompS11'" scpi.Parse "display:wind1:trace2:feed
'S11'" scpi.Parse "display:wind1:trace3:feed 'b1'" scpi.Parse
"display:wind1:trace4:feed 'S11_1'" scpi.Parse "display:wind1:trace5:feed
'S22'" scpi.Parse "display:wind1:trace6:feed 'S44'" scpi.Parse
"sens2:sweep:lfex:state ON" scpi.Parse "sens4:sweep:lfex:state ON" scpi.Parse
"sens6:sweep:lfex:state ON" scpi.Parse "*OPC?" scpi.Parse "SYST:CAL:ALL:RES"
scpi.Parse "SYST:CAL:ALL:GUID:CHAN?" scpi.Parse "SYST:CAL:ALL:SEL?" scpi.Parse
"SYST:CAL:ALL:MCL:PROP:VAL 'Include Power Calibration', 'True'" 'Identifiying
independnet power calibration channels: scpi.Parse "SYST:CAL:ALL:MCL:PROP:VAL
'Independent Calibration Channels', '2,4'" scpi.Parse "SYST:CAL:ALL:CHAN1:PORT
1,2" scpi.Parse "SYST:CAL:ALL:CHAN1:PORT:SEL?" scpi.Parse
"SYST:CAL:ALL:CHAN2:PORT 1,2" scpi.Parse "SYST:CAL:ALL:CHAN2:PORT:SEL?"
scpi.Parse "SYST:CAL:ALL:CHAN3:PORT 1,2" scpi.Parse
"SYST:CAL:ALL:CHAN3:PORT:SEL?" scpi.Parse "SYST:CAL:ALL:CHAN4:PORT 1,2,4"
scpi.Parse "SYST:CAL:ALL:CHAN4:PORT:SEL?" scpi.Parse
"SENS200:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 male'" scpi.Parse
"SENS200:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 male'" scpi.Parse
"SENS200:CORR:COLL:GUID:CONN:PORT4 'APC 3.5 male'" scpi.Parse
"SYST:CAL:ALL:GUID:PORT?" scpi.Parse "SENS200:CORR:COLL:GUID:CKIT:PORT1
'85052D'" scpi.Parse "SENS200:CORR:COLL:GUID:CKIT:PORT2 '85052D'" scpi.Parse
"SENS200:CORR:COLL:GUID:CKIT:PORT4 '85052D'" 'Commands sent to channel 200
will apply to call client channels: scpi.Parse
"SENS200:CORR:COLL:GUID:PSEN1:POW:LEV -5" 'To change the value for a
particular client, use that channel instead: scpi.Parse
"SENS2:CORR:COLL:GUID:PSEN1:POW:LEV -9" scpi.Parse
"SENS200:CORR:COLL:GUID:INIT" scpi.Parse "SENS200:CORR:COLL:GUID:STEP?"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 1" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 2" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 3"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 5" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 4" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 6"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 7" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 8" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 9"
scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 10" scpi.Parse
"SENS200:CORR:COLL:GUID:DESC? 11" scpi.Parse "SENS200:CORR:COLL:GUID:DESC? 12"
'Note: Even though user is only prompted once for a power sensor connection
'In this case - it performs 4 sweeps: One on CalAll channels 200, and 500
(LFE) 'And one on channel 2 and one on channel 4(independnet calibrations)
scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN1;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN2;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN3;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN4;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN5;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN6;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN7;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN8;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN9;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ STAN10;" scpi.Parse
"SENS200:CORR:COLL:GUID:ACQ STAN11;" scpi.Parse "SENS200:CORR:COLL:GUID:ACQ
STAN12;" scpi.Parse "sens200:corr:coll:guid:save;*opc?"  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


# Cal All - Noise Figure

'\------------------------------------------ ' create NF channel
'\------------------------------------------ SYST:FPRESET DISP:WIND:STATE ON
CALC1:MEAS1:DEF "S11:Noise Figure Cold Source" DISP:MEAS1:FEED 1
CALC1:MEAS2:DEF "NF:Noise Figure Cold Source" DISP:MEAS2:FEED 1
'\------------------------------------------ ' configure power sensor
'\------------------------------------------ system:communicate:psensor usb,
"Agilent Technologies,U8485A,MY53470003"
'\------------------------------------------ ' configure calibrate all
'\------------------------------------------ SYST:CAL:ALL:RESET
SYST:CAL:ALL:CSET:PREFIX "Example" SYST:CAL:ALL:SEL 1
SYST:CAL:ALL:CHAN1:PORTS:SEL 1,2 '\------------------------------------------
' use this query to see what cal all properties are ' relevant to the noise
figure channel '\------------------------------------------
SYST:CAL:ALL:MCLASS:PROP:NAME:CAT? "Noise Figure Cold Source"
'\------------------------------------------ ' set scalar noise cal, using
power meter '\------------------------------------------
SYST:CAL:ALL:MCLASS:PROP:VAL:STATE "Noise Cal Method", "Scalar"
SYST:CAL:ALL:MCLASS:PROP:VAL:STATE "Receiver Characterization Method", "Use
Power Meter" '\------------------------------------------ ' retrieve the
guided cal channel number '\------------------------------------------
SYST:CAL:ALL:GUIDED:CHAN? ' configure the sensor ' set ignored unless you want
to calibrate ' an adapter used for the power sensor.
SENS200:CORR:COLL:GUID:PSEN1:CONN 'Ignored' SENS200:CORR:COLL:GUID:PSEN1:CKIT
'Not used' SENS200:CORR:COLL:GUID:PSEN1:POW:LEV -15
'\------------------------------------------------- ' configure basic cal
properties: connectors, kits ' NOTE: always fully specify ecals when Noise
figure ' is in the channel list. IE: include the ecal serial ' number!
'\-------------------------------------------------
SENS200:CORR:COLL:GUID:CONN:PORT1:SEL "APC 3.5 male"
SENS200:CORR:COLL:GUID:CONN:PORT2:SEL "APC 3.5 female"
SENS200:CORR:COLL:GUID:ckit:port2:SEL "N4691-60004 ECal 02297"
SENS200:CORR:COLL:GUID:ckit:port1:SEL "N4691-60004 ECal 02297"
SENS200:CORR:COLL:GUID:INIT ' acquire the calibration
SENS200:CORR:COLL:GUID:STEPS? SENS200:CORR:COll:guid:DESC? 1
SENS200:CORR:COLL:GUID:ACQ STAN1 SENS200:CORR:COLL:GUID:desc? 2
SENS200:CORR:COLL:GUID:ACQ STAN2 SENS200:CORR:COLL:GUID:desc? 3
SENS200:CORR:COLL:GUID:ACQ STAN3 SENS200:CORR:COLL:GUID:SAVE  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


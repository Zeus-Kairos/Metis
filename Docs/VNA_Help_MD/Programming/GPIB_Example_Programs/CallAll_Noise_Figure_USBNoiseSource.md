# CallAll_Noise Figure_USBNoiseSource

Dim app Set app = CreateObject("Agilentpna835x.application","hostname") Set
scpi = app.ScpiStringParser scpi.Parse("SYST:PRESET")
scpi.Parse("calc:par:del:all") scpi.Parse("calc:cust:def "ENR","Noise Figure
Cold Source","ENR"") scpi.Parse("disp:wind:trac1:feed "ENR"")
scpi.Parse("SENSe:FREQuency:STOP 8.5E+9") scpi.Parse("SYST:CAL:ALL:RESet")
scpi.Parse("syst:cal:all:sel 1") scpi.Parse("SYST:CAL:ALL:CSET:PREFix "test"")
scpi.Parse("syst:cal:all:chan1:port:sel 1,2")
scpi.Parse("syst:cal:all:mcl:prop:val "Receiver Characterization Method","Use
Noise Source"") scpi.Parse("syst:cal:all:mcl:prop:val "USB Noise
Source","U1831C MY12345678"") scpi.Parse("syst:cal:all:mcl:prop:val "Noise
Source Connector","APC 3.5 female"") scpi.Parse("syst:cal:all:mcl:prop:val
"Noise Source CalKit","85052D"") scpi.Parse("syst:cal:all:mcl:prop:val
"Include Power Calibration","false"") scpi.Parse("SYST:CAL:ALL:GUID:CHAN?")
scpi.Parse("SENS200:CORR:COLL:GUID:CONN:PORT1 'APC 3.5 male'")
scpi.Parse("SENS200:CORR:COLL:GUID:CONN:PORT2 'APC 3.5 female'")
scpi.Parse("SENS200:CORR:COLL:GUID:CKIT:PORT1 '85052D'")
scpi.Parse("SENS200:CORR:COLL:GUID:CKIT:PORT2 '85052D'")
scpi.Parse("SENS200:CORR:COLL:GUID:INIT")
scpi.Parse("SENS200:CORR:COLL:GUID:STEP?")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 1")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 2")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 3")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 4")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 5")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 6")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 7")
scpi.Parse("SENSe200:CORRection:COLLect:GUIDed:DESC? 8")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN1")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN2")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN3")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN4")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN5")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN6")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN7")
scpi.Parse("SENS200:CORR:COLL:GUID:ACQ STAN8")
scpi.Parse("sens200:corr:coll:guid:save")  
---


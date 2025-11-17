# Cal All - SMC

'\------------------------------------------ ' create a standard channel
'\------------------------------------------ DISPlay:WINDow1:STATE ON
CALC1:PARameter:DEFine:EXT "MyMeas", S21 DISPlay:WINDow1:TRACe1:FEED "MyMeas"
SENSe1:BANDwidth 700 SENSe1:FREQuency:CENTer 1ghz SENSe1:FREQuency:SPAN 1ghz
SENSe1:SWEep:POINts 11 '\------------------------------------------ ' create a
Mixer channel '\------------------------------------------
DISPlay:WINDow2:STATE ON CALC2:CUST:DEF 'My SC21', 'Scalar Mixer/Converter',
'SC21' DISP:WIND2:TRAC:FEED 'My SC21' SENS2:SWEep:POINts 11 SENS2:BANDwidth
1e3 SENS2:MIX:INPut:FREQ:MODE SWEPt SENS2:MIX:INPut:FREQ:STAR 3.6e9
SENS2:MIX:INPut:FREQ:STOP 3.9e9 SENS2:MIX:LO:FREQ:MODE FIXED
SENS2:MIX:LO:FREQ:FIX 1.0e9 SENS2:MIX:LO:POW 10 SENS2:MIX:OUTP:FREQ:SID LOW
SENS2:MIX:CALC Output SENS2:MIX:LO:NAME 'Port 3' SENS2:MIX:APPLY
'\------------------------------------------ ' configure cal all
'\------------------------------------------ SYST:CAL:ALL:RESet
SYST:CAL:ALL:SEL 1,2 SYST:CAL:ALL:IFBW 1e3 SYST:CAL:ALL:PORT1:SOUR:POWer -10
SYST:CAL:ALL:CSET:PREFix 'MyCalAllExample'
'\----------------------------------------------------- ' query for the
available mixer cal properties to set ' this is an info only query
'\-----------------------------------------------------
SYST:CAL:ALL:MCL:PROP:NAME:CAT? 'Scalar Mixer/Converter'
SYST:CAL:ALL:MCL:PROP:VAL:CAT? 'Phase Correction Method'
SYST:CAL:ALL:MCL:PROP:VAL:CAT? 'Mixer Delay'
'\------------------------------------------------------------- ' Enable phase
correction using a cal mixer with known delay
'\-------------------------------------------------------------
SYST:CAL:ALL:MCL:PROP:VAL 'Enable Phase Correction','true'
SYST:CAL:ALL:MCL:PROP:VAL 'Phase Correction Method','Use Mixer Delay'
SYST:CAL:ALL:MCL:PROP:VAL 'Mixer Delay', '10e-9'
'\------------------------------------------------------------- ' configure
power sensor '\-------------------------------------------------------------
SYST:COMM:PSEN USB, "Agilent Technologies,U8485A,my53470003"
'\------------------------------------------------------------- ' Perform
calibration '\-------------------------------------------------------------
SYST:CAL:ALL:GUIDed:CHAN? SENS200:corr:coll:guid:conn:port1 "APC 3.5 male"
SENS200:corr:coll:guid:conn:port2 "APC 3.5 female"
SENS200:corr:coll:guid:conn:port3 "Not used" SENS200:corr:coll:guid:conn:port4
"Not used" SENS200:corr:coll:guid:ckit:port1 "N4691-60004 ECal"
SENS200:corr:coll:guid:ckit:port2 "N4691-60004 ECal"
SENS200:corr:coll:guid:init SENS200:corr:coll:guid:steps?
SENS200:corr:coll:guid:acq stan1 SENS200:corr:coll:guid:acq stan2
SENS200:CORR:COLL:GUID:desc? 3 SENS200:corr:coll:guid:acq stan3
SENS200:CORR:COLL:GUID:SAVE  
---  
  
The channel number used for the SENSe header is determined by the
SYST:CAL:ALL:GUID:CHAN? command. You must query this channel number  do not
assume that it will always be a particular value.


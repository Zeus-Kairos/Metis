# CALulate:TDR Commands

These commands control the setup and execution of TDR measurements.

CALCulate:TDR ALLocate DEEM | BPOT:FILename | BPOR:STATe | LENGth | PORT:FILename | PORT:STATe | STATe DEVice EMPHasis | CURSor | POST1 | POST2 | PRE1 | STATe EQUalization | CTLE | DC | POLE1 | POLE2 | ZERO1 | FILename | STATe | TYPE EYE | EXECute | INPut | BPATtern | LENGth | TYPE | DRATe | JITTer | DLIMit | PERiodic | FREQuency | MAGNitude | RANDom | MAGNitude | STATe | TYPE | OLEVel | RTIMe | DATA | THReshold | ZLEVel | MASK | FAIL? | STATe | RESults | DATA? | DISPlay | STATe | THReshold | STATe MEASure | ACTive | MARKer | DTIMe | DATA? | POSition | STATe | TARGet | FORMat | MARKer | REFerence | STATe | STATe | PARameter | PEELing | STATe | SMOothing | STATe | TIME | COUPle | IMPulse | WIDTh | STEP | RTIMe | THReshold | COUPle | TYPE | TTIMe | DATA | STATe | THReshold TIME | STEP | AMPLitude  
---  
  
Click on a red keyword to view the command details.

See Also

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## CALCulate<cnum>:TDR:ALLocate <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the type of parameter and format allocation for each trace.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Parameters to display. Choose from: SPARameters \- Display all S-parameter data. TPARameters \- Display all Time domain data. MIXed \- Display a mix of commonly measured time-domain and S-parameter data.  
Examples |  CALC:TDR:ALL SPAR  
calculate2:tdr:allocate sparameters  
Query Syntax |  CALCulate<cnum>:TDR:ALLocate?  
Return Type |  String  
Default |  MIXed  
  
* * *

## CALCulate<cnum>:TDR:DEVice <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the DUT topology.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Topology. Choose from: SEND1 \- Single-ended, 1-port. SEND2 \- Single-ended, 2-port. DIF1 \- Differential, 1-port. SEND4 \- Single-ended, 4-port. DIF2 \- Differential, 2-port.  
Examples |  CALC:TDR:DEV SEND2  
calculate2:tdr:device:send2  
Query Syntax |  CALCulate<cnum>:TDR:DEVice?  
Return Type |  String  
Default |  SEND1  
  
* * *

## CALCulate<cnum>:TDR:DEEM:BPOR<pnum>:FILename <file>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the filename of the s4p de-embedding user file.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<pnum> |  Port number for balance port. If unspecified, <pnum> is set to 1.  
<file> |  File Name. This file is saved as a 4-port touchstone file with the .s4p extensions.  
Examples |  CALC:TDR:DEEM:BPOR1:FIL "test.s4p"  
calculate2:tdr:deem:bport2:filename "test.s4p"  
Query Syntax |  CALCulate<cnum>:TDR:DEEM:BPOR<pnum>:FILename?  
Return Type |  String  
Default |  " " (Empty String)  
  
* * *

## CALCulate<cnum>:TDR:DEEM:BPOR<pnum>:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets s4p de-embedding function state ON/OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<pnum> |  Port number for balance port. If unspecified, <pnum> is set to 1.  
<bool> |  ON or 1 \- Turns s4p de-embedding function ON.  
OFF or 0 \- Turns s4p de-embedding function OFF.  
Examples |  CALC:TDR:DEEM:BPOR1:STAT ON  
calculate2:tdr:deem:bport2:state off  
Query Syntax |  CALCulate<cnum>:TDR:DEEM:BPOR<pnum>:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:DEEM:LENGth

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the approximate fixture length  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Approximate fixture length (range: 0 to max DUT length)  
Examples |  CALC:TDR:DEEM:LENG 1.5e-9  
calculate2:tdr:deem:length 1.3e-9  
Query Syntax |  CALCulate<cnum>:TDR:DEEM:LENGth?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:DEEM:PORT<pnum>:FILename <file>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the filename of the s2p de-embedding user file.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<pnum> |  Port number. If unspecified, <pnum> is set to 1.  
<file> |  File Name. This file is saved as a 2-port touchstone file with the .s2p extensions.  
Examples |  CALC:TDR:DEEM:PORT1:FIL "test.s2p"  
calculate2:tdr:deem:port2:filename "test.s2p"  
Query Syntax |  CALCulate<cnum>:TDR:DEEM:PORT<pnum>:FILename?  
Return Type |  String  
Default |  " " (Empty String)  
  
* * *

## CALCulate<cnum>:TDR:DEEM:PORT<pnum>:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets s2p de-embedding function state ON/OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<pnum> |  Port number. If unspecified, <pnum> is set to 1.  
<bool> |  ON or 1 \- Turns s2p de-embedding function ON.  
OFF or 0 \- Turns s2p de-embedding function OFF.  
Examples |  CALC:TDR:DEEM:PORT1:STAT ON  
calculate2:tdr:deem:port2:state off  
Query Syntax |  CALCulate<cnum>:TDR:DEEM:PORT<pnum>:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:DEEM:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets de-embedding function state ON/OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns de-embedding function ON.  
OFF or 0 \- Turns de-embedding function OFF.  
Examples |  CALC:TDR:DEEM:STAT ON  
calculate2:tdr:deem:state off  
Query Syntax |  CALCulate<cnum>:TDR:DEEM::STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:EMPHasis:CURSor:POST1 <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the emphasis post1 level.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Post1 level value. The range is -20 dB to +20 dB.  
Examples |  CALC:TDR:EMPH:CURS:POST1 3  
calculate2:tdr:emphasis:cursor:post1 3  
Query Syntax |  CALCulate<cnum>:TDR:EMPHasis:CURSor:POST1?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:EMPHasis:CURSor:POST2 <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the emphasis post2 level.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Post2 level value. The range is -20 dB to +20 dB.  
Examples |  CALC:TDR:EMPH:CURS:POST2 3  
calculate2:tdr:emphasis:cursor:post2 3  
Query Syntax |  CALCulate<cnum>:TDR:EMPHasis:CURSor:POST2?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:EMPHasis:CURSor:PRE1 <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the emphasis pre1 level.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Pre1 level value. The range is -20 dB to +20 dB.  
Examples |  CALC:TDR:EMPH:CURS:PRE1 2  
calculate2:tdr:emphasis:cursor:pre1 2  
Query Syntax |  CALCulate<cnum>:TDR:EMPHasis:CURSor:PRE1?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:EMPHasis:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
emphasis function state ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns emphasis ON.  
OFF or 0 \- Turns emphasis OFF.  
Examples |  CALC:TDR:EMPH:STAT ON  
calculate2:tdr:emphasis:state off  
Query Syntax |  CALCulate<cnum>:TDR:EMPHasis:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:CTLE:DC <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the equalization CTLE (Continuous Time Linear Equalization) DC gain
parameter.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  CTLE value. The range is 0 to 10.  
Examples |  CALC:TDR:EQU:CTLE:DC 0.077  
calculate2:tdr:equalization:ctle:dc 0.077  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:CTLE:DC?  
Return Type |  Double  
Default |  0.667  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:CTLE:POLE1 <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the equalization CTLE (Continuous Time Linear Equalization) Pole1
parameter.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  CTLE value. The range is 0 to 76E9 in Hz.  
Examples |  CALC:TDR:EQU:CTLE:POLE1 2E9  
calculate2:tdr:equalization:ctle:pole1 2e9  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:CTLE:POLE1?  
Return Type |  Double  
Default |  1.95E9  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:CTLE:POLE2 <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the equalization CTLE (Continuous Time Linear Equalization) Pole2
parameter.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  CTLE value. The range is 0 to 76E9 in Hz.  
Examples |  CALC:TDR:EQU:CTLE:POLE2 2E9  
calculate2:tdr:equalization:ctle:pole2 2e9  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:CTLE:POLE2?  
Return Type |  Double  
Default |  5E9  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:CTLE:ZERO1 <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the equalization CTLE (Continuous Time Linear Equalization) zero
parameter.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  CTLE value. The range is 0 to 76E9 in Hz.  
Examples |  CALC:TDR:EQU:CTLE:ZERO1 650E6  
calculate2:tdr:equalization:ctle:zero1 650e6  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:CTLE:ZERO1?  
Return Type |  Double  
Default |  650E6  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:FILename <file>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the filename of the equalization equation user file. It is necessary to
select the file using CALCulate:TDR:EQUalization:TYPE and turn ON the
:CALCulate:TDR:EQUalization:STATe. This file is saved with .csv extension.
Specify the file name with the extension. When you use directory names (folder
names) and file name, separate them with "\ " (back slash), or "/" (slash).  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<file> |  Filename up to 254 characters.  
Examples |  CALC:TDR:EQU:FIL "C:\folder\User.csv"  
calculate2:tdr:equalization:filename "C:\folder\User.csv"  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:FILename?  
Return Type |  String  
Default |  " " (Empty String)  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
equalization function state ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns equalization ON.  
OFF or 0 \- Turns equalization OFF.  
Examples |  CALC:TDR:EQU:STAT ON  
calculate2:tdr:equalization:state off  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:EQUalization:TYPE <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the equalization type.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Equalization type. Choose from: EQUation \- Option to enter values for equation calculation. USER \- Load user file.  
Examples |  CALC:TDR:EQU:TYPE EQU  
calculate2:tdr:equalization:type equation  
Query Syntax |  CALCulate<cnum>:TDR:EQUalization:TYPE?  
Return Type |  Double  
Default |  EQUation  
  
* * *

## CALCulate<cnum>:TDR:EYE:EXECute

Applicable Models: All with TDR Options (S9x011A/B) (Write-only) This command
performs the calculation for the simulated eye diagram for the active trace.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Example |  CALC:TDR:EYE:STAT ON  
CALC:PAR:MNUM:SEL 3  
CALC:TDR:EYE:EXEC  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:BPATtern:LENGth <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the bits' power of 2 for a PRBS pattern. This value is used only when the
selected bit pattern type is PRBS.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Bit pattern power of 2. The range is 3 to 15 (resolution is 1).  
Examples |  CALC:TDR:EYE:INP:BPAT:TYPE PRBS  
CALC:TDR:EYE:INP:BPAT:LENG 7  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:BPATtern:LENGth?  
Return Type |  Integer  
Default |  7  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:BPATtern:TYPE <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the bit pattern type for the simulated eye function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Eye pattern type. Choose from: PRBS \- Pseudo-Random Bit Sequence. K285 \- K 28.5. USER \- Custom user-defined pattern. STAT \- Statistical calculation.  
Examples |  CALC:TDR:EYE:INP:BPAT:TYPE K285  
calculate2:tdr:eye:input:bpattern:type k285  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:BPATtern:TYPE?  
Return Type |  String  
Default |  PRBS  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:DRATe <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the bit rate in bits/sec for the simulated eye function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Bit rate in bits/sec. The range is 1.21M to 60.8G.  
Examples |  CALC:TDR:EYE:INP:DRAT 1.1E9  
calculate2:tdr:eye:input:drate 1.1e9  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:DRATe?  
Return Type |  Double  
Default |  1G  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:JITTer:DLIMit <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the display limit value.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Display limit value. The range is 0 to 1.  
Examples |  CALC:TDR:EYE:INP:JITT:DLIM 0  
calculate2:tdr:eye:input:jitter:dlimit 0  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:JITTer:DLIMit?  
Return Type |  Double  
Default |  1-E-9  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:JITTer:PERiodic:FREQuency <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the periodic jitter frequency. This value is used only when the periodic
jitter function type is selected.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Periodic jitter frequency in Hz. The range is 0 to TDR eye jitter max frequency.  
Examples |  CALC:TDR:EYE:INP:JITT:PER:FREQ 0  
calculate2:tdr:eye:input:jitter:periodic:frequency 0  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:JITTer:PERiodic:FREQuency?  
Return Type |  Double  
Default |  500E3  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:JITTer:PERiodic:MAGNitude <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the periodic jitter magnitude in rms. This value is used only when
periodic jitter function type is selected.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Periodic jitter magnitude. The range is 0 to 1 UI.  
Examples |  CALC:TDR:EYE:INP:JITT:TYPE:PER  
CALC:TDR:EYE:INP:JITT:PER:MAGN 0.5  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:JITTer:PERiodic:MAGNitude?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:JITTer:RANDom:MAGNitude <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the random jitter magnitude in rms. This value is used only when random
jitter function type is selected.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Random jitter magnitude. The range is 0 to 0.25 UI.  
Examples |  CALC:TDR:EYE:INP:JITT:TYPE:RAND  
CALC:TDR:EYE:INP:JITT:RAND:MAGN 0.05  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:JITTer:RANDom:MAGNitude?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:JITTer:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
jitter function state with simulated eye ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns jitter ON.  
OFF or 0 \- Turns jitter OFF.  
Examples |  CALC:TDR:EYE:INP:JITT:STAT ON  
calculate2:tdr:eye:input:jitter:state off  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:JITTer:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:JITTer:TYPE <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the jitter function type for the simulated eye function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Jitter type. Choose from: RANDom \- Random jitter function. PERiodic \- Periodic jitter function.  
Examples |  CALC:TDR:EYE:INP:JITT:TYPE RAND  
calculate2:tdr:eye:input:jitter:type random  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:JITTer:TYPE?  
Return Type |  String  
Default |  PERiodic  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:OLEVel <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the voltage level for bit "1" for the simulated eye function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Level for bit "1". The range is -5 V to +5 V.  
Examples |  CALC:TDR:EYE:INP:OLEV 100E-3  
calculate2:tdr:eye:input:olevel 100e-3  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:OLEVel?  
Return Type |  Double  
Default |  0.2  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:RTIMe:DATA <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the rise time value for the simulated eye function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Rise time for simulated eye function in seconds.  
Examples |  CALC:TDR:EYE:INP:RTIM:DATA 90E-12  
calculate2:tdr:eye:input:rtime:data 90e-12  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:RTIMe:DATA?  
Return Type |  Double  
Default |  35E-12  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:RTIMe:THReshold <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the rise time threshold for the simulated eye.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Threshold levels. Choose from: T1_9 \- 10% to 90%. T2_8 \- 20% to 80%.  
Examples |  CALC:TDR:EYE:INP:RTIM:THR T1_9  
calculate2:tdr:eye:input:rtime:threshold t1_9  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:RTIMe:THReshold?  
Return Type |  String  
Default |  T1_9  
  
* * *

## CALCulate<cnum>:TDR:EYE:INPut:ZLEVel <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the voltage level for bit "0" for the simulated eye function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Voltage level for bit "0". The range is -5 V to +5 V.  
Examples |  CALC:TDR:EYE:INP:ZLEV 100E-3  
calculate2:tdr:eye:input:zlevel 100e-3  
Query Syntax |  CALCulate<cnum>:TDR:EYE:INPut:ZLEVel?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:EYE:MASK:FAIL?

Applicable Models: All with TDR Options (S9x011A/B) (Read-only) This command
returns the mask test result.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples |  CALC:TDR:EYE:MASK:FAIL?  
calculate2:tdr:eye:mask:fail?  
Return Type |  Boolean ON or 1 \- Mask test fail.  
OFF or 0 \- Mask test pass.  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:TDR:EYE:MASK:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
mask test function state with simulated eye ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns mask test ON.  
OFF or 0 \- Turns mask test OFF.  
Examples |  CALC:TDR:EYE:MASK:STAT ON  
calculate2:tdr:eye:mask:state off  
Query Syntax |  CALCulate<cnum>:TDR:EYE:MASK:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:EYE:RESults:DATA?

Applicable Models: All with TDR Options (S9x011A/B) (Read-only) This command
returns the results of the eye measurement. There are 18 values returned. The
minimum and maximum values are returned in addition to the displayed results
(16 values) on the TDR application GUI.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples |  CALC:TDR:EYE:RESults:DATA?  
calculate2:tdr:eye:results:data?  
Return Type |  Variant Array  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:TDR:EYE:RESults:DISPlay:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
overlay ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns overlay ON.  
OFF or 0 \- Turns overlay OFF.  
Examples |  CALC:TDR:EYE:RES:DISP:STAT ON  
calculate2:tdr:eye:results:display:state off  
Query Syntax |  CALCulate<cnum>:TDR:EYE:RESulsts:DISPlay:STATe?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## CALCulate<cnum>:TDR:EYE:RESults:THReshold <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the rise time threshold level for the results of eye measurement.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Threshold levels. Choose from: T1_9 \- 10% to 90%. T2_8 \- 20% to 80%.  
Examples |  CALC:TDR:EYE:RES:THR T1_9  
calculate2:tdr:eye:results:threshold t1_9  
Query Syntax |  CALCulate<cnum>:TDR:EYE:RESults:THReshold?  
Return Type |  String  
Default |  T1_9  
  
* * *

## CALCulate<cnum>:TDR:EYE:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
Eye/Mask window ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns Eye/Mask window ON.  
OFF or 0 \- Turns Eye/Mask window OFF.  
Examples |  CALC:TDR:EYE:STAT ON  
calculate2:tdr:eye:state off  
Query Syntax |  CALCulate<cnum>:TDR:EYE:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:ACTive:MARKer <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets active marker number.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Marker number to activate. The range is 0 to 10.  
Examples |  CALC:TDR:MEAS1:ACT:MARK 1  
calculate2:tdr:measure1:active:marker 1  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:ACTive:MARKer?  
Return Type |  Integer  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:DATA?

Applicable Models: All with TDR Options (S9x011A/B) (Read-only) This command
returns the delta time result value. You can get the result even if
CALCulate:TDR:MEASure:DTIMe:STATe is off.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples |  CALC:TDR:MEAS1:DTIM:DATA?  
calculate2:tdr:measure1:dtime:data?  
Return Type |  Double  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:POSition <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets delta time reference position.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Delta time reference position. The range is 0 to 100.  
Examples |  CALC:TDR:MEAS1:DTIM:POS 0  
calculate2:tdr:measure1:dtime:position 0  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:POSition?  
Return Type |  Double  
Default |  50  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
delta time marker in the marker search ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns delta time marker ON.  
OFF or 0 \- Turns delta time marker OFF.  
Examples |  CALC:TDR:MEAS1:DTIM:STAT ON  
calculate2:tdr:measure1:dtime:state off  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:TARGet <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the target trace number for the delta time function. The MEASure[1-256]
is the trace number starting point for delta time. The <value> is the trace
number stopping point for delta time.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Trace number stopping point for delta time. The range is 1 to 16.  
Examples |  CALC:TDR:MEAS1:DTIM:TARG 5  
calculate2:tdr:measure1:dtime:target 5  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:DTIMe:TARGet?  
Return Type |  Integer  
Default |  1  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:FORMat <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the trace format.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Trace format. For S-Parameter measurements, choose from: MLINear MLOGarithmic PHASe UPHase IMAGinary REAL POLar SMITh SADMittance SWR GDELay KELVin| FAHRenheit CELSius PPHase IMPedance VOLT For Time Domain measurements, choose from: IMPedance VOLT MLOGarithmic MLINear REAL  
Examples |  CALC:TDR:MEAS1:FORM IMP  
calculate2:tdr:measure1:format impedance  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:FORMat?  
Return Type |  String  
Default |  MLINear  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:MARKer:REFerence[:STATe] <ON | OFF>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
reference marker ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<ON | OFF> |  ON (or 1) - turns reference marker ON OFF (or 0) - turns reference marker ON  
Examples |  CALC:TDR:MEAS1:MARK:REF ON  
calculate2:tdr:measure1:marker:reference:state OFF  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:MARKer:REFerence[:STATe]?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:MARKer<mkr>[:STATe] <ON|OFF>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) Turns the
specified marker ON or OFF.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mkr> |  Any marker number from 1 to 15; if unspecified, value is set to 1.  
<ON|OFF> |  ON (or 1) - turns marker ON. OFF (or 0) - turns marker OFF.  
Examples |  CALC:TDR:MEAS:MARK ON  
calculate2:tdr:measure2:marker8 on  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:MARKer<mkr>:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:PARameter <string>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the measurement parameter.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<sting> |  Measurement parameter. For S-Parameter measurements:: Sxy Sddxy Sdcxy Scdxy Sccxy X: 1 to 4 Y: 1 to 4 For Time Domain measurements: Txy Tddxy Tdcxy Tcdxy Tccxy  
Examples |  CALC:TDR:MEAS1:PAR T11  
calculate2:tdr:measure1:parameter t11  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:PARameter?  
Return Type |  String  
Default |  S11  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:PEELing:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets state for the peeling function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns peeling function ON.  
OFF or 0 \- Turns peeling function OFF.  
Examples |  CALC:TDR:MEAS1:PEEL:STAT ON  
calculate2:tdr:measure1:peeling:state off  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:PEELing:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:SMOothing:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets state for the smoothing function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns smoothing function ON.  
OFF or 0 \- Turns smoothing function OFF.  
Examples |  CALC:TDR:MEAS1:SMO:STAT ON  
calculate2:tdr:measure1:smoothing:state off  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:SMOothing:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TIME:IMPulse:WIDTh <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the impulse width value for the transform function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Transform function impulse width value.  
Examples |  CALC:TDR:MEAS1:TIME:IMP:WIDT 17E-12  
calculate2:tdr:measure1:time:impulse:width 17e-12  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:TIME:IMPulse:WIDTh?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TIME:STEP:COUPle <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
enables/disables rise time coupling.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns rise time coupling ON.  
OFF or 0 \- Turns rise time coupling OFF.  
Examples |  CALC:TDR:MEAS:TIME:STEP:COUP ON  
calculate2:tdr:meas:time:step:couple off  
Query Syntax |  CALCulate<cnum>:TDR:MEAS:TIME:STEP:COUPle?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TIME:STEP:RTIMe <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets rise time value for the transform function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Transform function rise time value in seconds.  
Examples |  CALC:TDR:MEAS1:TIME:STEP:RTIM 0  
calculate2:tdr:measure1:time:step:rtime 0  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:TIME:STEP:RTIMe?  
Return Type |  Double  
Default |  0  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TIME:STEP:RTIMe:THReshold <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the rise time threshold level for the results of eye measurement.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Transform function rise time threshold levels. Choose from: T1_9 \- 10% to 90%. T2_8 \- 20% to 80%.  
Examples |  CALC:TDR:MEAS1:TIME:STEP:RTIM:THR T1_9  
calculate2:tdr:measure1:time:step:rtime:threshold t1_9  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:TIME:STEP:RTIMe:THReshold?  
Return Type |  String  
Default |  T1_9  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TIME:TYPE <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the stimulus type for the transform function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Transform function stimulus type. Choose from: LPSTep \- Low pass step. LPIMpulse -Low pass impulse.  
Examples |  CALC:TDR:MEAS1:TIME:TYPE LPST  
calculate2:tdr:measure1:time:type lpstep  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:TIME:TYPE?  
Return Type |  String  
Default |  LPSTep  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TTIMe:DATA?

Applicable Models: All with TDR Options (S9x011A/B) (Read-only) This command
returns the rise time result value for marker search. You can get the data
even if CALCulate:TDR:MEASure:TTIMe:STATe is off.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
Examples |  CALC:TDR:MEAS1:TTIM:DATA?  
calculate2:tdr:measure1:ttime:data?  
Return Type |  Double  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TTIMe:STATe <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
displays the rise time marker.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns rise time marker ON.  
OFF or 0 \- Turns rise time marker OFF.  
Examples |  CALC:TDR:MEAS1:TTIM:STAT ON  
calculate2:tdr:measure1:ttime:state off  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:TTIMe:STATe?  
Return Type |  Boolean  
Default |  OFF  
  
* * *

## CALCulate<cnum>:TDR:MEASure[1-256]:TTIMe:THReshold <enum>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets the rise time threshold for the rise time in the marker search function.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<enum> |  Rise time threshold levels. Choose from: T1_9 \- 10% to 90%. T2_8 \- 20% to 80%.  
Examples |  CALC:TDR:MEAS1:TTIM:THR T1_9  
calculate2:tdr:measure1:ttime:threshold t1_9  
Query Syntax |  CALCulate<cnum>:TDR:MEASure[1-256]:TTIMe:THReshold?  
Return Type |  String  
Default |  T1_9  
  
* * *

## CALCulate<cnum>:TDR:TIME:COUPle <bool>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
enables/disables time coupling.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<bool> |  ON or 1 \- Turns time coupling ON.  
OFF or 0 \- Turns time coupling OFF.  
Examples |  CALC:TDR:TIME:COUP ON  
calculate2:tdr:time:couple off  
Query Syntax |  CALCulate<cnum>:TDR:TIME:COUPle?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## CALCulate<cnum>:TDR:TIME:STEP:AMPLitude <value>

Applicable Models: All with TDR Options (S9x011A/B) (Read-Write) This command
sets or gets the step amplitude value.  
---  
Parameters |   
<cnum> |  Channel number of the measurement. If unspecified, <cnum> is set to 1.  
<value> |  Step amplitude value in Hz, dBm, or seconds. The range is 0.001 to 5.  
Examples |  CALC:TDR:TIME:STEP:AMPL 200ms  
calculate2:tdr:time:step:amplitude .05s  
Query Syntax |  CALCulate<cnum>:TDR:TIME:STEP:AMPLitude?  
Return Type |  Double  
Default |  0.2  
  
* * *

##


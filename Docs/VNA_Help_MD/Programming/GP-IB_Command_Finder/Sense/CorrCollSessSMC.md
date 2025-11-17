# Sense:Correction:Collect:Session:SMC Commands - Superseded

* * *

Note: These commands (commonly known as "Session" commands) were replaced with
[Sens:Corr:Coll:Guid:SMC](CorrCollGuidSMC.md) commands .

Performs scalar (SMC) calibration on a frequency converting device.

SENSe:CORRection:COLLect:SESSion:SMC | ECAL | [CHARacterza](CorrCollSessSMC.md#ECAL_CHAR) | FSIMulator | NETWork | [FILename](CorrCollSessSMC.md#NetworkFilename) | [MODE](CorrCollSessSMC.md#NetworkMode) | [IMPort](CorrCollSessSMC.md#Import) | PHASe | [DELay](CorrCollSessSMC.md#PhaseDelay) | [METHod](CorrCollSessSMC.md#PhaseMethod) | [MIXer](CorrCollSessSMC.md#PhaseMixer) | PWRCal | [SEParate](CorrCollSessSMC.md#PwrCalSeparate) | [SRCPort](CorrCollSessSMC.md#SRCPort) | TWOPort | ECAL | ORIentation | [[STATe]](CorrCollSessSMC.md#TP_ECAL_ORIE_STAT) | [PORTmap](CorrCollSessSMC.md#map) | [METHod](CorrCollSessSMC.md#ecal_method) | [OMITisolat](CorrCollSessSMC.md#ECAL_OMIT) | [OPTion](CorrCollSessSMC.md#SENS_OPERation)  
---  
  
Click on a red keyword to view the command details.

Red keywords are obsolete.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about SMC Calibrations](../../../FreqOffset/SMC_Measurements.md#CalOverview)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

NOTE: To configure a power meter and sensor see
[SOURce:POWer:](../SourceCorrection.md) commands.

* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n >:SMC:ECAL:CHARacteriza <mod>
,<char>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Specifies the ECal
module and characterization to be used for the SMC calibration.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<mod> |  1 \- Electronic Calibration Module  
<char> |  Specifies which characterization within the ECal module from which to read the confidence data. 0 Factory characterization (data that was stored in the ECal module by Keysight). Default if not specified. 1 User characterization #1 2 User characterization #2 3 User characterization #3 4 User characterization #4 5 User characterization #5  
Examples |  SENS:CORR:COLL:SESS:SMC:ECAL:CHAR 1,2  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:ECAL:CHAR?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1,0  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n> :SMC:FSIMulator:NETWork<p>:FILename
<string>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Specifies the S2P
filename to embed or de-embed on the input or output of your mixer
measurement. [Learn more.](../../../FreqOffset/SMC_Measurements.md#Waveguide)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<p> |  Apply network to input or output of mixer. Choose from: 1 - Input of mixer 2 - Output of mixer  
<string> |  Filename of the S2P used for embedding or de-embedding. Use the full path name, file name, and .S2P suffix, enclosed in quotes.  
Examples |  SENS:CORR:COLL:SESS:SMC:FSIM:NETW1:FIL "c:\users\public\network analyzer\documents/WaveguideAdapt.S2P"  
Query Syntax |  SENS<ch>:CORRection:COLLect:SESSion<n> :SMC:FSIMulator:NETWork<x>:FILename?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:FSIMulator:NETWork<p>:MODE
<char>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Allows you to embed
(add) or de-embed (remove) circuit network effects on the input and output of
your mixer measurement. [Learn
more.](../../../FreqOffset/SMC_Measurements.htm#Waveguide)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<p> |  Apply network to input or output of mixer. Choose from: 1 - Input of mixer 2 - Output of mixer  
<char> |  Choose from: NONE \- Do nothing with effects of S2P file. EMBed \- Add effects of S2P file from the measurement results. DEEMbed \- Remove effects of S2P file from the measurement results.  
Examples |  SENS:CORR:COLL:SESS:SMC:FSIM:NETW1:MODE EMB  
Query Syntax |  SENS<ch>:CORRection:COLLect:SESSion<n> :SMC:FSIMulator:NETWork<x>:MODE?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:IMPort <calName>, <dataset>

Applicable Models: N522xB, N523xB, N524xB (Write-only) Imports existing Source
Power Cal data into the SMC calibration.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<calName> |  (String) Name of existing Cal Set from which power meter data is imported.  
<dataset> |  (String) Name of the data set. Use POWER_STEP  
Examples |  SENS2:CORR:COLL:SESS1:SMC:IMP "MyPowerCal", "POWER_STEP"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PHASe:DELay <num>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Set and return the
known delay through the calibration mixer. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<char> |  Known delay through the calibration mixer in seconds.  
Examples |  SENS:CORR:COLL:SESS:SMC:PHAS:DEL 12e-9 sense2:correction:collect:session2:smc:phase:delay 12e-10  
Query Syntax |  SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PHASe:DELay?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 seconds  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PHASe:METHod <char>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Set and return the
method of setting the delay through the calibration mixer. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<char> |  Choose from: FIXed - use a known delay value set with [SENS:CORR:COLL:SESS:SMC:PHAS:DEL](CorrCollSessSMC.md#PhaseDelay) MIXer \- use the S2P file set with [SENS:CORR:COLL:SESS:SMC:PHAS:MIX](CorrCollSessSMC.md#PhaseMixer)  
Examples |  SENS:CORR:COLL:SESS:SMC:PHAS:METH FIX sense2:correction:collect:session2:smc:phase:method mixer  
Query Syntax |  SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PHASe:METHod?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  FIXed  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PHASe:MIXer <string>

Applicable Models: N522xB, N523xB, N524xB (Write-only) Set the filename of the
S2P file used to characterize the calibration mixer. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<string> |  Calibration mixer filename. Use the following rules to specify path names:

  * The default folder is "c:\users\public\network analyzer\documents"
  * You can change the active directory using [MMEMory:CDIRectory](../Memory.md#chgdir).
  * Specify only the file name if using the active directory.
  * You can also use an absolute path name to specify the folder and file.

  
Examples |  SENS:CORR:COLL:SESS:SMC:PHAS:MIX "MyCalMixer.s2p" sense2:correction:collect:session2:smc:phase:mixer "MyCalMixer.s2p"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PWRCal:SEParate <bool>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Specifies whether to
use a Thru standard or to use two power sensor connections during the power
cal of an SMC calibration. This command must be sent BEFORE the
[INITiate](CorrCollSess.md#INIT) command and all the other calibration
commands.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<bool> |  OFF or 0 \- Perform Cal with Thru standard. ON or 1 \- Do NOT use a Thru, but instead perform separate power cals on Input and Output reference planes.  
Examples |  SENS:CORR:COLL:SESS:INIT "SMC"  
SENS:CORR:COLL:SESS:SMC:PWRC:SEP 1  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:PWRCal:SEParate?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 or OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:PWRCal:SRCPort <string>
Obsolete

(Read-Write) Specifies which port to calibrate. Note: Beginning with Rev 6.0,
this command is no longer necessary. Because of improved calibration
techniques, Both is always selected although a power meter measurement is
performed only on port 1.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<char> |  '1' Source port 1 (SMC forward direction) '2' Source port 2 (SMC reverse direction 'BOTH' (both forward and reverse directions)  
Examples |  SENS:CORR:COLL:SESS:SMC:PWRC:SRCP 'both'  
SENSe2:CORRection:COLLection:SESSion6:SMC:PWRCal:SRCPort '2'  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:PWRC:SRCP?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

##
SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:TWOPort:ECAL:ORIentation[:STATe]
<bool>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets ECAL Auto-
Orientation ON or OFF. If setting auto-orientation OFF, you must manually
specify the orientation of the ECAL module with
[SENS:CORR:COLL:SESS:SMC:TWOP:ECAL:PORTmap](CorrCollSessSMC.md#map).  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<bool> |  OFF or 0 = Orientation OFF ON or 1 = Orientation ON  
Examples |  SENS:CORR:COLL:SESS:SMC:TWOP:ECAL:ORI 1  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:TWOP:ECAL:ORI?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n>:SMC:TWOPort:ECAL:PORTmap <mod>,
<string>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Specifies the manual
orientation (which ports of the module are connected to which ports of the
VNA) when auto-orientation is OFF.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<mod> |  1 - Electronic Calibration Module  
<string> |  Format in the following manner: Aw,Bx,Cy,Dz where

  * A, B, C, and D are literal ports on the ECAL module
  * w,x,y, and z are substituted for VNA port numbers to which the ECAL module port is connected.

Ports of the module which are not used are omitted from the string. For
example, on a 4-port ECal module with

  * port A connected to VNA port 2
  * port B connected to VNA port 3
  * port C not connected
  * port D connected to VNA port 1

the string would be: A2,B3,D1 If either the receive port or source port (or
load port for 2-port cal) of the CALC:PAR:SELected measurement is not in this
string and orientation is OFF, an attempt to perform an ECal calibration will
fail.  
Examples |  SENS:CORR:COLL:SESS:SMC:TWOP:ECAL:PORTmap 1,'A1,B2'  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:TWOP:ECAL:PORTmap?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  "A1,B2"  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n >:SMC:TWOPort:METHod <string>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Specifies the guided
ECal method for performing the thru portion of the calibration.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<string> |  ECAL Method: Choose from: 'DEFAULT' \- Default 'ADAP' \- Adapter removal 'FLUSH' \- Flush Through 'UNKN' \- Unknown Thru  
Examples |  SENS:CORR:COLL:SESS:SMC:TWOPort:METH 'default'  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:TWOPort:METH?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  DEFAULT  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n >:SMC:TWOPort:OMITisolat <bool>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Select to omit or
perform the isolation portion of the ECAL.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<bool> |  ON or 1 \- Omit isolation OFF or 0 \- Perform isolation  
Examples |  SENS:CORR:COLL:SESS:SMC:TWOPort:OMIT 1  
Query Syntax |  SENS:CORR:COLL:SMC:TWOPort:OMIT?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  1  
  
* * *

## SENSe<ch>:CORRection:COLLect:SESSion<n >:SMC:TWOPort:OPTion <string>

Applicable Models: N522xB, N523xB, N524xB (Read-Write) Sets the SMC
calibration to ECAL or MECHanical  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  Session number of the calibration. [Learn about Cal sessions.](CorrCollSess.md)  
<char> |  Choose from: 'ECAL' Electronic Calibration Module - Note: This selection assumes there is only one ECal module on the USB and so it selects the first enumerated module on the bus, and the factory characterization on that ECal module, to be used for the cal. 'MECH' Mechanical Calibration Kit  
Examples |  SENS:CORR:COLL:SESS:SMC:TWOPort:OPTion 'ECAL'  
Query Syntax |  SENS:CORR:COLL:SESS:SMC:TWOPort:OPTion?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ECAL  
  
* * *


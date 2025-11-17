# Sense:Correction:Collect:Guided:SMC Commands

* * *

These commands, along with the standard [Guided commands](CorrGuided.md),
performs a SMC calibration on a frequency converting device.

Note: These commands replace the
[SENSe:CORRectionCOLLect:Session:SMC](CorrCollSessSMC.md) commands. These
commands allow the entire SMC cal to be performed from the Guided cal
interface.

These commands are also used to perform a [GCx
Calibration](../../../Applications/Gain_Compression_for_Converters.htm#GCXCal).
[See an
example](../../GPIB_Example_Programs/Create_and_Cal_a_GCX_Measurement.htm).

SENSe:CORRection:COLLect:GUIDed:SMC FSIMulator | NETWork | FILename | MODE IMPort [LO:PCAL[:STATe]](CorrCollGuidSMC.md#LOPwrCal) PHASe | DELay | METHod | MIXer PWRCal | [CANCel](CorrCollGuidSMC.md#PwrCalCancel) | [RECeiver](CorrCollGuidSMC.md#PwrCalReceiver) | SEParate  
---  
  
Click on a red keyword to view the command details.

Red keywords are obsolete.

See Also

  * [All GUIDed commands](CorrGuided.md)

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Learn about SMC Calibrations](../../../FreqOffset/SMC_Measurements.md#CalOverview)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

NOTE: To configure a power meter and sensor see
[SOURce:POWer:](../SourceCorrection.md) commands.

* * *

## SENSe<ch>:CORRection:COLLect:GUIDed :SMC:FSIMulator:NETWork<p>:FILename
<string>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Read-Write)
Specifies the S2P filename to embed or de-embed on the input or output of your
mixer measurement. [Learn
more.](../../../FreqOffset/SMC_Measurements.htm#Waveguide)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<p> |  Apply network to input or output of mixer. Choose from: 1 - Input of mixer 2 - Output of mixer  
<string> |  Filename of the S2P used for embedding or de-embedding. Use the full path name, file name, and .S2P suffix, enclosed in quotes.  
Examples |  SENS:CORR:COLL:GUID:SMC:FSIM:NETW1:FIL "D:\WaveguideAdapt.S2P"  
Query Syntax |  SENS<ch>:CORRection:COLLect:GUIDed:SMC:FSIMulator:NETWork<x>:FILename?  
Return Type |  String  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:FSIMulator:NETWork<p>:MODE <char>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Read-Write)
Allows you to embed (add) or de-embed (remove) circuit network effects on the
input and output of your mixer measurement. [Learn
more.](../../../FreqOffset/SMC_Measurements.htm#Waveguide)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<p> |  Apply network to input or output of mixer. Choose from: 1 - Input of mixer 2 - Output of mixer  
<char> |  Choose from: NONE \- Do nothing with effects of S2P file. EMBed \- Add effects of S2P file from the measurement results. DEEMbed \- Remove effects of S2P file from the measurement results.  
Examples |  SENS:CORR:COLL:GUID:SMC:FSIM:NETW1:MODE EMB  
Query Syntax |  SENS<ch>:CORRection:COLLect:GUIDed:SMC:FSIMulator:NETWork<x>:MODE?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:IMPort <calName>, <dataset>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Write-only)
Imports Guided Power Cal or Phase Reference Cal into the current SMC
calibrations. For the Guided Power Cal: The port of the mixer input must have
the same source attenuator setting between the SMC channel and the Guided
Power Cal Set. The frequencies of the Guided Power Cal must include all the
mixer frequencies. Interpolation will be applied to the Guided Power Cal
frequencies if they do not exactly match. For the Phase Reference Cal: The
port of the mixer input must have the same source attenuator setting as used
in the phase reference cal. The phase reference cal must include all the mixer
frequencies. Interpolation will be applied to the phase reference cal
frequencies if they do not exactly match. [Learn more about Phase Reference
Cal](../../../FreqOffset/Phase_Reference_Calibration.htm). The following error
message may appear (it is not written to the VNA Error Log):

  * Interpolation target is out of range. Cannot interpolate when incompatible frequency ranges occur.

  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<calName> |  (String) Name of existing Cal Set from which to import power data.  
<dataset> |  (String) Name of the data set. Choose from:

  * POWER_STEP -Iimport the Guided Power Cal data.
  * "POWER_AND_PHASE" \- Import the Phase Reference + power cal data. When this command is sent, the SMC Cal Method is automatically set to Use Phase Reference Cal. [Learn more](../../../FreqOffset/SMC_plus_Phase.md#SMCCalSetup). There is no other command to set this.

  
Examples |  SENS2:CORR:COLL:GUID:SMC:IMP "MyPowerCal","POWER_STEP" [See example program](../../GPIB_Example_Programs/Use_an_Existing_Power_Cal_During_an_SMC_Cal.md) SENS:CORR:COLL:GUID:SMC:IMP "MyPhaseRefCal","POWER_AND_PHASE" [See example program](../../GPIB_Example_Programs/Create_and_Cal_an_SMC_Measurement.md)  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:LO<n>:PCAL[:STATe] <bool>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Read-Write)
Sets and returns whether or not the LO power cal step is included in the cal
steps when an SMC or GCx cal is performed. [Learn
more.](../../../Applications/Gain_Compression_for_Converters.htm#GCXCal) Set
LO Power level for the calibration using
[SENS:CORR:COLL:GUID:PSEN1:POW:LEV](CorrCollGuidPSens.md#PsenPowLevel).  
---  
Parameters |   
<cnum> |  Any existing channel number; if unspecified, value is set to 1.  
<n> |  LO Stage. Choose 1.  
<bool> |  LO Power Cal state. Choose from: O or OFF \- Skips over the LO Power Cal when calibrating. 1 or ON \- Includes a step for LO Power Cal when calibrating  
Examples |  SENS:CORR:COLL:GUID:SMC:LO1:PCAL 0  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:SMC:LO<n>:PCAL[:STATe]  
Return Type |  Boolean  
Default |  OFF or 0  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PHASe:DELay <num>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Excepts
M9485A) (Read-Write) Set and return the known delay through the calibration
mixer. [Learn more.](../../../FreqOffset/SMC_plus_Phase.md)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<char> |  Known delay through the calibration mixer in seconds.  
Examples |  SENS:CORR:COLL:GUID:SMC:PHAS:DEL 12e-9 sense2:correction:collect:guided:smc:phase:delay 12e-10  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PHASe:DELay?  
Return Type |  Numeric  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  0 seconds  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PHASe:METHod <char>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Excepts
M9485A) (Read-Write) Set and return the method of setting the delay through
the calibration mixer. [Learn
more.](../../../FreqOffset/SMC_plus_Phase.htm#SMCPhase) To select Phase
Reference Cal method for correcting an SMC+Phase measurement, use
[SENS:CORR:COLL:GUID:SMC:IMPort](CorrCollGuidSMC.md#Import)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<char> |  Choose from: FIXed - use a known delay value set with SENS:CORR:COLL:GUID:SMC:PHAS:DEL MIXer \- use the S2P file set with SENS:CORR:COLL:GUID:SMC:PHAS:MIX  
Examples |  SENS:CORR:COLL:GUID:SMC:PHAS:METH FIX sense2:correction:collect:guided:smc:phase:method mixer  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PHASe:METHod?  
Return Type |  Character  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  FIXed  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PHASe:MIXer <string>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Excepts
M9485A) (Write-only) Set the filename of the S2P file used to characterize the
calibration mixer. [Learn more.](../../../FreqOffset/SMC_plus_Phase.md)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<string> |  Calibration mixer filename. Use the following rules to specify path names:

  * The default folder is "D:\"
  * You can change the active directory using [MMEMory:CDIRectory](../Memory.md#chgdir).
  * Specify only the file name if using the active directory.
  * You can also use an absolute path name to specify the folder and file.

  
Examples |  SENS:CORR:COLL:GUID:SMC:PHAS:MIX "MyCalMixer.s2p" sense2:correction:collect:guided:smc:phase:mixer "MyCalMixer.s2p"  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PWRCal:CANCel

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Write-only)
Aborts a power cal. This command should be sent when a power cal is running.  
---  
Parameters |   
<ch> |  Channel number of the SMC cal being performed. If unspecified, value is set to 1  
Examples |  SENS:CORR:COLL:GUID:SMC:PWRC:CANC  
Query Syntax |  Not Applicable  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PWRCal:RECeiver <bool>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Read-Write)
Set whether to use the reference receiver for faster iteration during power
cal or use a power meter.  This command should be set during calibration
setup. [Learn more](../../../S3_Cals/PwrCalibration.md#spcOptionsIm).  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  OFF or 0 \- Use a power meter only. ON or 1 \- Use a power meter for the first reading and the reference receiver for all subsequent readings.  
Examples |  SENS:CORR:COLL:GUID:SMC:PWRC:REC 1  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PWRCal:RECeiver?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  ON or 1  
  
* * *

## SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PWRCal:SEParate <bool>

Applicable Models: All with SMC Options (S9x082A/B, S9x083A/B) (Read-Write)
Specifies whether to use a Thru standard or to use two power sensor
connections during the power cal of an SMC calibration. Note: This command
must be sent BEFORE ALL other calibration commands.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<bool> |  OFF or 0 \- Perform Cal with Thru standard. ON or 1 \- Do NOT use a Thru, but instead perform separate power cals on Input and Output reference planes.  
Examples |  **' The following is an example sequence of commands:** **SENS:CORR:COLL:GUID:SMC:PWRC:SEP 1** SENS:CORR:COLL:GUID:CONN:PORT1 "APC 3.5 female" SENS:CORR:COLL:GUID:CONN:PORT2 "APC 3.5 female" SENS:CORR:COLL:GUID:CONN:PORT3 "Not used" SENS:CORR:COLL:GUID:CONN:PORT4 "Not used" SENS:CORR:COLL:GUID:CKIT:PORT1 "N4691-60006 ECal 02638" SENS:CORR:COLL:GUID:CKIT:PORT2 "N4691-60006 ECal 02638" SENS:CORR:COLL:GUID:INIT  
Query Syntax |  SENSe<ch>:CORRection:COLLect:GUIDed:SMC:PWRCal:SEParate?  
Return Type |  Boolean  
[ Default ](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) |  OFF or 0  
  
* * *


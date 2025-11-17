# Sense:Correction Commands

* * *

Performs and applies calibration and other error correction features.

  * To perform a Guided Calibration, use ONLY the [Sens:Corr Coll:GUIDed](CorrGuided.md) commands.

  * To perform an Unguided Calibration, do NOT use the Sens:Corr:Coll:Guided commands.

  * See the ["Unguided" example programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md) for clarification.

SENSe:CORRection [CACHe:MODE](Sense_Correction.md#CacMode) CCHeck | [[:ACQuire]](Sense_Correction.md#chkAcq) | [DONE](Sense_Correction.md#chkDone) | [PARameter](Sense_Correction.md#chkPar) [CKIT - More Commands](CorrCKIT_SCPI.md) COLLect | [[:ACQuire]](Sense_Correction.md#scca) | [APPLy](Sense_Correction.md#apply) | [CKIT - More Commands](CorrCollCKIT.md) | DISPlay:WINDow | [AOFF](Sense_Correction.md#CalWindowAoff) | [[:STATe]](Sense_Correction.md#CalWindowState) | [GUIDed - More Commands](CorrGuided.md) | IDLE | TRIGger | ISOLation: | [AVER:INCRement](Sense_Correction.md#IsolAvg) | [ECAL[:STATe]](Sense_Correction.md#IsoEcal) | LEAKage - [More Commands](CorrCollLeak.md) | [METHod](Sense_Correction.md#sccm) | NOISe | [ENR:ADAP:DEEMbed[:STATe]](Sense_Correction.md#NoiseENRDeemb) | [LO:PCAL[:STATe]](Sense_Correction.md#NoiseLOPCAl) | [PSEN:ADAP:DEEMbed[:STATe]](Sense_Correction.md#NoisePsenDeem) | RECeiver:PULL[:STATe] | THRU:ADAPter:DEEMbed[:STATe] | [SAVE](Sense_Correction.md#sccs) | [SESSion - More Commands](CorrCollSess.md) | SWEep:CHANnel | [AOFF](Sense_Correction.md#CalWindowSweepAoff) | [[:STATe]](Sense_Correction.md#CalWinSweepChan) [CSET - More Commands](CorrCset.md) ENR:CALibration:TABLe | [DATA](Sense_Correction.md#ENRData) | [ID:DATA](Sense_Correction.md#EnrID) | [SERial:DATA](Sense_Correction.md#EnrSerial) | TEMPerature:DATA [EXTension - More Commands](CorrExtension.md) GCSetup | [POWer](Sense_Correction.md#GCSPower) | SENSor: | [CKIT](Sense_Correction.md#GCSCkit) | [CONNector](Sense_Correction.md#GCSConnector) [IMD - More Commands](Corr_IMD.md) IMPedance:INPut | [MAGNitude](Sense_Correction.md#imped) [INTerpolate[:STATe]](Sense_Correction.md#scis) [ISOLation[:STATe]](Sense_Correction.md#sciss) LEAKage[:STATe] METHods | [MATCh](Sense_Correction.md#methodsMatch) | PORT | SUBSet | FULL[:VALue] | RESet | RESPonse[:VALue] | [:STATe] | [SA:PORT](Sense_Correction.md#MethSAPort) [MODel](Sense_Correction.md#Model) PREFerence | CALibration | [[:FOM]:RANGe](Sense_Correction.md#PrefCalFOM) | CSET | [SAVE](Sense_Correction.md#CsetSave) | [SAVUser](Sense_Correction.md#Savuser) | ECAL | [ORIentation](Sense_Correction.md#Orie) | OVERrange[:STATe] | [PMAP](Sense_Correction.md#Pmap) | [SIMCal](Sense_Correction.md#Simcal) | [TRIG:FREE](Sense_Correction.md#PrefTrig) RPOWer:OFFSet | [[:AMPLitude]](Sense_Correction.md#RecPowerOffset) RVELocity | [COAX](Sense_Correction.md#scrc) SFOWard | [[:STATe]](Sense_Correction.md#sforward) [[:STATe]](Sense_Correction.md#scs) [TCOLd:USER:VALue](Sense_Correction.md#tcold) [TDR More Commands](TDR_Correction.md) TSTandards | [[:STATe]](Sense_Correction.md#2STDS1) TYPE | [CATalog?](Sense_Correction.md#catalog) WAVE[:METHod] WAVE:NORM[:METHod] [ZA More Commands](ZA.md)  
---  
  
Click on a keyword to view the command details.

Blue commands are superseded.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * New [See Calibrating the VNA Using SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [ Learn about Measurement Calibration](../../../S3_Cals/Measurement_Calibration.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<cnum>:CORRection:CACHe:MODE <num>

Applicable Models: All (Read-Write) Set this mode at ON for SNP file fast
saving. This must be enabled before the SNP data is acquired by
[CALC:MEAS:DATA:SNP:PORTS:SAVE](../Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:SNP:PORTs:SAVE)
or [CALC:DATA:SNP:PORTS:SAVE](../Calculate/Data.md#snpSave). This value is
channel specific. If the channel does not exist, the default value is returned
(1).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<num> |  0: Never correct all results. 1: Always correct all results. 2: Correct all results when correction is a full 2P and greater. 3: Correct all results when correction is a full 4P and greater. N: Correct all results when correction is a full NP and greater.  
Examples |  SENS2:CORR:CACHe:MODE 2 'any value > 0 and < 9 will work for this example SENS:SWE:MODE SING;*OPC? CALC:MEAS1:DATA:SNP:PORTS:SAVE "1,2,3,4,5,6,7,8","multiportdevice.s8p", FAST  
Query Syntax |  SENSe:CORRection:CACHe:MODE?  
Return Type |  Numeric  
Default |  1 (Preset does not affect the setting.)  
  
* * *

## SENSe<cnum>:CORRection:CCHeck[:ACQuire] <mod>[,char]

Applicable Models: All (Write-only) Reads the 'confidence data' associated
with the specified ECal module and puts it into memory. The measurement is
selected using [SENS:CORR:CCH:PAR](Sense_Correction.md#chkPar). This command
is compatible with *OPC. Note: A confidence check can NOT be performed
remotely from User Characterizations that are stored on the VNA disk.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<mod> |  ECAL Module that contains the confidence data. Choose from: ECAL1 ..through.. ECAL50  
[char] |  Optional argument. Specifies which characterization within the ECal module that the confidence data will be read from. CHAR0 Factory characterization (data that was stored in the ECal module by Keysight). Default if not specified. CHAR1 User characterization #1 CHAR2 User characterization #2 ...and so forth up to: CHAR12 User characterization #12  
Examples |  SENS:CORR:CCHeck ECAL2 sense2:correction:ccheck:acquire ecal1,char1  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:CCHeck:DONE

Applicable Models: All (Write-only) Concludes the Confidence Check and sets
the ECal module back into the idle state.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
Examples |  SENS:CORR:CCH:DONE  
sense2:correction:ccheck:done  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:CCHeck:PARameter <Mname>

Applicable Models: All (Read-Write) Specifies an existing measurement to be
used for the Confidence Check. Note: A confidence check can NOT be performed
remotely from User Characterizations that are stored on the VNA disk.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<Mname> |  Name of the measurement you are selecting for the confidence check. The measurement must already exist.  
Examples |  SENS:CORR:CCH:PAR 'TEST'  
'selects the measurement "test" on channel 1 for the confidence check
sense2:correction:ccheck:parameter 'test'  
'selects the measurement "test" on channel 2 for the confidence check  
Query Syntax |  SENSe<cnum>:CORRection:CCHeck:PARameter? Returns the name of the selected measurement on channel <cnum>.  
Return Type |  String  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:COLLect[:ACQuire] <class>[,subclass][,sync]

Applicable Models: All (Write-only) For UNGUIDED calibration, measures the
specified standards from the selected calibration kit. The calibration kit is
selected using the [Sense:Correction:Collect:CKIT](CorrCollCKIT.md#scccs)
command.  For using two sets of standards, see
[SENS:CORR:TST](Sense_Correction.md#2STDS1). Note: If sending the optional
sync parameter you must also send the optional subclass parameter or a syntax
error will occur. Note: Before using this command you must select two items:  
1\. Select a calibration method using
[SENS:CORR:COLL:METH](Sense_Correction.md#sccm)  
2\. At least one measurement in the channel must be defined. That can be done
with
[CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<class> |  Measures the standards associated with these class labels. Choose from:  
|  Label |  SOLT (Forward) |  SOLT (Reverse) |  TRL  
---|---|---|---|---  
|  STAN1 |  SA |  SA |  TRL "R"  
|  STAN2 |  SB |  SB |  N/A  
|  STAN3 |  SC |  SC |  TRL "L"  
|  STAN4 |  FWD TRANS |  REV TRANS |  TRL "T"  
|  STAN5 |  Generic Isolation; not associated with calibration kit definition.  
|  ECAL1 through ECAL50 |  ECAL modules. You must send a subclass value of CHAR0 through CHAR<n>. This value is not ignored. It refers to either the factory or user characterization.  
|  RESPonse |  Same as [Normalize](../../../S3_Cals/Calibration_Wizard.md#MechMeas) selection in Unguided Cal. (subclass is ignored)  
|  POWer |  Take a receiver power cal sweep and turn correction ON. You must send a subclass value of SST1 through SST7. However, the subclass will be ignored.  
|  SLSET |  Sets 'sliding load type', and increments the "number of slides" count. The total number of slides is critical to the correct calculation of the sliding load algorithm. See a [sliding load cal example.](../../GPIB_Example_Programs/Sliding_Load_Cal.md)  
|  SLDONE |  Computes the sliding load using a circle fit algorithm.  
[subclass] |  Optional argument. For mechanical calibration kits, choose from the following to specify the standard to be acquired from the [SENS:CORR:COLL:CKIT:ORDer](CorrCollCKIT.md#sccco) list. If not specified, subclass is set to SST1.  
|  SST1 |  First standard in the order list  
---|---|---  
|  SST2 |  Second standard in the order list  
|  SST3 |  Third standard in the order list  
|  SST4 |  Fourth standard in the order list  
|  SST5 |  Fifth standard in the order list  
|  SST6 |  Sixth standard in the order list  
|  SST7 |  Seventh standard in the order list  
|  If an ECAL module (1 through 8) is specified for <class>, choose one of the
following for specifying which characterization within the ECal module will be
used for the acquire. If not specified, the default is CHAR0.  
|  CHAR0 |  Factory characterization (data that was stored in the ECal module by Keysight)  
---|---|---  
|  CHAR1 |  User characterization #1  
|  CHAR2 |  User characterization #2  
|  ...and so forth up to:  
|  CHAR12 |  User characterization #12  
[sync] |  Optional argument. Choose from: SYNChronous \- blocks SCPI commands during standard measurement (default behavior) ASYNchronous \- does NOT block SCPI commands during standard measurement. [Learn more about this argument](../../Learning_about_GPIB/Understanding_Command_Synchronization.md#Synch)  
Examples |  SENS:CORR:ACQ POWer,SST1,SYNC 'Subclass is ignored for power  SENS:CORR:ACQ ECAL,CHAR0,SYNC 'Subclass is not ignored - refers to factory or user characterization   
---|---  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:COLLect:APPLy

Applicable Models: All (Write-only) Applies error terms to the measurement
that is selected using
[CALCulate:MEASure:PARameter](../Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter).
Note: Before using this command you must select a measurement using
[CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine).
You can select one measurement for each channel. Note: This command is only
necessary if you need to modify error terms. If you do not need to modify
error terms, [SENSe<cnum>:CORRection:COLLect:SAVE](Sense_Correction.md#sccs)
calculates and then automatically applies error terms after you use
[SENS:CORR:COLL:ACQuire](Sense_Correction.md#scca) to measure cal standards.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
Example | 

  1. CALCulate2:PARameter:SELect S21_2 'select the measurement to apply terms to
  2. SENSe2:CORRection:COLLect:METHod SPARSOLT 'set type of cal method.
  3. CALCulate2:DATA? SCORR1 'download the error term of interest
  4. 'Modify the error term here
  5. CALCulate2:DATA SCORR1 'upload the error term of interest
  6. SENSe2:CORRection:COLLect:APPLy 'applies the error terms to the measurement

  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SENSe:CORRection:COLLect:DISPlay:WINDow:AOFF

Applicable Models: All (Write-only) Clears the flags for windows to be shown
during calibrations. To flag a window to be shown see
[SENS:CORR:COLL:DISP:WIND](Sense_Correction.md#CalWindowState).  
---  
Examples |  SENS:CORR:COLL:DISP:WIND:AOFF sense:correction:collect:display:window:aoff [See an example using this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Query Syntax |  Not Applicable  
Default |  Not Applicable  
  
* * *

## SENSe:CORRection:COLLect:DISPlay:WINDow<wNum>[:STATe] <bool>

Applicable Models: All (Write-only) Set the 'show' state of the window to be
displayed during a calibration to view the measurements/channels. [Learn
more](../../../S3_Cals/Calibration_Wizard.htm#CalWindow).  When this command
is sent, the specified window is 'flagged' to be shown during calibration. The
flag is cleared when the window is closed. A Preset or Instrument State Recall
also closes the window. If the same window number is reopened, this command
must be sent again to show the window during a calibration. The flag is NOT
saved with an instrument state. Send this command for each additional window
to show during a calibration.  
---  
Parameters |   
<wNum> |  Window number to show during a calibration. The calibration window will also be shown with this window. The window must already be created. Use [DISPlay:CATalog?](../Display.md#cat) to read all existing window numbers.  
<bool> |  Window state. Choose from: ON (or 1) - Show the specified window during calibration. OFF (or 0) - Do NOT show the specified window during calibration.  
Examples |  SENS:CORR:COLL:DISP:WIND1 1 sense:correction:collect:display:window2:state off [See an example using this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Query Syntax |  Not Applicable  
Default |  OFF  
  
* * *

## SENSe:CORRection:COLLect:IDLE:TRIGger <bool>

Applicable Models: All (Read-Write) This command enables/disables asynchronous
sweeping during a calibration acquisition.  
---  
Parameters |   
<bool> |  Choose from: ON (or 1) - Enable asynchronous sweeping during a calibration acquisition (the default legacy behavior). OFF (or 0) - Disable asynchronous sweeping during a calibration acquisition.  
Examples |  SENS:CORR:COLL:IDLE:TRIG 1  
Query Syntax |  SENSe:CORRection:COLLect:IDLE:TRIGger?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  ON  
  
* * *

## SENSe:CORRection:COLLect:ISOLation:AVERage:INCRement <num>

Applicable Models: All (Read-Write) Specifies amount to increment (increase)
the channel averaging factor during isolation measurement of the ECal module
during an unguided ECal calibration. Note: if the channel currently has
averaging turned OFF and <num> is greater than 1, averaging will be turned ON
only during the isolation measurements and with the averaging factor equal to
<num>.  
---  
Parameters |   
<num> |  Incremental Averaging factor. The maximum averaging factor is 65536 (2^16).  
Examples |  SENS:CORR:COLL:ISOL:AVER:INCR 16 sense:correction:collect:isolation:average:increment 0  
Query Syntax |  SENSe:CORRection:COLLect:ISOLation:AVERage:INCRement?  
Return Type |  Numeric  
Default |  8 - If this command is NOT sent, but [ECal isolation is measured](Sense_Correction.md#IsoEcal), then averaging will be turned ON with factor set to 8 during the isolation measurement.  
  
* * *

## SENSe<cnum>:CORRection:COLLect:ISOLation:ECAL[:STATe] <bool>

Applicable Models: All (Read-Write) Specifies whether or not the isolation
state of the ECal module will be measured as part of an unguided ECal
calibration. An unguided calibration is performed using the
SENS:CORR:COLL:METH and SENS:CORR:COLL:ACQ commands. Note: The inherent
isolation of the VNA is better than that attained with this command. ONLY use
this command when using an external test set, and ONLY using a 8509x ECal
module.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  ON (or 1) - isolation is measured during the unguided ECal calibration. OFF (or 0) isolation is NOT measured during the unguided ECal calibration.  
Examples |  SENS1:CORR:COLL:ISOL:ECAL ON sense2:correction:collect:isolation:ecal:state 0  
Query Syntax |  SENSe:CORRection:COLLect:ISOLation:ECAL:STATe?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  OFF  
  
* * *

## SENSe<cnum>:CORRection:COLLect:METHod <char>

Applicable Models: All (Read-Write) For UNGUIDED calibration, sets the
calibration method (also known as 'Calibration Type' on calibration dialog
box.) To select a Cal Type from a Cal Set, use
[CALC:MEAS:CORR:TYPE](../Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:TYPE).
Note: Before using this command you must select a measurement using
[CALCulate:PARameter:SELect](../Calculate/Parameter.md#cps). You can select
one measurement for each channel.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<char> |  Choose from:  
  
|  Method |  Description  
---|---|---  
|  NONE |  No Cal method  
|  REFL1OPEN |  Response Open  
|  REFL1SHORT or REFL1 |  Response Short  
|  REFL3 |  Full 1 port  
|  RESPonse |  Same as [Normalize](../../../S3_Cals/Calibration_Wizard.md#MechMeas) selection in Unguided Cal.  
|  RPOWer |  Receiver Power Cal - Used only with receiver measurements.  
|  TRAN1 |  Response Thru - Requires a Thru standard.  
|  TRAN2 |  Response Thru and Isolation - Requires a Thru standard.  
|  SPARSOLT |  Full SOLT 2 port  
  
Examples |  SENS:CORR:COLL:METH REFL1  
sense2:correction:collect:method sparsolt  
---|---  
Query Syntax |  SENSe<cnum>:CORRection:COLLect:METHod?  
Return Type |  Character  
Default |  NONE  
  
* * *

## SENSe<ch>:CORRection:COLLect:NOISe:ENR:ADAPter:DEEMbed[:STATe] <bool>

Applicable Models: All with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the state of ENR Adapter de-embedding. [Learn
more.](../../../Applications/Noise_Cal.htm#DeEmbedAdapter)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  ENR Adapter de-embed state. Choose from: OFF or 0 \- Do not force de-embedding. ON or 1 \- Force de-embedding.  
Examples |  SENS:CORR:COLL:NOIS:ENR:ADAP:DEEM 0 sense2:correction:collect:noise:enr:adapter:deembed:state ON  
Query Syntax |  SENSe:CORRection:COLLect:NOISe:ENR:ADAPter:DEEMbed[:STATe]?  
Return Type |  Boolean  
Default |  O - OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:NOISe:LO<n>:PCAL[:STATe] <bool>

Applicable Models: VNAs with Noise Figure Option (S9x029A/B, 028, 029)
(Excepts M9485A, M980xA, P50xxA/B, M983xA) (Read-Write) Enables and disables
LO power calibration for NFX.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<n> |  LO Stage (number). Choose 1 for NFX.  
<bool> |  LO Power Cal state. Choose from: OFF or 0 \- Disable LO Power Cal ON or 1 \- Enable LO Power Cal  
Examples |  SENS:CORR:COLL:NOIS:LO1:PCAL 0 sense2:correction:collect:noise:lo1:pcal:state ON  
Query Syntax |  SENSe:CORRection:COLLect:NOISe:LO<n>:PCAL:STATe?  
Return Type |  Boolean  
Default |  O - OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:NOISe:PSENsor:ADAPter:DEEMbed[:STATe] <bool>

Applicable Models: VNAs with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the state of power sensor adapter de-embedding. [Learn
more.](../../../Applications/Noise_Cal.htm#DeEmbedAdapter)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  Power sensor adapter de-embed state. Choose from: OFF or 0 \- Do not force de-embedding. ON or 1 \- Force de-embedding.  
Examples |  SENS:CORR:COLL:NOIS:PSEN:ADAP:DEEM 0 sense2:correction:collect:noise:psensor:adapter:deembed:state ON  
Query Syntax |  SENSe:CORRection:COLLect:NOISe:PSENsor:ADAPter:DEEMbed[:STATe]?  
Return Type |  Boolean  
Default |  O - OFF  
  
* * *

## SENSe<ch>:CORRection:COLLect:NOISe:RECeiver:PULL[:STATe] <bool>

Applicable Models: VNAs with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the state of the noise receiver pulling during
calibration. This determines whether or not noise parameters of the noise
receiver are measured. [Learn
more.](../../../Applications/Noise_Cal.htm#MeasNoiseParams)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  Noise receiver pull state. Choose from: OFF or 0 \- Do not perform noise receiver pulling measurements. ON or 1 \- Perform noise receiver pulling measurements.  
Examples |  SENS:CORR:**COLL:NOIS:REC:PULL 0** sense2:correction:collect:**noise:receiver:pull:state ON**  
Query Syntax |  SENSe:CORRection:COLLect:NOISe:RECeiver:PULL[:STATe]?  
Return Type |  Boolean  
Default |  1 - ON  
  
* * *

## SENSe<ch>:CORRection:COLLect:NOISe:THRU:ADAPter:DEEMbed[:STATe] <bool>

Applicable Models: VNAs with Noise Figure Option (S9x029A/B, 028, 029) (Read-
Write) Set and read the state of the thru adapter de-embedding. [Learn
more.](../../../Applications/Noise_Cal.htm#DeEmbedAdapter)  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1  
<bool> |  Thru adapter de-embed state. Choose from: OFF or 0 \- Do not force de-embedding. ON or 1 \- Force de-embedding.  
Examples |  SENS:CORR:COLL:NOIS:THRU:ADAP:DEEM 0 sense2:correction:collect:noise:thru:adapter:deembed:state ON  
Query Syntax |  SENSe:CORRection:COLLect:NOISe:THRU:ADAPter:DEEMbed[:STATe]?  
Return Type |  Boolean  
Default |  O - OFF  
  
* * *

## SENSe<cnum>:CORRection:COLLect:SAVE

Applicable Models: All (Write-only) For UNGUIDED calibrations ONLY. This
command does the following:

  * calculates the error terms using the selected :METHod
  * applies the error terms to the selected measurement (turns error correction ON.)
  * saves the calibration error-terms to the channels Cal Register or a User Cal Set.

The Cal Register or User Cal Set is determined by the setting of the
[SENS:CORR:PREFerence:CSET:SAVE](Sense_Correction.md#CsetSave) command. Do
NOT use this command during an ECAL. When performing an ECAL calibration using
[SENS:CORR:COLL:ACQuire](Sense_Correction.md#scca), this SAVE operation is
performed automatically before the completion of a successful ACQuire. Before
using this command you must select a measurement using
[CALCulate:MEASure:PARameter](../Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter).
You can select one measurement for each channel.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
Examples |  SENS:CORR:COLL:SAVE  
sense2:correction:collect:save  
Query Syntax |  Not applicable  
Default |  Not applicable  
  
* * *

## SENSe:CORRection:COLLect:SWEep:CHANnel:AOFF

Applicable Models: All (Write-only) Clears ALL flags for channels to sweep
during calibration. To flag a channel, see
[SENS:CORR:COLL:SWE:CHAN](Sense_Correction.md#CalWinSweepChan).  This is
equivalent with
[SENSe:CORRection:COLLect:GUIDed:DISPlay:WINDow:AOFF](CorrGuided.md#DispWindAoff).  
---  
Examples |  SENS:CORR:COLL:SWE:CHAN:AOFF sense:correction:collect:sweep:channel:aoff [See an example using this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Default |  Not applicable  
  
* * *

## SENSe<cnum>:CORRection:COLLect:SWEep:CHANnel<cnum2>[:STATe] <bool>

Applicable Models: All (Write-only) Specifies an alternate channel (other than
the calibration channel) to be viewed while using the calibration wizard.
When this command is sent, the <cnum2> channel is 'flagged' to be swept during
calibration.  The flag is cleared when the channel is deleted, if the
Measurement Class is changed, or if all measurements are deleted from the
channel. If the same channel number is recreated, this command must be sent
again to sweep the channel during a calibration. The flag is NOT saved with an
instrument state. A Preset or Instrument State Recall deletes the channel.
This is equivalent with
[SENSe:CORRection:COLLect:GUIDed:DISPlay:WINDow](CorrGuided.md#DispWindStat).
Note: This command is intended to be used in conjunction with the interactive
calibration wizard.  
---  
Parameters |   
<cnum> |  The channel to be calibrated. If unspecified, value is set to 1.  
<cnum2> |  The channel to sweep when waiting to measure a standard. This channel must already exist with at least one measurement in the channel. If this channel is in continuous sweep mode, it must have the same attenuator settings and path configuration (PNA-X only).  
<bool> |  Channel sweep state. Choose from: ON (or 1) - Sweep the channel during calibration. OFF (or 0) - Do NOT sweep the channel during calibration.  
Examples |  SENS:CORR:COLL:SWE:CHAN2 1 sense2:correction:collect:sweep:channel3:state off [See an example using this command.](../../GPIB_Example_Programs/Show_Custom_Window_during_Calibration.md)  
Query Syntax |  Not Applicable  
Default |  OFF  
  
* * *

## SENSe:CORRection:ENR:CALibration:TABLe:DATA <freq, value, freq, value...>

Applicable Models: All (Read-Write) Set and read the ENR (Excess Noise Ratio)
calibration data. All of the frequency and ENR data must be sent at the same
time. Use [MMEM:LOAD](../Memory.md#recall) to load, and [MMEM:STORE:ENR
CAL](../Memory.htm#StoreENR) to save ENR table data from disk. [Learn more
about Noise Source ENR files.](../../../Applications/Noise_Cal.htm#ENRFiles)  
---  
Parameters |   
<freq, value> |  (Numeric) ENR data. Frequency value in Hz followed by a ENR noise value in dB. Enter as many pairs as necessary.  
Examples |  SENS:CORR:ENR:CAL:TABL:DATA 1.0E9,14.37,2.5E9,15.28  
sense:correction:enr:calibration:table:data 1.0E9,14.37,2.5E9,15.28  
Query Syntax |  SENSe:CORRection:ENR:CALibration:TABLe:DATA?  
Return Type |  Comma separated numeric values  
Default |  Not Applicable  
  
* * *

## SENSe:CORRection:ENR:CALibration:TABLe:ID:DATA <id>

Applicable Models: All (Read-Write) Sets and returns ID of ENR table. While
this is for informational purposes only, it can be used to record the model of
the noise source. [Learn more about ENR
files.](../../../Applications/Noise_Cal.htm#ENRFiles)  
---  
Parameters |   
<id> |  (String) Identifier for the ENR table.  
Examples |  SENS:CORR:ENR:CAL:TABL:ID:DATA "346C"  
sense:correction:enr:calibration:table:id:data "ENR Table"  
Query Syntax |  SENSe:CORRection:ENR:CALibration:TABLe:ID:DATA?  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## SENSe:CORRection:ENR:CALibration:TABLe:SERial:DATA <sn>

Applicable Models: All (Read-Write) Sets and returns the serial number of
noise source. This is for informational purposes only to identify the specific
noise source for which the data pertains. [Learn more about ENR
files.](../../../Applications/Noise_Cal.htm#ENRFiles)  
---  
Parameters |   
<sn> |  Serial number of the noise source for which the data applies, enclosed in quotes.  
Examples |  SENS:CORR:ENR:CAL:TABL:SER:DATA "ABCD1234"  
sense:correction:enr:calibration:table:serial:data "ABCD1234"  
Query Syntax |  SENSe:CORRection:ENR:CALibration:TABLe:SERial:DATA?  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## SENSe:CORRection:ENR:CALibration:TABLe:TEMPerature:DATA <num>

Applicable Models: All (Read-Write) Sets/Returns the value of the temperature
in the ENR file (the temperature it was calibrated at) in Kelvin. The ENR file
must be first loaded by [MMEM:LOAD](../Memory.md#recall). [Learn more about
ENR files.](../../../Applications/Noise_Cal.htm#ENRFiles)  
---  
Parameters |   
<num> |  Temperature level in Kelvin.  
Examples |  SENS:CORR:ENR:CAL:TABL:TEMP:DATA 273.0 SENSe:CORRection:ENR:CALibration:TABLe:TEMPerature:DATA 302  
Query Syntax |  SENSe:CORRection:ENR:CALibration:TABLe:TEMPerature:DATA?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:GCSetup:POWer <num>

Applicable Models: N522xB, N524xB, M9485A, E5080A/B, M980xA, P50xxA/B, M983xA
(Read-Write) Set and read the power level at which to perform the Source Power
Cal portion of a Gain Compression (Opt S93086A/B) Calibration. [Learn more
about this setting.](../../../Applications/GCA_Cal.htm#SourceCal)  
---  
Parameters |   
<num> |  Power level in dB. Choose a value from +30 to (-30).  
Examples |  SENS:CORR:GCS:POW 0  
sense:correction:gcsetup:power 5  
Query Syntax |  SENSe:CORRection:GCSetup:POWer?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SENSe<ch>:CORRection:GCSetup:SENSor:CKIT <string>

Applicable Models: N522xB, N524xB, M9485A, E5080A/B, M980xA, P50xxA/B, M983xA
(Read-Write) Set and read the cal kit to be used for calibrating at the port 1
reference plane when the power sensor connector is different from the DUT port
1. [Learn more.](../../../Applications/GCA_Cal.md#SelectDUTDiag)  
---  
Parameters |   
<string> |  Cal Kit. Use [SENS:CORR:COLL:GUID:CKIT:PORT1:CAT?](CorrGuided.md#gKitCat) to return a list of valid cal kits.  
Examples |  SENS:CORR:GCS:SENS:CKIT "85052B"  
Query Syntax |  SENSe:CORRection:GCSetup:SENSor:CKIT?  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## SENSe<ch>:CORRection:GCSetup:SENSor:CONNector<string>

Applicable Models: N522xB, N524xB, M9485A, E5080A/B, M980xA, P50xxA/B, M983xA
(Read-Write) Set and read the power sensor connector type which is used to
perform the Source Power Cal portion of a Gain Compression Calibration. [Learn
more.](../../../Applications/GCA_Cal.htm#SelectDUTDiag)  
---  
Parameters |   
<string> |  Power sensor connector type. Use [SENS:CORR:COLL:GUID:CONN:CAT?](CorrGuided.md#gConnCat) to return a list of valid connector types. Select "Ignored" to NOT compensate for the adapter.  
Examples |  SENS:CORR:GCS:SENS:CKIT "3.5 mm (50) male"  
Query Syntax |  SENSe:CORRection:GCSetup:SENSor:CKIT?  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## SENSe:CORRection:IMPedance:INPut:MAGNitude <num>

Applicable Models: All (Read-Write) Sets and returns the system impedance
value for the analyzer.  
---  
Parameters |   
<num> |  System Impedance value in ohms. Choose any number between 0.001 and 1000 ohms.  
Examples |  SENS:CORR:IMP:INP:MAGN 75  
sense:correction:impedance:input:magnitude 50.5  
Query Syntax |  SENSe:CORRection:IMPedance:INPut:MAGNitude?  
Return Type |  Numeric  
Default |  50  
  
* * *

## SENSe<ch>:CORRection:INTerpolate[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns correction interpolation ON or OFF.
Note: Before using this command you must select a measurement using
[CALC:PAR:SEL](../Calculate/Parameter.md#cps). You can select one measurement
for each channel.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns interpolation ON.   
OFF (or 0) - turns interpolation OFF.  
Examples |  SENS:CORR:INT ON  
sense2:correction:interpolate:state off  
Query Syntax |  SENSe<cnum>:CORRection:INTerpolate[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  ON  
  
* * *

## SENSe<ch>:CORRection:ISOLation[:STATe] <ON | OFF> OBSOLETE

This command no longer works beginning in the VNA 5.2 release. The set and
query of this command will NOT return an error. To perform isolation as part
of an unguided calibration, you must explicitly measure the isolation standard
using [SENS:CORR:COLL:ACQ Stan5](Sense_Correction.md#scca). To measure
isolation as part of an ECal, use
[SENS:CORR:COLL:ISOL:ECAL](Sense_Correction.md#IsoEcal). (Read-Write) Turns
isolation cal ON or OFF during Full 2-port calibration. If this command is not
sent, the default state is to disable Isolation.  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns isolation ON. OFF (or 0) - turns isolation OFF.  
Examples |  SENS:CORR:ISOL ON sense2:correction:isolation:state off  
Query Syntax |  SENSe<cnum>:CORRection:ISOLation[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  OFF - (Isolation disabled)  
  
* * *

## SENSe<ch>:CORRection:LEAKage[:STATe] <ON | OFF>

This command enables the leaky part for error correction. this commands
depends on SENS:CORR[:STATe] in the following way

  * When channel correction is enabled, leaky correction is enabled automatically
  * When channel correction is disabled, leaky correction is disabled automatically
  * Use SENS:CORR:LEAK:STAT to control the leakage correction when channel correction is enabled
  * When a calset with leaky cal is selected, channel correction is enabled as well as leakage correction 
    * If the calset has lo leakage, the leaky correction is not enabled

  
---  
Parameters |   
<ch> |  Any existing channel number. If unspecified, value is set to 1.  
<ON | OFF> |  ON (or 1) - turns leakage part ON. OFF (or 0) - turns leakage partn OFF.  
Examples |  SENS:CORR:LEAK ON sense2:correction:leakage:state off  
Query Syntax |  SENSe<cnum>:CORRection:LEAKaga[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  OFF - (leaky disabled)  
  
* * *

## SENSe<ch>:CORRection:METHods:MATCh <bool>

Applicable Models: All (Read-Write) Turns match-correction ON or OFF. Use this
command AFTER performing an Guided Power Cal. [Learn
more.](../../../S3_Cals/Guided_Power_Calibration.htm#Matching)  
---  
Parameters |   
<ch> |  Channel number on which Guided Power Cal was performed. If unspecified, value is set to 1.  
<bool> |  ON (or 1) - Turns match-correction ON OFF (or 0) - Turns match-correction OFF.  
Examples |  SENS:CORR:METH:MATC 0  
sense2:correction:methods:match off  
Query Syntax |  SENSe<cnum>:CORRection:METHods:MATCh?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  ON  
  
* * *

## SENSe<ch>:CORRection:METHods:PORT:SUBSet:FULL[:VALue] <port numbers>

Applicable Models: All (Read-Write) Sets and returns the selected ports to
include in a full NPort correction. If other ports are selected using the
SENSe:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue] command, they will be
corrected with enhanced response calibration. Ports not selected using the
SENSe:CORRection:METHods:PORT:SUBSet:FULL[:VALue] or
SENSe:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue] command are uncorrected.
[Learn more](../../../S3_Cals/Guided_Power_Calibration.md#MatchingDialog).
The default is all ports are selected for a full NPort correction. To assign a
port to be corrected with enhanced response calibration using the
SENSe:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue] command, they first have
to be removed from the full NPort correction list. Ports can be removed from
the full NPort correction list by setting a new list that excludes the ports
to be corrected with enhanced response calibration. For information about port
sub-setting, refer to [Port Sub-Setting Examples](../../../S3_Cals/Port_Sub-
Setting.htm). Note: The SENSe:CORRection:METHods:PORT:SUBSet:[:STATe] must be
set to ON to enable the full command.  
---  
Parameters |   
<ch> |  Channel number.  
<port numbers> |  Comma separated list of ports to include in the full correction. The default is all ports selected.  
Examples |  16-port VNA with an active 16-port calibration SENS:CORR:METH:PORT:SUBS:STAT 1 SENS:CORR:METH:PORT:SUBS:FULL:VAL 1,2,3  
sense2:correction:methods:port:subset:full:value 1,2,3 Result: Full correction
on ports 1, 2, and 3 All other port parameters are uncorrected  
Query Syntax |  SENSe<cnum>:CORRection:METHods:PORT:SUBSet:FULL[:VALue]?  
Return Type |  Array_int  
Default |  All ports included  
  
* * *

## SENSe<ch>:CORRection:METHods:PORT:SUBSet:RESet

Applicable Models: All (Write) Resets the full and response list to their
default values. [Learn
more](../../../S3_Cals/Guided_Power_Calibration.htm#MatchingDialog).  For
information about port sub-setting, refer to [Port Sub-Setting
Examples](../../../S3_Cals/Port_Sub-Setting.htm).  
---  
Parameters |   
<ch> |  Channel number.  
Examples |  SENS:CORR:METH:PORT:SUBS:RES  
sense2:correction:methods:port:subset:reset  
Return Type |  Not applicable  
Default |  Not applicable  
  
* * *

## SENSe<ch>:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue] <port numbers>

Applicable Models: All (Read-Write) Sets and returns the selected ports to be
corrected with enhanced response calibration. If other ports are selected
using the SENSe:CORRection:METHods:PORT:SUBSet:FULL[:VALue] command, they will
be corrected in a full NPort correction. Ports not selected using the
SENSe:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue] or
SENSe:CORRection:METHods:PORT:SUBSet:FULL[:VALue] command are uncorrected.
[Learn more](../../../S3_Cals/Guided_Power_Calibration.md#MatchingDialog).
To assign a ports to be corrected with enhanced response calibration ensure
that they are not selected for the full NPort correction list. Ports can be
removed from the full NPort correction list by setting a new list that
excludes the ports to be corrected with enhanced response calibration. For
information about port sub-setting, refer to [Port Sub-Setting
Examples](../../../S3_Cals/Port_Sub-Setting.htm). Note: The
SENSe:CORRection:METHods:PORT:SUBSet:[:STATe] must be set to ON to enable the
response command.  
---  
Parameters |   
<ch> |  Channel number.  
<port numbers> |  Comma separated list of ports to include for enhanced response correction. The default is no ports selected.  
Examples |  Example #1: 16-port VNA with an active 16-port calibration SENS:CORR:METH:PORT:SUBS:STAT 1 SENS:CORR:METH:PORT:SUBS:FULL:VAL 1,2,3,4,5,6  
SENS:CORR:METH:PORT:SUBS:RESP:VAL 7,8 Result: Full correction on ports 1-6
Enhanced response corrected for parameters involving ports 7 and 8 No
correction for ports 9-16 Example #2: 16-port VNA with an active 16-port
calibration SENS:CORR:METH:PORT:SUBS:FULL:VAL 0  
SENS:CORR:METH:PORT:SUBS:RESP:VAL 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16
Result: Enhanced response correction for parameters involving any ports  
Query Syntax |  SENSe<cnum>:CORRection:METHods:PORT:SUBSet:RESPonse[:VALue]?  
Return Type |  Array_int  
Default |  Empty list  
  
* * *

## SENSe<ch>:CORRection:METHods:PORT:SUBSet[:STATe] <bool>

Applicable Models: All (Read-Write) Set and return the ON/OFF subset
correction state. [Learn
more](../../../S3_Cals/Guided_Power_Calibration.htm#MatchingDialog).  For
information about port sub-setting, refer to [Port Sub-Setting
Examples](../../../S3_Cals/Port_Sub-Setting.htm).  
---  
Parameters |   
<ch> |  Channel number.  
<bool> |  Choose from: 0 - OFF \- Subset correction OFF. 1 - ON \- Subset correction ON.  
Examples |  SENS:CORR:METH:PORT:SUBS:STAT 1 sense2:correction:methods:port:subset:state 1  
Query Syntax |  SENSe<cnum>:CORRection:METHods:PORT:SUBSet:[:STATe]?  
Return Type |  Boolean  
Default |  0  
  
* * *

## SENSe<cnum>:CORRection:METHods:SA:PORT<pnum> <CorrMethod>

Applicable Models: All with Spectrum Analysis (Write-Read) Sets and returns
the correction method for the spectrum analysis.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<pnum> |  Port number. If unspecified, value is set to 1.  
<CorrMethod> |  Correction Method. Choose from: ACTual : The full error corrected actual waves at device reference planes. RESPonse: Raw measurements scaled with the response terms and do not include any match correction.  
Examples |  SENS:CORR:METH:SA:PORT2 ACTual sense2:correction:methods:sa:port1 actual  
Query Syntax |  SENSe<cnum>:CORRection:METHods:SA:PORT<pnum>?  
Default |  RESPonse  
  
* * *

## SENSe<ch>:CORRection:MODel <param>

Applicable Models: All except E5080A, M9485A (Write-Read) Sets and returns the
error term model. Note: In trigger hold mode, acquired data may be inaccurate
after transitioning from 10 to 8 term model. In this case, it is recommended
to trigger a new sweep. The reverse transition (8 to 10 term model) is safe
and does not require the new sweep.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<parm> |  Error term method. Choose from: TERM8 TERM10  
Examples |  SENS1:CORR:MOD TERM8  
Query Syntax |  SENSe<cnum>:CORRection:MODel?  
Return Type |  String  
Default |  TERM10  
  
* * *

## SENSe:CORRection:PREFerence:CALibration[:FOM]:RANGe <char>

Applicable Models: All (Read-Write) Specifies the FOM frequency range to use
when performing calibration.  
---  
Parameters |   
<char> |  Choose from: PRIMary \- Used for calibrating at the mmWave frequencies when NOT using a test set. [Learn more.](../../../IFAccess/mmWave_Measurement_w_No_Test_Set.md) AUTO \- All other calibration situations.  
Examples |  SENS:CORR:PREF:CAL:RANG PRIM  
sense:correction:preference:calibration:fom:range auto  
Query Syntax |  SENSe:CORRection:PREFerence:CALibration[:FOM]:RANGe?  
Return Type |  Character  
Default |  AUTO  
  
* * *

## SENSe:CORRection:PREFerence:CSET:SAVE <char>

Applicable Models: All Important Notes:

  * This command replaces [SENS:CORR:PREF:CSET:SAVU](Sense_Correction.md#savuser)
  * With 6.0 we implemented a change that defaults to saving completed calibrations to Cal Registers instead of User Cal Sets. To revert to the old behavior, send this command with the USER argument.

(Read-Write) Specifies the default manner in which calibrations that are
performed using SCPI or COM are to be stored. Cal data is ALWAYS stored to the
channel Cal Register regardless of this setting. This setting survives
instrument preset and reboot. It remains until changed by another execution of
this command. Note: Cal Set arguments used with commands such as
[SENS:CORR:COLL:GUID:INIT](CorrGuided.md#gInit),
[SENS:CORR:COLL:GUID:SAVE](CorrGuided.md#gSave) and
[SENS:CORR:COLL:GUID:SAVE:CSET](CorrGuided.md#SaveCSET) will override of any
of these default preference settings. Learn about [Cal Registers and User Cal
Sets.](../../../S3_Cals/Cal_Sets.htm)  
---  
Parameters |   
<char> |  CALRegister \- Each Cal is saved ONLY to the channel Cal Register. If the error terms from a new Cal can co-exist with those in the Cal Register, they are appended. USER \- Each Cal is saved to its own new User Cal Set file. The Cal Set name is automatically generated. To change the name, send [SENS:CORR:CSET:NAME](CorrCset.md#name) after the cal is complete. This reverts to pre-6.0 behavior. REUSe \- The cal is saved to the Cal Set that is currently selected on the specified channel, which could be the channel Cal Register. If the channel does not yet have a selected Cal Set, the cal will be saved to a new User Cal Set with an automatically-generated name. If the error terms from a new Cal can co-exist with those in the Cal Set, they are appended.  
Examples |  SENS:CORR:PREF:CSET:SAVE USER  
sense:correction:preference:cset:save reuse  
Query Syntax |  SENSe:CORRection:PREFerence:CSET:SAVE?  
Return Type |  Character  
Default |  CALRegister  
  
* * *

## SENSe:CORRection:PREFerence:CSET:SAVUser <bool> Superseded

Applicable Models: N522xB, N523xB, N524xB, M9485A This command is replaced
with [SENS:CORR:PREF:CSET:SAVE](Sense_Correction.md#CsetSave) NOTE: With 6.0
we implemented a change that defaults to saving completed calibrations to Cal
Registers instead of User Cal Sets. To revert to the old behavior, send this
command as ON (1). For UI and COM use, this can be done from the [GPIB
console](../../Learning_about_GPIB/How_to_Configure_for_GPIB_SCPI_and_SICL.htm#console).
(Read-Write) Specifies whether cal data is automatically saved to a User Cal
Set file after performing a SCPI calibration. Cal data is always saved to a
Cal Register regardless of this setting. This setting survives instrument
preset and reboot. It remains until changed by another execution of this
command. Learn about [Cal Registers and User Cal
Sets.](../../../S3_Cals/Cal_Sets.htm)  
---  
Parameters |   
<bool> |  ON or 1 \- Cal is automatically saved to a User Cal Set file when performing a SCPI calibration. The Cal Set name is automatically generated. To change the name, send [SENS:CORR:CSET:NAME](CorrCset.md#name) after the cal is complete. Reverts to pre-6.0 behavior. OFF or 0 \- Cal is NOT automatically saved to a User Cal Set. To save a calibration to a User Cal Set, use [SENS:CORR:COLL:GUID:INIT](CorrGuided.md#gInit).  
Examples |  SENS:CORR:PREF:CSET:SAVU 1  
sense:correction:preference:cset:savuser 0  
Query Syntax |  SENSe:CORRection:PREFerence:CSET:SAVUser?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  OFF (0)  
  
* * *

## SENSe:CORRection:PREFerence:ECAL:ORIentation[:STATe] <ON|OFF>

Applicable Models: All (Read-Write) Specifies whether or not the VNA should
perform orientation of the ECal module during calibration. Orientation is a
technique by which the VNA automatically determines which ports of the module
are connected to which ports of the VNA. Orientation begins to fail at very
low power levels or if there is much attenuation in the path between the VNA
and the ECal module. If orientation is turned OFF, the
[SENS:CORR:PREF:ECAL:PMAP](Sense_Correction.md#Pmap) command must be used to
specify the port connections before performing a cal.  Note: For 3-port or
4-port measurements, when orientation is OFF, you are not allowed to specify
how the ECAL module is connected. Instead, the VNA determines the orientation.
Use [SENS:CORR:COLL:GUID:DESC?](CorrGuided.md#gDesc) to query the
orientation. The VNA does not verify that you made the connection properly.
This setting remains until the VNA is restarted or this command is sent again.  
---  
Parameters |   
<bool> |  ECAL orientation state. Choose from: ON or 1 \- VNA performs orientation of the ECal module. OFF or 0 \- VNA does NOT performs orientation of the ECal module.  
Examples |  SENS:CORR:PREF:ECAL:ORI OFF sense:correction:preference:ecal:orientation:state on  
Query Syntax |  SENSe:CORRection:PREFerence:ECAL:ORIentation[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  ON (1)  
  
* * *

## SENSe:CORRection:PREFerence:ECAL:OVERrange[:STATe] <ON|OFF>

Applicable Models: All (Read-Write) Sets and returns the ECAL over range
state.  
---  
Parameters |   
<bool> |  ECAL over range state. Choose from: ON or 1 \- Enable ECAL over range. OFF or 0 \- Disable ECAL over range.  
Examples |  SENS:CORR:PREF:ECAL:OVER OFF sense:correction:preference:ecal:overrange:state on  
Query Syntax |  SENSe:CORRection:PREFerence:ECAL:OVERrange[:STATe]?  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  ON (1)  
  
* * *

## SENSe:CORRection:PREFerence:ECAL:PMAP <module>,<string>

Applicable Models: All (Read-Write) When ECal module orientation is turned OFF
([SENS:CORR:PREF:ECAL:ORI](Sense_Correction.md#Orie)), this command specifies
the port mapping (which ports of the module are connected to which ports of
the VNA) prior to performing ECal calibrations. This setting remains until the
VNA is restarted or this command is sent again.  
---  
Parameters |   
<module> |  Specifies which ECal module this port map is being applied to. Choose from: ECAL1 .through. ECAL50  
<string> |  Format this parameter in the following manner: Aw,Bx,Cy,Dz where

  * A, B, C, and D are literal ports on the ECAL module
  * w,x,y, and z are substituted for VNA port numbers to which the ECAL module port is connected.

Ports of the module which are not used are omitted from the string. For
example, on a 4-port ECal module with port A connected to VNA port 2 port B
connected to VNA port 3 port C not connected port D connected to VNA port 1
the string would be: A2,B3,D1 If either the receive port or source port (or
load port for 2-port cal) of the CALC:PAR:SELected measurement is not in this
string and orientation is OFF, an attempt to perform an ECal calibration will
fail.  
Examples |  SENS:CORR:PREF:ECAL:PMAP ECAL2, 'A1,B2' sense:correction:preference:ecal:pmap ecal3, 'a2,b1,c3'  
Query Syntax |  SENSe:CORRection:PREFerence:ECAL:PMAP? <module>  
Return Type |  String  
Default |  Null string ()  
  
* * *

## SENSe:CORRection:PREFerence:SIMCal <bool> Obsolete

This command is no longer supported. [Learn more about old and new
behaviors.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Uploading)
(Read-Write) Sets and returns a preference for the Unguided Cal behavior
described below. This setting persists until it is changed. This preference
can also be set ON by executing the script on the VNA at C:\Program
Files(x86)\Keysight\Network Analyzer\System\wincal32.reg.  
---  
Parameters |   
<bool> |  Boolean - Choose from: 0 - OFF \- Reverts to new (preferred) behavior. An error is returned if standard data is not acquired before sending [SENS:CORR:COLL:SAVE](Sense_Correction.md#sccs). 1 - ON \- (WinCal compatible) Prevents [SENS:CORR:COLL:SAVE](Sense_Correction.md#sccs) from failing when standard data has not, and will not, be acquired.  
Examples |  SENS:CORR:PREF:SIMC 0 sense:correction:preference:simcal 1  
Query Syntax |  SENSe:CORRection:PREFerence:SIMCal?  
Return Type |  Boolean  
Default |  0  
  
* * *

## SENSe:CORRection:PREFerence:TRIG:FREE <char>, <bool>

Applicable Models: All (Read-Write) Sets and returns the preference for the
trigger behavior during a calibration. This setting persists until it is
changed. Note: If [TRIGger:SOURce](../Trigger_SCPI.md#tss) = Manual, during a
calibration the VNA ALWAYS switches to Internal for one trigger, then back to
Manual, regardless of this preference command.  
---  
Parameters |   
<char> |  Character \- Calibration type. Choose from: GUIDed - preference setting pertains to a Guided calibration. UNGuided - preference setting pertains to an Unguided calibration.  
<bool> |  Boolean - Choose from: 0 - OFF \- The trigger behavior during the specified calibration type DOES respect the setting of the [TRIGger:SOURce](../Trigger_SCPI.md#tss) command. For example,when Trigger source = External, the single trigger method will wait for the External trigger signal and then allow only one sweep. 1 - ON \- (Pre-6.0 behavior) The trigger behavior during the specified calibration type does NOT respect the setting of the [TRIGger:SOURce](../Trigger_SCPI.md#tss) command. For example, when Trigger source = External, during calibration the VNA switches to Internal sweep, responds to one trigger signal to measure the standard, then switches back to External.  
Examples |  SENS:CORR:PREF:TRIG:FREE GUID,1 sense:correction:preference:trig:free unguided,0  
Query Syntax |  SENSe:CORRection:PREFerence:TRIG:FREE? <char>  
Return Type |  Boolean  
Default |  OFF for both calibration types.  
  
* * *

## SENSe<cnum>:CORRection:RPOWer:OFFSet[:AMPLitude] <num>

Applicable Models: All (Read-Write) Adjusts a receiver power cal to account
for components or adapters that are added between the source port and receiver
while performing this cal. For more information, see [Receiver
Cal](../../../S3_Cals/PwrCalibration.htm#ReceiverPowerCal).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Offset Value in dB. Specify loss as a negative number; and gain as a positive number. Choose a number between -200 and 200.  
Examples |  SENS:CORR:RPOW:OFFS .5  
sense2:correction:rpower:offset:amplitude .-5  
Query Syntax |  SENSe<cnum>:CORRection:RPOWer:OFFSet[:AMPLitude]?  
Return Type |  Numeric  
Default |  0  
  
* * *

## SENSe<cnum>:CORRection:RVELocity:COAX <num>

Applicable Models: All (Read-Write) Sets the velocity factor to be used with
Electrical Delay and Port Extensions.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<num> |  Velocity factor. Choose a number between 0 and 10 (.66 polyethylene dielectric; .7 PTFE dielectric)  
Examples |  SENS:CORR:RVEL:COAX .66  
sense2:correction:rvelocity:coax .70  
Query Syntax |  SENSe<cnum>:CORRection:RVELocity:COAX?  
Return Type |  Numeric  
Default |  1  
  
* * *

## SENSe<cnum>:CORRection:SFORward[:STATe] <boolean>

Applicable Models: All (Read-Write) Sets the direction a calibration will be
performed when only one set of standards is used.  Use
[SENSe:CORRection:TSTandards[:STATe]](Sense_Correction.md#2STDS1) OFF to
specify that only one set of standards will be used.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<boolean> |  ON (1) \- FORWARD direction of a 2-port calibration will be performed OFF (0) \- REVERSE direction of a 2-port calibration will be performed  
Examples |  SENS:CORR:SFOR 1  
sense2:correction:sforward:state 0 See an
[example](../../GPIB_Example_Programs/Perform_Unguided_2-Port_Mech_Cal.md)
using this command  
Query Syntax |  SENSe<cnum>:CORRection:SFORward[:STATe]?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## SENSe<cnum>:CORRection[:STATe] <ON | OFF>

Applicable Models: All (Read-Write) Turns error correction ON and OFF for the
specified channel.  Note: Before using this command you must select a
measurement using
[CALCulate:MEASure:PARameter](../Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter).
You can select one measurement for each channel.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1  
<ON | OFF> |  ON (or 1) - correction is applied to the channel. OFF (or 0) - correction is NOT applied to the channel.  
Examples |  SENS:CORR ON  
sense2:correction:state off  
Query Syntax |  SENSe<cnum>:CORRection[:STATe]? To query the error correction state for a measurement, use [CALC:MEAS:CORR:STATe?](../Calculate/MeasureCorrection.md#CALCulate:MEASure:CORRection:STATe)  
Return Type |  Boolean (1 = ON, 0 = OFF)  
Default |  OFF  
  
* * *

## SENSe<cnum>:CORRection:TCOLd:USER:VALue <num>

Applicable Models: All (Read-Write) Sets and returns the temperature of the
noise source connector. Learn more about [Noise Figure
Calibration](../../../Applications/Noise_Cal.htm).  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<num> |  Noise source temperature in Kelvin.  
Examples |  SENS:CORR:TCOL:USER:VAL 295 sense2:correction:tcold:user:value 298 See an [example](../../GPIB_Example_Programs/Create_and_Cal_a_Noise_Figure_Measurement.md) using this command  
Query Syntax |  SENSe<cnum>:CORRection:TCOLd:USER:VALue?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:TSTandards[:STATe] <boolean>

Applicable Models: All (Read-Write) Specifies the acquisition of calibration
data using ONE or TWO sets of standards.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<boolean> |  ON (1) \- TWO identical sets of standards will be used to simultaneously calibrate two ports (for both Forward and Reverse parameters). OFF (0)\- ONE set of standards will be used to perform a full 2-port calibration, one port at a time. When specifying ON (use two sets), the [SENS:CORR:COLL:ACQuire](Sense_Correction.md#scca) command uses the same standard index for each calibration class. To specify the calibration standard gender for each port, you must first ensure that the order of calibration class accurately reflects the configuration of your DUT. For example, for a DUT with a male connector on port 1 and a female connector on port 2, order the devices within the S11 classes (A, B, and C) such that the MALE standards are first in the list. Then order the S22 classes specifying the FEMALE standards as the first in the list.  
Examples |  SENS:CORR:TST 1  
sense2:correction:tstandard:state 0 See an
[example](../../GPIB_Example_Programs/Perform_Unguided_2-Port_Mech_Cal.md)
using this command  
Query Syntax |  SENSe<cnum>:CORRection:TSTandards[:STATe]?  
Return Type |  Boolean  
Default |  ON  
  
* * *

## SENSe:CORRection:TYPE:CATalog? <char>

Applicable Models: All (Read-Write) Lists the Cal Types in the VNA by either
GUID or registered name. [Learn more about applying Cal Type using
SCPI.](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)
Note: Before using this command you must select a measurement using
[CALCulate:MEASure:PARameter](../Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter).
You can select one measurement for each channel.  
---  
Parameters |   
<char> |  Specifies the type of list. Choose from: GUID - the registered GUID of the Cal Type NAME - the registered name of the Cal Type  
Examples |  SENS:CORR:TYPE:CAT? GUID  
Query Syntax |  SENSe<cnum>:CORRection:TYPE:CATalog? <char>  
Return Type |  Comma-separated string  
Default |  Not Applicable  
  
* * *

## SENSe<cnum>:CORRection:WAVE[:METHod] <param>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the wave correction method.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<parm> |  Wave correction method. Choose from: ACTual \- Full error corrected actual waves at DUT plane. MATCh  Matched corrected waves at DUT plane. RESPonse \- Response corrected wave at DUT plane.  
Examples |  SENS1:CORR:WAVE ACT  
Query Syntax |  SENSe<cnum>:CORR:WAVE[:METHod]?  
Return Type |  String  
Default |  MATC  
  
* * *

## SENSe<cnum>:CORRection:WAVE:NORM[:METHod] <param>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the wave normalization method.  
---  
Parameters |   
<cnum> |  Any existing channel number. If unspecified, value is set to 1.  
<parm> |  Wave normalization method. Choose from: POWer \- Waves are computed according to Kurokawa's power wave definition. TRAVeling  Waves are computed according to a traveling wave definition.  
Examples |  SENS1:CORR:WAVE:NORM POW  
Query Syntax |  SENSe<cnum>:CORR:WAVE:NORM[:METHod]?  
Return Type |  String  
Default |  POW  
  
* * *


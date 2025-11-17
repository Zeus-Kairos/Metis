# Differential I/Q Commands

* * *

Controls the Differential I/Q configuration.

Diff IQ Setup Dialog  
---  
![](../../../assets/images/IQSetupDiag.gif) | [SENSe:DIQ:FREQ:RANGe:ADD](DIQ.md#FrRangeAdd)  
SENSe:DIQ:FREQ:RANGe:COUNt  
[SENSe:DIQ:FREQ:RANGe:DELete](DIQ.md#FrRangeDelete)  
Range Settings Dialog |  | SCPI  
---|---|---  
![](../../../assets/images/DIQRangeSettingsDialog.png) | Frequency | [SENSe:DIQ:FREQ:RANGe:STARt](DIQ.md#FrRangeStart)  
[SENSe:DIQ:FREQ:RANGe:STOP](DIQ.md#FrRangeStop)  
[SENSe:DIQ:FREQ:RANGe:IFBW](DIQ.md#FrRangeIFBW)  
Coupling | [SENSe:DIQ:FREQ:RANGe:COUPle:STATe](DIQ.md#FrRangeCplState)  
[SENSe:DIQ:FREQ:RANGe:COUPle:ID](DIQ.md#FrRangeCplID)  
[SENSe:DIQ:FREQ:RANGe:COUPle:OFFSet](DIQ.md#FrRangeCplOffset)  
[SENSe:DIQ:FREQ:RANGe:COUPle:UCONvert](DIQ.md#FrRangeCplUconv)  
[SENSe:DIQ:FREQ:RANGe:COUPle:MULTiplier](DIQ.md#FrRangeCplMult)  
[SENSe:DIQ:FREQ:RANGe:COUPle:DIvisor](DIQ.md#FrRangeCplDivisor)  
Source Configuration Dialog | SCPI  
---|---  
![](../../../assets/images/IQSourceConfigDiag1a.png) |  | [SENSe:DIQ:PORT:STATe](DIQ.md#PortState)  
[SENSe:DIQ:PORT:RANGe](DIQ.md#PortRange)  
[SOURce:PHASe:EXTernal:CATalog?](../SourcePhase.md#SOURce:PHASe:EXTernal:CATalog)
[SOURce:PHASe:EXTernal:PORT](../SourcePhase.md#SOURce:PHASe:EXTernal:PORT)  
Power | [SENSe:DIQ:PORT:POWer:SWEep](DIQ.md#PortPowerSwp)  
[SENSe:DIQ:PORT:POWer:STARt](DIQ.md#PortPowerStart)  
[SENSe:DIQ:PORT:POWer:STOP](DIQ.md#PortPowerStop)  
[SENSe:DIQ:PORT:POWer:ALC:MODE](DIQ.md#PortPowerALC)  
[SENSe:DIQ:PORT:POWer:ATT](DIQ.md#PortPowerAtten)  
[SENSe:DIQ:PORT:POWer:ATT:AUTO](DIQ.md#PortPowerAttenAuto)  
Phase | [SENSe:DIQ:PORT:PHASe:STATe](DIQ.md#PortPhaseState)  
[SENSe:DIQ:PORT:PHASe:SWEep](DIQ.md#PortPhaseSweep)  
[SENSe:DIQ:PORT:PHASe:STARt](DIQ.md#PortPhaseStart)  
[SENSe:DIQ:PORT:PHASe:STOP](DIQ.md#PortPhaseStop)  
[SENSe:DIQ:PORT:PHASe:REF](DIQ.md#PortPhaseRef)  
[SENSe:DIQ:PORT:PHASe:PAR](DIQ.md#PortPhasePar)  
[SOURce:PHASe:CONTrol:TOLerance](../SourcePhase.md#tolerance)  
[SOURce:PHASe:CONTrol:ITERation](../SourcePhase.md#iteration)  
Match Correction | [SENSe:DIQ:PORT:MATCh:STATe](DIQ.md#PortMatchState)  
[SENSe:DIQ:PORT:MATCh:TREC](DIQ.md#PortMatchTrec)  
[SENSe:DIQ:PORT:MATCh:RREC](DIQ.md#PortMatchRRec)  
[SENSe:DIQ:PORT:MATCh:RANG](DIQ.md#PortMatchRange)  
Edit Parameters Dialog | SCPI  
---|---  
![](../../../assets/images/IQEditParamsDiag.gif) | [SENSe:DIQ:PARameter:DEFine](DIQ.md#parDefine)  
[SENSe:DIQ:PARameter:DELete](DIQ.md#paramDelete)  
[SENSe:DIQ: PARameter:CATalog?](DIQ.md#paramCat)  
[SENSe:DIQ:SAVE](DIQ.md#save)  
[SENSe:DIQ:LOAD](DIQ.md#load)  
  
Click on a keyword to view the command details.

### See Also

  * [CALC:MEAS:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine) \- creates a Differential IQ measurement.

  * [Select X-Axis commands](../Calculate/MeasureX.md)

  * Calibration uses the [Guided Calibration commands](../../COM_Reference/Objects/GuidedCalibration_Object.md).

  * [Example Program](../../GPIB_Example_Programs/Create_and_Cal_a_Diff_IQ_Measurement.md)

  * [Learn about DIQ](../../../Applications/Differential_IQ.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

* * *

## SENSe<ch>:DIQ:FREQuency:RANGe:ADD

Applicable Models: All with option S9x089A/B (Write-only) Adds a frequency
range using the next available range name. For example, with the default F1
range name present, sending this command will create F2. On the [Measurement
Setup dialog](../../../Applications/Differential_IQ.htm#SetupDiag) this is the
New setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
Examples | SENS:DIQ:FREQ:RANG:ADD sense2:diq:frequency:range:add  
Query Syntax | Not applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe:COUNt?

Applicable Models: All with option S9x089A/B (Read-only) Returns the number of
frequency ranges in the DIQ channel.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
Examples | SENS:DIQ:FREQ:RANG:COUN?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:COUPle:DIVisor <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
value by which the coupled range will be divided to achieve the frequency
range specified by <rNum>. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Divisor setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number.  
<value> | Divisor value. Choose a positive or negative integer.  
Examples | SENS:DIQ:FREQ:RANG1:COUP:DIV 1 sense2:diq:frequency:range2:couple:divisor 2  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:COUPle:DIVisor?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:COUPle:ID <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
frequency range to couple settings to. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the range to Couple To setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number to be coupled. Range 1 can NOT be coupled to another range.  
<value> | Frequency range number to couple to. This range should be already created using [SENS:DIQ:FREQ:RANGe:ADD](DIQ.md#FrRangeAdd)  
Examples | SENS:DIQ:FREQ:RANG2:COUP:ID 3 sense2:diq:frequency:range2:couple:id 1  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:COUPle:ID?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:COUPle:MULTiplier <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
value by which the coupled range will be multiplied to achieve the frequency
range specified by <rNum>. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Multiplier setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number.  
<value> | Multiplier value. Choose a positive or negative integer.  
Examples | SENS:DIQ:FREQ:RANG1:COUP:MULT 2 sense2:diq:frequency:range2:couple:multiplier 1  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:COUPle:MULTiplier?  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:COUPle:OFFSet <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
frequency range number to be used as an offset. The frequencies of the range
<rNum> will be offset from the 'coupled to' range by this frequency range. The
[SENS:DIQ:FREQ:RANG:COUP:UCON](DIQ.md#FrRangeCplUconv) command determines
whether the offset is positive or negative. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Offset setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number.  
<value> | Offset range number. The resulting range must be within the frequency range of the analyzer.  
Examples | SENS:DIQ:FREQ:RANG1:COUP:OFFS 2 sense2:diq:frequency:range3:couple:offset 2 'range 3 is offset from the 'coupled to' range by the frequencies defined by range 2  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:COUPle:OFFSet?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:COUPle:STATe <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
ON / OFF state of frequency range coupling. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Couple (On|Off) setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number.  
<value> | (Boolean) Choose from:

  * ON or 1 - Range is coupled
  * OFF or 0 - Range is NOT coupled

  
Examples | SENS:DIQ:FREQ:RANG1:COUP:STAT 1 sense2:diq:frequency:range2:couple:state off  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:COUPle:STATe?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF (0)  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:COUPle:UCONvert <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
state of the Up / Down conversion setting. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Coupling, this is the Up (On|Off) setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number.  
<value> | (Boolean) Choose from:

  * ON or 1 - The offset range is ADDED to the 'coupled to' frequency range.
  * OFF or 0 - The offset range is SUBTRACTED from to the 'coupled to' frequency range.

  
Examples | SENS:DIQ:FREQ:RANG1:COUP:UCONvert 1 sense2:diq:frequency:range2:couple:uconvert off  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:COUPle:UCONvert?  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:DELete

Applicable Models: All with option S9x089A/B (Write-only) Deletes the
specified frequency range. On the [Measurement Setup
dialog](../../../Applications/Differential_IQ.htm#SetupDiag) this is the
Remove setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | Frequency range number to delete.  
Examples | SENS:DIQ:FREQ:RANG1:DEL sense2:diq:frequency:range2:delete  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:IFBW <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
receiver IF bandwidth setting. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Frequency, this is the IFBW setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | (Integer) Frequency range number.  
<value> | (Numeric) IF Bandwidth in Hz. The list of valid IF Bandwidths is different depending on the analyzer model. ([See the list](../../../S2_Opt/Trce_Noise.md#IFDiag).) If an invalid number is specified, the analyzer will round up to the closest valid number.  
Examples | SENS:DIQ:FREQ:RANG1:IFBW 1e3 sense2:diq:frequency:range2:ifbw 100e3  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:IFBW?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1e5  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:STARt <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
start value for the specified frequency range. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Frequency, this is the Start setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | (Integer) Frequency range number.  
<value> | (Numeric) Frequency range start value. Choose a value within the frequency range of the analyzer.  
Examples | SENS:DIQ:FREQ:RANG1:STAR 1e9 sense2:diq:frequency:range2:start 20e6  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:STARt?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Start frequency of the analyzer  
  
* * *

## SENSe<ch>:DIQ:FREQuency:RANGe<rNum>:STOP <value>

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
stop value for the specified frequency range. On the [Frequency
Range](../../../Applications/Differential_IQ.htm#RangeDiag) dialog under
Frequency, this is the Stop setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<rNum> | (Integer) Frequency range number.  
<value> | (Numeric) Frequency range stop value. Choose a value within the frequency range of the analyzer.  
Examples | SENS:DIQ:FREQ:RANG1:STOP 10e9 sense2:diq:frequency:range2:stop 500e6  
Query Syntax | SENSe<ch>:DIQ:FREQuency:RANGe<num>:STOP?  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Maximum frequency of the analyzer.  
  
* * *

## SENSe<ch>:DIQ:LOAD <filename>[,<type>]

Applicable Models: All with option S9x089A/B (Write-only) Recalls the list of
parameters and frequency ranges settings from a previously-saved *.xml file.
Use [SENSe:DIQ:SAVE](DIQ.md#save) to store the files. Note: The Frequency
Range settings and the DIQ Parameters are saved and recalled from a single
*.xml file.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<filename> | (String) Full path (optional) and filename with or without the *.xml extension. If the full path is not provided, the file is saved to the D:\ drive.  
<type> | (Character) Choose the type of settings to be recalled: PLISt \- just the parameters. FRANge \- just the frequency settings. ALL \- both parameters and frequency settings.  
Examples | SENS:DIQ:LOAD "myDIQfile",ALL sense2:diq:load "D:\myDIQfile.xml",plist  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | PLISt  
  
* * *

## SENSe<ch>:DIQ:SAVE <filename>

Applicable Models: All with option S9x089A/B (Write-only) Stores the list of
parameters and frequency ranges settings to an*.xml file for recall at a later
time. Use [SENSe:DIQ:LOAD](DIQ.md#load) to recall files. Note: The Frequency
Range settings and the DIQ Parameters are saved and recalled from a single
*.xml file.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<filename> | (String) Full path (optional) and filename with or without the *.xml extension. If the full path is not provided, the file is saved to the D:\ drive.  
Examples | SENS:DIQ:SAVE "myDIQfile" sense2:diq:save "D:\myDIQfile.xml"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:DIQ:PARameter:CATalog?

Applicable Models: All with option S9x089A/B (Read-only) Returns a list of all
existing parameters.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<name> | (String) Comma-separated list of parameters, each parameter in the form name:expression.  
Examples | SENS:DIQ:PAR:CAT? sense2:diq:parameter:catalog? 'Example of returned parameters "IPwrF1:a1_F1","OPwrF1:b2_F1","GainF1:b2_F1/a1_F1"  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:DIQ:PARameter:DEFine <name>,<expression>

Applicable Models: All with option S9x089A/B (Write-only) Create a new
parameter for Differential IQ channel. Use
[CALCulate:MEASure:DEFine](../Calculate/Measure.md#CALCulate:MEASure:DEFine)
to create a new trace with the new parameter. Use
[CALCulate:MEASure:PARameter](../Calculate/MeasurePARameter.md#CALCulate:MEASure:PARameter)
to change the parameter of one of the existing traces to the new parameter.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<name> | (String) Parameter name. Note: Do not use underscores in the parameter name. For example, b2_f1 cannot be used as a parameter name. However, b2f1 is a valid parameter name.  
<expression> | (String) Parameter expression using receiver names and mathematical expressions.  
Examples | SENS:DIQ:PAR:DEF "myNewParam","(a1_F1+b1_F2)/c1" sense2:diq:parameter:define "myNewParam","(a1_F1+b1_F2)/c1"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:DIQ:PARameter:DELete <name>

Applicable Models: All with option S9x089A/B (Write-only) Deletes the named
parameter.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<name> | (String) Parameter name that was used when the parameter was created.  
Examples | SENS:DIQ:PAR:DEL "myNewParam" sense2:diq:parameter:delete "myNewParam"  
Query Syntax | Not Applicable  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:MATCh:RANGe <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
existing frequency ranges over which Match Correction is to be performed. On
the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Match Frequency Range setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (String) Frequency ranges, including the "F<n>", where <n> is the range number. Separate each range with a comma.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:MATC:RANG "F1,F2,F3" sense2:diq:port3:match:range "F1", "Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT:RANGe? [src]  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depends on <port>  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:MATCh:RRECeiver <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
reference receiver to be used to perform Match Correction. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Reference Receiver setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (String) Choose any of the reference receivers in the analyzer using logical receiver notation. [Learn more](../../../S1_Settings/Measurement_Parameters.md#RecNotation). These would be "a_" where _ is the test port number.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT2:MATC:RREC "a2" 'port 2 reference receiver sense2:diq:port3:match:rreceiver "a1","Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT:RRECeiver? [src]  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depends on <port>  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:MATCh:STATe <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
Match Correction ON/OFF state. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Match Correction ON setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Boolean) Choose from:

  * ON or 1 - Perform Match Correction
  * OFF or 0 - Do not perform Match Correction.

  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:MATC:STAT 1 sense2:diq:port3:match:state off,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT:STATe? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:MATCh:TRECeiver <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
test port receiver to be used to perform Match Correction. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Match Correction, this is the Test Receiver setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (String) Choose any of the test port receivers in the analyzer using logical receiver notation. [Learn more](../../../S1_Settings/Measurement_Parameters.md#RecNotation). These would be "b_" where _ is the test port number.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT3:MATC:TREC "b3" sense2:diq:port3:match:treceiver "b1","Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT:TRECeiver? [src]  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depends on <port>  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:PHASe:PARameter <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
receivers to be used to measure the phase of the sources. The phase
measurement will be the difference between these two receivers. Select the
receivers based on your application. You are responsible to make sure that
your DUT configuration routes the signals of interest to the correct
receivers. Otherwise, the phase will not be properly controlled. On the
[Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Control Receiver setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (String) Phase parameter using the following syntax: rCont/rRef Where:

  * rCont is the receiver used to measure the controlled source.
  * rRef is the receiver used to measure the reference source.

Only logical receiver notation (a1,b1) is available. [Learn
more](../../../S1_Settings/Measurement_Parameters.htm#RecNotation). Enclose
the entire parameter in quotes.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:PHAS:PAR "a1/a3" sense2:diq:port3:phase:parameter "b2/a2","Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:PHASe:PARameter? [src]  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not applicable  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:PHASe:REFerence <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
port to be used as a reference when controlling phase for the specified
<port>. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Refer To setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (String) Reference port. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. The two internal VNA sources are available ONLY at specific ports. For example on a 4-port PNA-X, the possible port pairings are: 1/3, 1/4, 2/3, or 2/4. Port 1 can NOT be paired with Port 2, and Port 3 can NOT be paired with Port 4. [Learn more about these limitations.](../../../S0_Start/Internal_Second_Source.md#Restrictions)  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:PHAS:REF "port 2" sense2:diq:port3:phase:reference "Port 3","Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:PHASe:REFerence? [src]  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Depends on <port>  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:PHASe:STARt <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
start value for a phase sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Start Phase setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Numeric) Start phase sweep value in degrees. Choose any positive or negative value.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:PHAS:STAR -90 sense2:diq:port3:phase:start 0,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:PHASe:STARt? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:PHASe:STATe <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
ON/ OFF state of phase control. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Phase State setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Character) Phase control state. Choose from: OFF \- Phase is NOT set or controlled. CONTrolled \- Phase is measured and iterated to within the specified tolerance. Specify the receivers and iteration properties using the [Source:Phase](../SourcePhase.md) commands. OPENloop \- Phase is set, but receivers are NOT used to measure and iterate the phase of the source. Therefore, the setting of phase is not as accurate or stable. Open Loop mode can be used with phase sweep (for example, from 0 to 360 degrees). However, each sweep may not start at 0 degrees. NO settings on the Phase Control Setup dialog are used in Open Loop. Note: After selecting Open Loop, set each source to ON (not Auto).  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:PHAS:STAT OFF sense2:diq:port3:phase:state controlled,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:PHASe:STATe? [src]  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:PHASe:STOP <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
stop value for a phase sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Stop Phase setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Numeric) Stop phase sweep value in degrees. Choose any positive or negative value.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:PHAS:STOP 270 sense2:diq:port3:phase:stop "Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:PHASe:STOP? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:PHASe:SWEep[:STATe] <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
ON / OFF state of phase sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Phase, this is the Sweep Phase (On|Off) setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Boolean) Choose from:

  * ON or 1 - Sweep phase.
  * OFF or 0 - Do not sweep phase.

  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:PHAS:SWE 1 sense2:diq:port3:phase:sweep:state off,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:PHASe:SWEep[:STATe]? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:POWer:ALC:MODE <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
leveling mode to be used for the specified source port. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Leveling Mode setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (String) Leveling mode. Choose from: "Internal" \- Standard internal analyzer leveling mode. "Internal-<n>,<p>" \- Receiver Leveling, where: <n> is the receiver name. <p> is the source port to be leveled. "Open Loop" \- Open loop leveling, used during pulse conditions with the internal source modulators. NOT available on all models. No leveling is used in setting the source power. The lowest settable power, without attenuation, is limited to -30dBm. The source power level accuracy is very compromised. Use a source power calibration to make the source power somewhat more accurate. "Open Loop-<n>,<p>" \- Open loop leveling, where: <n> is the receiver name. <p> is the source port to be leveled  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:POW:ALC:MODE "Internal" sense2:diq:port3:power:alc:mode "Internal-a2,1","Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:POWer:ALC:MODE? [src]  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | "Internal"  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:POWer:ATTenuation <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
amount of source attenuation. Sending this command will set
[SENS:DIQ:PORT:POW:ATT:AUTO](DIQ.md#PortPowerAttenAuto) OFF On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Source Attenuation setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Numeric) Source Attenuation value. Choose from 0 to the maximum amount of source attenuation in the correct step size. Rounding will occur when the selected value can not be achieved. [See attenuators for all VNA models](../../../Support/Configurations.md).  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:POW:ATT 10 sense2:diq:port3:power:attenuation 0,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:POWer:ATTenuation? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 0  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:POWer:ATTenuation:AUTO <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
ON/ OFF state of auto range source attenuation. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Auto range source attenuator setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Boolean) Choose from:

  * ON or 1 - Auto range the source attenuation.
  * OFF or 0 - Do not Auto range the source attenuation.

  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:POW:ATT:AUTO 1 sense2:diq:port3:power:attenuation:auto off,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:POWer:ATTenuation:AUTO? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | ON  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:POWer:STARt <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
start value of a power sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Start Power setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Numeric) Power sweep start value in dBm. Choose start and stop value within a single attenuator range of the analyzer (generally about 30 dB).  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:POW:STAR -10 sense2:diq:port3:power:start 0,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:POWer:STARt? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -5 dBm  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:POWer:STOP <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
stop value of a power sweep. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Stop Power setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Numeric) Power sweep stop value in dBm. Choose start and stop value within a single attenuator range of the analyzer (generally about 30 dB).  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:POW:STOP 0 sense2:diq:port3:power:stop 2,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:POWer:STOP? [src]  
Return Type | Numeric  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | -5 dBm  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:POWer:SWEep[:STATe] <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
state of sweeping power. On the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog under Power, this is the Sweep Power (On|Off) setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Boolean) Sweep Power state. Choose from:

  * ON or 1 - Perform power sweep.
  * OFF or 0 - Do not perform power sweep.

  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:POW:SWE 1 sense2:diq:port3:power:sweep:state off, "Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT<port>:POWer:SWEep[:STATe]? [src]  
Return Type | Boolean  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | OFF  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:RANGe <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
frequency range number to which the specified source port will be set. At the
top of the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog this is the Frequency Range setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port number.  
<value> | (Integer) Frequency range number.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:RANG 1 sense2:diq:port3:range 2,"Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT:RANGe? [src]  
Return Type | Integer  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | 1  
  
* * *

## SENSe<ch>:DIQ:PORT<port>:STATe <value>[,<src>]

Applicable Models: All with option S9x089A/B (Read-Write) Sets and reads the
ON / OFF state of the source specified by <port>. At the top of the [Source
Configuration](../../../Applications/Differential_IQ.htm#SourceConfigurationDiag)
dialog this is the Source State setting.  
---  
Parameters |   
<ch> | The Differential IQ channel number. If unspecified, value is set to 1.  
<port> | (Integer) Source port name.  
<value> | (Character) Choose from: AUTO \- Source power is turned ON at the specified test port when required by the measurement. This is the most common (default) setting. Auto sources are turned OFF when other sources are performing Match Correction sweeps. ON \- Source power is ALWAYS ON, regardless of measurements that are in process. Use this setting to supply source power to a DUT port that always requires power, such as an LO port. This could turn OFF power at another test port. [Learn about internal second source restrictions](../../../S0_Start/Internal_Second_Source.md). OFF \- Source power is never ON, regardless of the measurement requirements. Use this setting to prevent damage to a sensitive DUT test port.  
<src> | String. (NOT case sensitive). Source port. Optional. Use [SOUR:CAT?](../source.md#Cat) to return a list of valid port names. While this argument can be used to make settings for ALL ports, it is designed to access ports such as an external source, true mode balanced port, or one of the Source outputs on the 2-port VNA-x model with multiple sources such as "Port 1 Src2". Otherwise, the <port> argument performs the same function. If both arguments are specified, [src] takes priority.  
Examples | SENS:DIQ:PORT1:STAT Auto sense2:diq:port3:state On, "Port 1 Src2"  
Query Syntax | SENSe<ch>:DIQ:PORT:STATe? [src]  
Return Type | Character  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Auto  
  
* * *


# CALCulate:MEASure:DATA Commands

Controls writing and reading VNA measurement data.

CALCulate:MEASure: DATA | BUFFer? | X | Y | FDATa | FMEMory | RAW | CATalog? | SDATa | SMEMory | SNP? | PORTs? | SAVE | X | AXIS | DOMain | FIXed | PARameter | VALue | [:VALues]  
---  
  
Click a keyword to view the command details.

See Also

  * [Calibrating with SCPI](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

  * See [CALCulate:MEASure:X:VALues](MeasureX.md#CALCulate:MEASure:X:VALues) for stimulus point data.

* * *

## (Write) CALCulate<cnum>:MEASure<mnum>:DATA:<char> <data>

(Read) CALCulate<cnum>:MEASure<mnum>:DATA:<char>?

Applicable Models: All Reads or writes Measurement data, Memory data, or
Normalization Divisor data from the [Data Access Map](../../DataMapSet.md)
location.

  * For Measurement data, use FDATA or SDATA
  * For Memory data, use FMEM or SMEM. When querying memory, you must first store a trace into memory using [CALC:MEAS:MATH:MEMorize](Measure.md#CALCulate:MEASure:MATH:MEMorize).
  * For Normalization Divisor (Receiver Power Cal error term) data, use SDIV.
  * Use [FORMat:DATA](../Format_SCPI.md#fd) to change the data type (<REAL,32>, <REAL,64> or <ASCii,0>).
  * Use [FORMat:BORDer](../Format_SCPI.md#fb) to change the byte order. Use NORMal when transferring a binary block from LabView or VEE. For other programming languages, you may need to "SWAP" the byte order.

[Equation Editor](../../../S4_Collect/Equation_Editor.md) Notes:

  * When equation editor is active on a trace in a standard S-parameter channel, Calc:Data returns the data from the parameter on the trace that was measured last. For example, for the equation "S22 + S33 + S11, then S33 is the last measured parameter because it uses source port 3.
  * In [applications](../../../Applications/Applications.md), if equation editor is active and the original parameter for the trace is not requested anywhere in the channel, then zeros are returned. If the original parameter is being measured within the channel, then data for the original parameter is returned.
  * In general, if an equation contains no measurement parameters, then data for the original parameter is returned.

Note: The Calc:Data SCORR command to read/write error terms is Superseded with
[SENS:CORR:CSET:DATA](../Sense/CorrCset.md#data). SCORR commands do NOT
accommodate greater than 12 error terms.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<char> |  FDATA |  Formatted measurement data to or from [Data Access Map](../../DataMapSet.md) location. Display (access point 2). Note: When querying FDATA, data is received in degrees. When setting phase using FDATA, the command expects the data in radians.

  * Corrected data is returned when correction is ON.
  * Uncorrected data is returned when correction is OFF.
  * Returns TWO numbers per data point for Polar and Smith Chart format. For both formats, the data is the real and imaginary data. To retrieve the resistance and reactance of a trace of data, use the [Z-Reflection conversion feature](Measure.md#CALCulate:MEASure:CONVersion:FUNCtion).
  * Returns one number per data point for all other formats.
  * Format of the read data is same as the displayed format.

  
|  SDATA |  Complex measurement data. Writes data to [Data Access Map](../../DataMapSet.md) location. Raw Measurement (access point 0). Note: Write access is forbidden on the standard channel if factory calibration is on (applies to ENA/PXI/Streamline, not to PNA); to disable factory calibration use SYST:FCOR:CHAN:COUP:STAT OFF command.

  * When writing corrected data, and correction is ON, it will be corrected again, resulting in meaningless data.
  * For unratioed measurements, the magnitude of the complex number is in sqrt(mW).

Reads data from Apply Error Terms (access point 1).

  * Returns TWO numbers per data point.
  * Corrected data is returned when correction is ON.
  * Uncorrected data is returned when correction is OFF.

  
|  FMEM |  Formatted memory data to or from [Data Access Map](../../DataMapSet.md) location. Memory result (access point 4).

  * Returns TWO numbers per data point for Polar and Smith Chart format.
  * Returns one number per data point for all other formats.
  * Format of the read data is same as the displayed format.
  * Returned data reflects the correction level (ON|OFF) when the data was stored into memory.

  
|  SMEM |  Complex memory data to or from [Data Access Map](../../DataMapSet.md) location. Memory (access point 3).

  * Returns TWO numbers per data point.
  * Returned data reflects the correction level (ON|OFF) when the data was stored into memory.
  * Returned data reflects the correction level (ON|OFF) when the data was stored into memory.

  
Examples |  CALC:MEAS:DATA:FDATA Data(x)  
calculate2:measure2:data:sdata data(r,i) See another
[example](../../GPIB_Example_Programs/Getting_and_Putting_Data_using_GPIB.md)
using this command.  
Return Type |  [Block data](../../Learning_about_GPIB/Getting_Data_from_the_Analyzer.md#block) |   
Default |  Not Applicable |   
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:BUFFer:X? <bufferName>

Applicable Models: All (Read-only) Retrieves frequency tone data from the
modulation distortion measurement.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<bufferName> |  (string)  Name of the buffer to be read. Note: The following names assume a 2-port VNA. Also, by default, the parameter names assume that VNA Port 1 is connected to the DUT input and VNA Port 2 is connected to the DUT output. If the RF Path settings are changed from the default, the names will change accordingly. For example, if the VNA has 4 ports and Port 4 is connected to the DUT output, the names will change to "PIn1", "POut4", "S11", "S41", etc. Choose from: "POut2" \- Power Out "PIn1" \- Power In "MSig2" \- Modulation Signal Out "MDist2" \- Modulation Distortion Out "MGain21" \- Modulation Gain "MComp21" \- Modulation Compression "PGain21" \- Power Gain "S11" \- Linear Input Match "S21" \- Linear Gain "LPin1" \- Linear Power In "LPOut1" \- Linear Reflected Power In "LPOut2" \- Linear Power Out  
Examples |  CALC:MEAS1:DATA:BUFF:X? "POut2"  
Return Type |  Depends on [FORM:DATA](../Format_SCPI.md#fd) command  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:BUFFer:Y? <bufferName>

Applicable Models: All (Read-only) Retrieves trace data (Y data) from the
modulation distortion measurement.  For un-ratioed parameters, the format of
the data is √mW. This includes these parameters, POut2, PIn1, Pout1, LPOut1,
LPOut2  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<bufferName> |  (string)  Name of the buffer to be read. Note: The following names assume a 2-port VNA. Also, by default, the parameter names assume that VNA Port 1 is connected to the DUT input and VNA Port 2 is connected to the DUT output. If the RF Path settings are changed from the default, the names will change accordingly. For example, if the VNA has 4 ports and Port 4 is connected to the DUT output, the names will change to "PIn1", "POut4", "S11", "S41", etc. Choose from: "POut2" \- Power Out "PIn1" \- Power In "MSig2" \- Modulation Signal Out "MDist2" \- Modulation Distortion Out "MGain21" \- Modulation Gain "MComp21" \- Modulation Compression "PGain21" \- Power Gain "S11" \- Linear Input Match "S21" \- Linear Gain "LPin1" \- Linear Power In "LPOut1" \- Linear Reflected Power In "LPOut2" \- Linear Power Out  
Examples |  CALC:MEAS1:DATA:BUFF:Y? "POut2"  
Return Type |  Depends on [FORM:DATA](../Format_SCPI.md#fd) command  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:RAW <string>,<dataBlock>

Applicable Models: All (Write-Read) Sets the raw data for the specified raw
parameter buffer. For unratioed parameters, the source port separator can be
either , or _. This command applies to a Standard channel only.
Application channels will return an error.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<string> |  String - (Not case-sensitive) Raw parameter buffer. For example, "S11".  
<dataBlock> |  String - (Not case-sensitive) Raw measurement data.  
Examples |  CALC:MEAS:DATA:RAW "S11",5.85E-002,-7.0E-002,+9.80E-003,+5.40E-002,+2.26E-002,+6.25E-002,-3.47E-002,+4.00E-002 calculate:measure:data:raw "S11",5.85E-002,-7.0E-002,+9.80E-003,+5.40E-002,+2.26E-002,+6.25E-002,-3.47E-002,+4.00E-002  
Query Syntax |  CALCulate<ch>:MEASure<mnum>:DATA:RAW? "<string>"  
Return Type |  [Block data](../../Learning_about_GPIB/Getting_Data_from_the_Analyzer.md#block)  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:RAW:CATalog?

Applicable Models: All (Read-only) Returns the list of raw parameters
associated with the measurement <mnum>. These are the raw parameters that are
actually used by the error correction; the <mnum> measurement may not strictly
depend on all of those. For example, 2 port S-parameters. If the DUT has
transmission, then changing raw S11 will modify the corrected S22. If
transmission is negligible, S22 is unaffected. The list is returned as strings
comma separated. For unratioed parameters, the source port separator is _
instead of , to avoid confusion in tokenization. This command applies to a
Standard channel only. Application channels will return an error.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
Example |  CALC:MEAS1:DATA:RAW:CAT?  
Return Type |  String  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:SNP? <n>

Applicable Models: All (Read-only) Reads SnP data from the selected measurement. [Learn more about SnP data](../../../S5_Output/SaveRecall.md#An *.s3p).  This command is valid ONLY with standard S-parameter measurements. |  Notes

  * This command returns SNP data without header information, and in columns, not in rows as .SnP files. This means that the data returned from this command sends all frequency data, then all Sx1 magnitude or real data, then all Sx1 phase or imaginary data, and so forth.
  * To avoid frequency rounding errors, specify [FORMat:DATA](../Format_SCPI.md#fd) <Real,64> or <ASCii, 0>

  
---  
  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<n> |  Amount of data to return. If unspecified, <n> is set to 2. The number you specify must be less than or equal to the number of available ports on the VNA. Choose from: **1 (S1P) returns 1-Port data for the active measurement if the active measurement is a reflection parameter such as S11 or S22. The behavior is UNDEFINED if the active measurement is a transmission parameter such as an S21**. 2 (S2P) returns data for the four 2 port parameters associated with the current measurement. Default. Data that is not available is zero-filled. 3 (S3P) returns data for the nine 3 port parameters associated with the current measurement. Data that is not available is zero-filled. 4 (S4P) returns data for the sixteen 4 port parameters associated with the current measurement. Data that is not available is zero-filled. SnP data can be output using several data formatting options. See [MMEM:STORe:TRACe:FORMat:SNP](../Memory.md#snp). See also [MMEM:STOR <file>.<snp>](../Memory.md#save)  
Examples |  CALC:MEAS1:DATA:SNP? 1  
Return Type |  Depends on [FORMat:DATA](../Format_SCPI.md#fd).  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:SNP:PORTs? <"x,y,z".>

Applicable Models: All (Read-only) Reads SNP data from the selected measurement for the specified ports. [Learn more about SNP data](../../../S5_Output/SaveRecall.md#An *.s3p). This command is valid ONLY with standard S-parameter measurements. |  Notes

  * This command returns SNP data without header information, and in columns, not in rows as .SnP files. This means that the data returned from this command sends all frequency data, then all Sx1 magnitude or real data, then all Sx1 phase or imaginary data, and so forth.
  * To avoid frequency rounding errors, specify [FORM:DATA](../Format_SCPI.md#fd) <Real,64> or <ASCii, 0>
  * Data that is not available is zero-filled.
  * For sweeps with a large number of data points, always follow this command with *OPC? [Learn more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  
---  
  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<"x,y,z"> |  Comma or space delimited port numbers for which data is requested, enclosed in quotes. SNP data can be output using several data formatting options. See [MMEM:STORe:TRACe:FORMat:SNP](../Memory.md#snp).  
Examples |  CALC:MEAS2:DATA:SNP:PORTs? "1,2,4,5,7" 'read data for these ports  
Return Type |  Depends on [FORMat:DATA](../Format_SCPI.md#fd)  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:SNP:PORTs:SAVE <"x,y,z">,<filename>[,
FAST] - Superseded

The command is replaced with
[MMEMory](../Memory.md#StoDataSnp)[:STORe:DATA:SNP](../Memory.md#StoDataSnp).
Applicable Models: All (Write-only) Saves SNP data from the selected
measurement for the specified ports. [Learn more about SNP
data](../../../S5_Output/SaveRecall.htm#An *.s3p).

  * The Normal vs Mixed Mode selection is NOT used as it is in the [Choose Ports dialog](../../../S5_Output/SaveRecall.md#ChoosePorts). Instead, data is returned as it is displayed on the trace. If the selected measurement is Mixed Mode (balanced), then balanced data is returned. If the selected measurement is an S-parameter, then S-parameter data is returned.
  * This command is valid ONLY with the Standard measurement class (NOT applications).
  * Data that is not available is zero-filled.
  * For sweeps with a large number of data points, always follow this command with *OPC? [Learn more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<"x,y,z"> |  String Comma or space delimited port numbers for which data is requested, enclosed in quotes.  
<filename> |  String Path, filename, and suffix of location to store the SNP data, enclosed in quotes. The suffix is not checked for accuracy. If saving 2 ports, specify "filename.s2p"; If saving 4 ports, specify "filename.s4p.", and so forth. SNP data can be output using several data formatting options. See [MMEM:STORe:TRACe:FORMat:SNP](../Memory.md#snp).  
[, FAST] |  Reduce the saving time [:SENS:CORR:CACH:MODE](../Sense/Sense_Correction.md#CacMode) should be set at ON.  
  
The correction must cover all the ports of the SNP port list.  The active
measurement must be a corrected S Parameter defined by the port list for the
SNP requests. EG: "S33" is not a proper selected measurement with
CALC:DATA:SNP:PORTS? <1,2>  
Examples |  CALC:MEAS2:DATA:SNP:PORTs:Save '1,2,4','D:\MyData.s3p';*OPC?  
Return Type |  Depends on [FORMat:DATA](../Format_SCPI.md#fd)  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:X:AXiS <string>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA, M983xA (Write-Read)
Sets the X-axis of the selected measurement to a DC Source. This command does
not change the default setting for new traces.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<string> |  String - (Not case-sensitive) For all channels EXCEPT DIQ, choose from the following: "Default" \- The default X-axis setting for the selected measurement. For Application measurements, the X-Axis domain is set with specific commands. "AO1" \- Internal DC source #1 "AO2" \- Internal DC source #2 Note: For DIQ channels, see CALC:MEAS:X:AXIS:DOMain For Modulation Distortion Channels (MOD), choose from: "SA Frequency" \- SA display showing the SA frequency settings. "Power In" \- Displays input power sweep. "Power Out" \- Displays output power sweep. "Measured Carrin" \- Measured input band power. "Measured CarrOut" \- Measured output band power. For Modulation Distortion Converters Channels (MODX), choose from: "SA Freq In" \- SA display showing mixer input range. "SA Freq Out" \- SA display showing mixer output range. "Power In" \- Displays input power sweep. "Power Out" \- Displays output power sweep. "Measured Carrin" \- Measured input band power. "Measured CarrOut" \- Measured output band power.  
Examples |  CALC:MEAS:DATA:X:AXIS 'Default' calculate:measure:data:x:axis "AO1"  
Query Syntax |  CALCulate<ch>:MEASure<mnum>:DATA:X:AXIS?  
Return Type |  String  
Default |  "Default"  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:X:AXIS:DOMain <string>

Applicable Models: N522xB, N523xB, N524xB, M983xA (Write-Read) Sets and
returns the X-Axis domain of the selected DIQ measurement.  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
|  |  Choose one of these: |  Then set X-Axis Source (CALC:MEAS:DATA:X:AXIS) using one of these as the argument.  
---|---  
"Frequency" |  "F1", "F2", etc.  
"Power" |  Source port: "Port 1", "Port 2", etc.  
"Phase" |  Source port: "Port 1", "Port 2", etc.  
"DC" |  DC Source:"AO1", "AO2"  
"Points" |  "Points"  
Example |  1\. CALC:MEAS:DATA:X:AXIS:DOM "Power" 2\. CALC:MEAS:DATA:X:AXIS "Port 1"  
Query Syntax |  CALCulate<ch>:MEASure<mnum>:DATA:X:AXIS:DOMain?  
Return Type |  String  
Default |  CALC:MEAS:DATA:X:AXIS:DOMain: "Frequency" CALC:MEAS:DATA:X:AXIS: "F1"  
  
* * *

## CALCulate<ch>:MEASure<mnum>:DATA:X:AXIS:FIXed:PARameter <string>

Applicable Models: N524xB models with Option S93070xB (Write-Read) Sets the
X-axis fixed parameter for a power sweep measurement in a Modulation
Distortion channel.  
---  
Parameters |   
<ch> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<string> |  String - (Not case-sensitive) For Modulation Distortion Channels (MOD), choose from: "SA Frequency" \- SA display showing the SA frequency settings. For Modulation Distortion Converters Channels (MODX), choose from: "SA Freq In" \- SA display showing mixer input range. "SA Freq Out" \- SA display showing mixer output range.  
Examples |  CALC:MEAS2:DATA:X:AXIS:FIX:PAR "SA Frequency" calculate:measure2:data:x:axis:fixed:parameter "SA Freq In"  
Query Syntax |  CALCulate<ch>:MEASure<mnum>:DATA:X:AXIS:FIXed:PARameter?  
Return Type |  String  
Default |  "SA Frequency"  
  
* * *

## CALCulate<ch>:MEASure<mnum>:DATA:X:AXIS:FIXed:PARameter:VALue <num>

Applicable Models: N524xB models with Option S93070xB (Write-Read) Sets the
X-axis fixed parameter spectrum analyzer frequency value for a power sweep
measurement in a Modulation Distortion channel.  
---  
Parameters |   
<ch> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
<num> |  Fixed parameter value.  
Examples |  CALC:MEAS2:DATA:X:AXIS:FIX:PAR:VAL 1.5e9 calculate:measure2:data:x:axis:fixed:parameter:value 1.5e9  
Query Syntax |  CALCulate<ch>:MEASure<mnum>:DATA:X:AXIS:FIXed:PARameter:VALue?  
Return Type |  Numeric  
Default |  Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:DATA:X[:VALues]?

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA (Read-only) Returns
the stimulus values for the selected measurement in the current units. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).
This command can be used for all Measurement Classes. Note: To avoid frequency
rounding errors, specify [FORM:DATA](../Format_SCPI.md#fd) <Real,64> or
<ASCii, 0>  
---  
Parameters |   
<cnum> |  Channel number of the measurement (optional).  
<mnum> |  Measurement number for each measurement.  
Examples |  1\. Calc:Par:Sel "MyGCATrace"  
2\. CALC:MEAS:DATA:X?  
Return Type |  Depends on [FORM:DATA](../Format_SCPI.md#fd) command  
Default |  Not applicable  
  
* * *


# Calculate:Data Commands

* * *

Controls writing and reading VNA measurement data.

These commands are Superseded by the [CALCulate:MEASure:DATA](MeasureDATA.md)
commands.

[CALCulate:DATA](Data.md#data) | [CUSTom](Data.md#custom) | [CATalog?](Data.md#cat) | MFData? | MSData? | [SNP?](Data.md#snp) | [PORTs](Data.md#snpReadByPort)? | [SAVE](Data.md#snpSave)  
---  
  
Click on a red keyword to view the command details.

Red is a superseded command.

See Also

  * [Example Programs](../../GPIB_Example_Programs/SCPI_Example_Programs.md)

  * [Data Access Map](../../DataMapSet.md)

  * [Synchronizing the Analyzer and Controller](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  * To read receiver data, use [CALC:RDATA?](RData.md)

  * To read error terms, use [SENS:CORR:CSET:DATA](../Sense/CorrCset.md#data)

  * To read SnP measurement data, use [CALC:DATA:SNP?](Data.md#snp)

  * [SCPI Command Tree](../SCPI_Command_Tree.md)

Critical Note: CALCulate commands act on the selected measurement. You can
select one measurement for each channel using
[Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).

* * *

## (Write) CALCulate<cnum>:DATA <char>,<data>

## (Read) CALCulate<cnum>:DATA? <char>

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Reads or writes
Measurement data, Memory data, or Normalization Divisor data from the [Data
Access Map](../../DataMapSet.htm) location.

  * For Measurement data, use FDATA, RDATA, or SDATA
  * For Memory data, use FMEM or SMEM. When querying memory, you must first store a trace into memory using [CALC:MATH:MEMorize](Math_Calc.md#cmm).
  * For Normalization Divisor (Receiver Power Cal error term) data, use SDIV
  * Use [FORMat:DATA](../Format_SCPI.md#fd) to change the data type (<REAL,32>, <REAL,64> or <ASCii,0>).
  * Use [FORMat:BORDer](../Format_SCPI.md#fb) to change the byte order. Use NORMal when transferring a binary block from LabView or Vee. For other programming languages, you may need to "SWAP" the byte order.

[Equation Editor](../../../S4_Collect/Equation_Editor.md) Notes:

  * When equation editor is active on a trace in a standard S-parameter channel, Calc:Data returns the data from the parameter on the trace that was measured last. For example, for the equation "S22 + S33 + S11, then S33 is the last measured parameter because it uses source port 3.
  * In [applications](../../../Applications/Applications.md), if equation editor is active and the original parameter for the trace is not requested anywhere in the channel, then zeros are returned. If the original parameter is being measured within the channel, then data for the original parameter is returned.
  * In general, if an equation contains no measurement parameters, then data for the original parameter is returned.

Note: The Calc:Data SCORR command to read / write error terms is Superseded
with [SENS:CORR:CSET:DATA](../Sense/CorrCset.md#data). SCORR commands do NOT
accommodate greater than 12 error terms. [See Critical
Note](Data.htm#Critical)  
---  
Parameters |  |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<char> | FDATA | Formatted measurement data to or from [Data Access Map](../../DataMapSet.md) location Display (access point 2). Note: When querying FDATA, data is received in degrees. When setting phase using FDATA, the command expects the data in radians.

  * Corrected data is returned when correction is ON.
  * Uncorrected data is returned when correction is OFF.
  * Returns TWO numbers per data point for Polar and Smith Chart format.
  * Returns one number per data point for all other formats.
  * Format of the read data is same as the displayed format.

  
| RDATA | Complex measurement data. Writes data to [Data Access Map](../../DataMapSet.md) location Raw Measurement (access point 0), same as SDATA. Note: Write access is forbidden on the standard channel if factory calibration is on (applies to ENA/PXI/Streamline, not to PNA); to disable factory calibration use SYST:FCOR:CHAN:COUP:STAT OFF command. Reads data from [Data Access Map](../../DataMapSet.md) location Raw Measurement (access point 0).

  * Returns TWO numbers per data point.
  * Returned numbers are uncorrected (regardless of correction state)

  
| SDATA | Complex measurement data. Writes data to [Data Access Map](../../DataMapSet.md) location Raw Measurement (access point 0). Note: Write access is forbidden on the standard channel if factory calibration is on (applies to ENA/PXI/Streamline, not to PNA); to disable factory calibration use SYST:FCOR:CHAN:COUP:STAT OFF command. Reads data from Apply Error Terms (access point 1). Note: Writing data to this access point, and then reading the data from this access point, will result in different values if correction or factory cal is ON.

  * Returns TWO numbers per data point.
  * Corrected data is returned when correction is ON.
  * Uncorrected data is returned when correction is OFF.

  
| FMEM | Formatted memory data to or from [Data Access Map](../../DataMapSet.md) location Memory result (access point 4).

  * Returns TWO numbers per data point for Polar and Smith Chart format.
  * Returns one number per data point for all other formats.
  * Format of the read data is same as the displayed format.
  * Returned data reflects the correction level (On|OFF) when the data was stored into memory.

  
| SMEM | Complex measurement data to or from [Data Access Map](../../DataMapSet.md) location Memory (access point 3).

  * Returns TWO numbers per data point.
  * Returned data reflects the correction level (On|OFF) when the data was stored into memory.
  * Returned data reflects the correction level (On|OFF) when the data was stored into memory.

  
| SDIV | Complex data from [Data Access Map](../../DataMapSet.md) location Normalization (5).

  * Returns TWO numbers per data point.
  * If normalization interpolation is ON and the number of points changes after the initial normalization, the divisor data will then be interpolated.
  * When querying the normalization divisor, you must first store a divisor trace using [CALC:NORMalize[:IMMediate]](Normalize.md#immediate).

  
  
The following Calc:Data SCORR command to read / write error terms is
Superseded with [SENS:CORR:CSET:DATA](../Sense/CorrCset.md#data). These SCORR
commands do NOT accommodate greater than 12 error terms.

For 2-Port SOLT and TRL calibrations | Specify this <char> | to get or put this Error Term...  
---|---|---  
SCORR1 | Forward Directivity  
SCORR2 | Forward Source Match  
SCORR3 | Forward Reflection Tracking  
SCORR4 | Forward Isolation  
SCORR5 | Forward Load Match  
SCORR6 | Forward Transmission Tracking  
SCORR7 | Reverse Directivity  
SCORR8 | Reverse Source Match  
SCORR9 | Reverse Reflection Tracking  
SCORR10 | Reverse Isolation  
SCORR11 | Reverse Load Match  
SCORR12 | Reverse Transmission Tracking  
  
EXAMPLE CALC:DATA FDATA,Data(x)  
calculate2:data sdata,data(r,i) See another
[example](../../GPIB_Example_Programs/Getting_and_Putting_Data_using_GPIB.md)
using this command.  
---  
Return Type: [Block
data](../../Learning_about_GPIB/Getting_Data_from_the_Analyzer.htm#block)  
[Default
-](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\))
Not Applicable  
  
* * *

## CALCulate<cnum>:DATA:CUSTom <name>,<data> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
has been replaced by [CALC:DATA](Data.md#data)[:](Data.md#snpReadByPort)
which can now be used with all VNA applications. (Read-Write) Reads or writes
data from a custom-named measurement buffer. [See Critical
Note](Data.htm#Critical)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<name> | Name of the buffer to be read or written  
<data> | Data to be read or written to the custom buffer. Format as one number per data point.  
Examples | CALC:DATA:CUST 'VectorResult0',0,1,2,3,4,5 'Write CALC:DATA:CUST? 'VectorResult0' 'Read  
Query Syntax | CALCulate:DATA:CUSTom? <name>  
Return Type | Depends on [Form:Data](../Format_SCPI.md#fd)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:DATA:CUSTom:CATalog? Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
has been replaced by [CALC:DATA](Data.md#cat)[:CAT](Data.md#snpReadByPort)
which can now be used with all VNA applications. (Read-only) Reads the list of
buffer names (comma separated list of string values) available from the
selected parameter. Specify the measurement using
[CALCulate:PARameter:SELect](Parameter.md#cps). [See Critical
Note](Data.htm#Critical)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
Examples | CALC:DATA:CUST:CAT? calculate:data:custom:catalog?  
Return Type | String  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:DATA:MFData? <measList>

Applicable Models: N522xB, N523xB, N524xB, E5080A, M948xA, P937xA (Read-only)
Gets the formatted data array of multiple traces (traces-n, m, .... to l) of
the selected channel. This command gets multiple trace data with one command,
while [CALC:MEAS:DATA:FDAT](MeasureDATA.md#FDATA) returns only one trace with
one command. Note: If valid data is not calculated because of the invalid
measurement, 1.#QNB is read out.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<measList> | Trace number. "n, m, l, ..." where n, m, l are 1 to the maximum trace number. Note: Use comma for separator of trace number.  
Examples | CALC:DATA:MFD? "1,2"  
Return Type | Data Block   
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:DATA<data>:MSData? <measList>

Applicable Models: N522xB, N523xB, N524xB, E5080A, M948xA, P937xA (Read-only)
Gets the corrected data array of multiple traces (traces-n, m, .... to l) of
the selected channel. This command is allows to get several corrected data
with one command, while [CALC:MEAS:DATA:SDAT](MeasureDATA.md#SDATA) returns
only one corrected data with one command. Note: If valid data is not
calculated because of the invalid measurement, 1.#QNB is read out.  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<measList> | Trace number. "n, m, l, ..." where n, m, l are 1 to the maximum trace number. Note: Use comma for separator of trace number.  
Examples | CALC:DATA:MSD? "1,2"  
Return Type | Data Block  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:DATA:SNP? <n> Superseded

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command has been replaced by [CALC:DATA:SNP:PORTs?](Data.md#snpReadByPort) (Read-only) Reads SnP data from the selected measurement. [Learn more about SnP data](../../../S5_Output/SaveRecall.md#An *.s3p). This command is valid ONLY with standard S-parameter measurements. | Notes

  * This command returns SNP data without header information, and in columns, not in rows as .SnP files. This means that the data returned from this command sends all frequency data, then all Sx1 magnitude or real data, then all Sx1 phase or imaginary data, and so forth.
  * To avoid frequency rounding errors, specify [FORM:DATA](../Format_SCPI.md#fd) <Real,64> or <ASCii, 0>

  
---  
  
[See Critical Note](Data.md#Critical)  
  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<n> | Amount of data to return. If unspecified, <n> is set to 2. The number you specify must be less than or equal to the number of available ports on the VNA. Choose from: **1 (S1P) returns 1-Port data for the active measurement if the active measurement is a reflection parameter such as S11 or S22. The behavior is UNDEFINED if the active measurement is a transmission parameter such as an S21**. 2 (S2P) returns data for the four 2 port parameters associated with the current measurement. Default. Data that is not available is zero-filled. 3 (S3P) returns data for the nine 3 port parameters associated with the current measurement. Data that is not available is zero-filled. 4 (S4P) returns data for the sixteen 4 port parameters associated with the current measurement. Data that is not available is zero-filled. SnP data can be output using several data formatting options. See [MMEM:STORe:TRACe:FORMat:SNP](../Memory.md#snp). See also [MMEM:STOR <file>.<snp>](../Memory.md#save)  
Examples | CALC:PAR:DEF MyMeasurement, S11 CALC:PAR:SEL MyMeasurement CALC:DATA:SNP? 1  
Return Type | Depends on [FORMat:DATA](../Format_SCPI.md#fd).  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:DATA:SNP:PORTs? <"x,y,z".>[, FAST]

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command replaces [CALC:DATA:SNP?](Data.md#snp). This command is more explicit regarding the data to be returned, and works for VNAs with multiport test sets. (Read-only) Reads SNP data from the selected measurement for the specified ports. [Learn more about SNP data](../../../S5_Output/SaveRecall.md#An *.s3p). This command is valid ONLY with standard S-parameter measurements. | Notes

  * This command returns SNP data without header information, and in columns, not in rows as .SnP files. This means that the data returned from this command sends all frequency data, then all Sx1 magnitude or real data, then all Sx1 phase or imaginary data, and so forth.
  * To avoid frequency rounding errors, specify [FORM:DATA](../Format_SCPI.md#fd) <Real,64> or <ASCii, 0>
  * Data that is not available is zero-filled.
  * For sweeps with a large number of data points, always follow this command with *OPC? [Learn more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

  
---  
  
[See Critical Note](Data.md#Critical)  
  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<"x,y,z"> | Comma or space delimited port numbers for which data is requested, enclosed in quotes. SNP data can be output using several data formatting options. See [MMEM:STORe:TRACe:FORMat:SNP](../Memory.md#snp).  
[, FAST] | Reduce the saving time [:SENS:CORR:CACH:MODE](../Sense/Sense_Correction.md#CacMode) should be set at ON.   
  
The correction must cover all the ports of the SNP port list.  The active
measurement must be a corrected S Parameter defined by the port list for the
SNP requests. EG: "S33" is not a proper selected measurement with
CALC:DATA:SNP:PORTS? <1,2>  
Examples | CALC:DATA:SNP:PORTs? "1,2,4,5,7" 'read data for these ports  
Return Type | Depends on [FORMat:DATA](../Format_SCPI.md#fd)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:DATA:SNP:PORTs:SAVE <"x,y,z">,<"filename">[, FAST]

Applicable Models: N522xB, N523xB, N524xB, M937xA, P937xA Note: This command
replaces [MMEM:STOR sNp](../Memory.md#save) for standard channels (only).
This command is more explicit regarding the data to be saved, and works for
VNAs with multiport test sets. (Write-only) Saves SNP data from the selected
measurement for the specified ports. [Learn more about SNP
data](../../../S5_Output/SaveRecall.htm#An *.s3p).

  * The Normal vs Mixed Mode selection is NOT used as it is in the [Choose Ports dialog](../../../S5_Output/SaveRecall.md#ChoosePorts). Instead, data is returned as it is displayed on the trace. If the selected measurement is Mixed Mode (balanced), then balanced data is returned. If the selected measurement is an S-parameter, then S-parameter data is returned.
  * This command is valid ONLY with the Standard measurement class (NOT applications).
  * Data that is not available is zero-filled.
  * For sweeps with a large number of data points, always follow this command with *OPC? [Learn more.](../../Learning_about_GPIB/Understanding_Command_Synchronization.md)

[See Critical Note](Data.md#Critical)  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<"x,y,z"> | String Comma or space delimited port numbers for which data is requested, enclosed in quotes.  
<filename> | String Path, filename, and suffix of location to store the SNP data, enclosed in quotes. The suffix is not checked for accuracy. If saving 2 ports, specify "filename.s2p"; If saving 4 ports, specify "filename.s4p.", and so forth. SNP data can be output using several data formatting options. See [MMEM:STORe:TRACe:FORMat:SNP](../Memory.md#snp).  
[, FAST] | Reduce the saving time [:SENS:CORR:CACH:MODE](../Sense/Sense_Correction.md#CacMode) should be set at ON.   
  
The correction must cover all the ports of the SNP port list.  The active
measurement must be a corrected S Parameter defined by the port list for the
SNP requests. EG: "S33" is not a proper selected measurement with
CALC:DATA:SNP:PORTS? <1,2>  
Examples | CALC:DATA:SNP:PORTs:Save '1,2,4','D:\MyData.s3p';*OPC?  
Return Type | Depends on [FORMat:DATA](../Format_SCPI.md#fd)  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
* * *

## CALCulate<cnum>:MEASure<mnum>:RDATa? <char>

(Read-only) Returns receiver data for the selected measurement. To query
measurement data, see [CALC:DATA?](Data.md) Critical Note: CALCulate commands
act on the selected measurement. You can select one measurement for each
channel using [Calc:Par:MNUM](Parameter.md#MnumSel) or
[Calc:Par:Select](Parameter.md#cps). [Learn
more](../../Learning_about_GPIB/Referring_to_Traces_Measurements_Channels_Windows_Using_SCPI.htm).  
---  
Parameters |   
<cnum> | Channel number of the measurement. There must be a selected measurement on that channel. If unspecified, <cnum> is set to 1.  
<mnum> | Measurement number for each measurement. There must be a selected measurement on the trace. If unspecified, <mnum> is set to 1.  
<char> | Choose from any physical receiver in the VNA. For example: "A" Also, REF - returns data for either R1 or R2 data depending on the source port of the selected measurement. See the [block diagram](../../../Specs/ManualChoice.md#Block_diag) showing the receivers in VNA. Note: Logical receiver notation is NOT allowed with this command. [Learn more.](../../../S1_Settings/Measurement_Parameters.md#RecNotation)  
Example | INITiate:CONTinuous OFF  
INITiate:IMMediate;*wai  
CALC:MEAS:RDATA? A CALCulate:RDATA? REF  
Return Type | Depends on [FORM:DATA](../Format_SCPI.md#fd) command - Two numbers per data point  
[Default](JavaScript:hhctrl.TextPopup\(DefSCPI,'Arial,8',10,10,00000000,0xc0ffff\)) | Not Applicable  
  
Notes:

Generally when you query the analyzer for data, you expect that the number of
data values returned will be consistent with the number of points in the
sweep.

However, if you query receiver data while the instrument is sweeping, the
returned values may contain zeros. For example, if your request for receiver
data is handled on the 45th point of a 201 point sweep, the first 45 values
will be valid data, and the remainder will contain complex zero.

This can be avoided by synchronizing this request with the end of a sweep or
putting the channel in hold mode.

[Learn about Unratioed
Measurements](../../../S1_Settings/Measurement_Parameters.htm#Unratioed_Power)

* * *


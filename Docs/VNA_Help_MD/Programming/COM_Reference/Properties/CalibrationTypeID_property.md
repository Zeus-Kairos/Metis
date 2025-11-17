##### Write/Read

|

##### [Learn about cal types](../../../S3_Cals/Cal_Sets.md#ApplyingCalSet)  
  
---|---  
  
## CalibrationTypeID Property

* * *

#### Description

|  Note: This command replaces [Calibration Type
Property](Calibration_Type_Property.htm). Sets or returns the current cal type
for the measurement using a Cal Type Name. This command is used to set the Cal
Type after recalling a Cal Set. [Learn
more](../../Learning_about_GPIB/Calibrating_the_Analyzer_Using_SCPI.htm#Applying)
You can also use the CLSID or GUID associated with the Cal Type.  
---|---  
  
####  VB Syntax

|  meas.CalibrationTypeID = id  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
id |  (String) Cal type. Case sensitive. Use one of the following:

### For Full Calibrations:

This command does not distinguish between TRL and SOLT. The same number of
error terms is applied for both Cal Types. "Full n Port(x,y,z...)" where n =
the number of ports to calibrate x,y,z = the port numbers to calibrate For
example: "Full 7 Port(2,3,4,5,6,7,8)"

### For Response Calibrations:

"Response(param)" OR "ResponseAndIsolation(param)" Where param =

  * S-parameter. For example"
  *     * "Response(S21)"
    * "ResponseAndIsolation(A/R)"
  * Single or ratioed receivers using either [logical receiver notation](../../../S1_Settings/Measurement_Parameters.md#RecNotation) or physical receiver notation. For example:
  *     * "Response(A)"
    * "ResponseAndIsolation(a3/b4)"

### For FCA Calibrations:

  * "SMC_2P" (Response + Input + Output) All four sweeps required. Most accurate.
  * "SMCRsp+IN" No Output match. All four sweeps required.
  * "SMCRsp+OUT" No Output match. All four sweeps required.
  * "SMCRsp" No Input or Output match. Saves two sweeps.

For VMC, multiple Cal types are not available.

### For Gain Compression Cal

where r = receive port; s = source port

  * "GCA 2P (r,s) - full 2-port cal
  * GCA Enh Resp (r,s) - Enhanced Response Cal

  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim pna Dim m Set pna = CreateObject("AgilentPNA835x.Application") Set m =
pna.ActiveMeasurement m.CalibrationTypeID = "Scalar Mixer Cal"
m.ErrorCorrection = True MsgBox m.CalibrationName  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_CalibrationTypeID( BSTR* CalibrationTypeID ); HRESULT
put_CalibrationTypeID( BSTR CalibrationTypeID );  
  
#### Interface

|  IMeasurement2  
  
* * *


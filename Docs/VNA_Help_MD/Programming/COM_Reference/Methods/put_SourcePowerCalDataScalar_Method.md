##### Write-only.

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## putSourcePowerCalDataScalar Method - Superseded

* * *

#### Description

|  Note: This method is replaced by [PutSourcePowerCalDataScalarEx
Method](Put_SourcePowerCalDataScalarEx_Method.htm) Inputs source power
calibration data (as scalar values) to this channel for a specific source
port.  
---|---  
  
####  VB Syntax

|  chandata.putSourcePowerCalDataScalar sourcePort, numValues, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chandata |  (interface)   An ISourcePowerCalData interface pointing to a Channel (object)  
sourcePort |  (long integer)  The source port for which calibration data is being input.  
numValues |  (long integer)  Number of data values being input. Note: If this does not equal the current number of points on the channel, the calibration will not be valid.  
data |  (single)  Array of source power cal data being input.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim chanData As ISourcePowerCalData  
Set chanData = app.ActiveChannel  
chanData.putSourcePowerCalDataScalar 1, 201, scalarCalValues(0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT putSourcePowerCalDataScalar(long sourcePort, long numValues, float
*pVals);  
  
#### Interface

|  ISourcePowerCalData


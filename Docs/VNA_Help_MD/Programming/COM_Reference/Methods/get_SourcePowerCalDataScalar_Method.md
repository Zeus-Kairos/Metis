##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## getSourcePowerCalDataScalar Method - Superseded

* * *

#### Description

|  Retrieves (as scalar values) requested source power calibration data, if it
exists, from this channel. Note: This method is replaced by
[GetSourcePowerCalDataScalarEx
Method](Get_SourcePowerCalDataScalarEx_Method.htm)  
---|---  
  
####  VB Syntax

|  chandata.getSourcePowerCalDataScalar sourcePort, numValues, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chandata |  (interface)   An ISourcePowerCalData interface pointing to a Channel (object)  
sourcePort |  (long integer)  The source port for which calibration data is being requested.  
numValues |  (long integer)  Number of data values. [out]  specifies number of data values returned. [in]  specifies number of values being requested (this must not be larger than the capacity of the data array).  
data |  (single)  Array to store the data.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim numValues As Long  
Dim scalarCalValues() As Single  
Dim chanData As ISourcePowerCalData  
Const port1 As Long = 1  
numValues = app.ActiveChannel.NumberOfPoints  
ReDim scalarCalValues(numValues)  
Set chanData = app.ActiveChannel  
  
chanData.getSourcePowerCalDataScalar port1, numValues, scalarCalValues(0)  
  
'Print the data  
For i = 0 to numValues - 1  
Print scalarCalValues(i)  
Next I  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT getSourcePowerCalDataScalar(long sourcePort, long *pNumValues,
float *pVals);  
  
#### Interface

|  ISourcePowerCalData


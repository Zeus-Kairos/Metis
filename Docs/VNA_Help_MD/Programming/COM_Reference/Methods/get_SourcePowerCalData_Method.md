##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## **getSourcePowerCalData Method -** Superseded

* * *

#### Description

|  Retrieves (as variant data type) requested source power calibration data,
if it exists, from this channel. Note: This method is replaced by
[GetSourcePowerCalDataEx Method](Get_SourcePowerCalDataEx_Method.md). Note:
This method returns a variant which is less efficient than methods available
on the ISourcePowerCalData interface  
---|---  
  
####  VB Syntax

|  data = chan.getSourcePowerCalData sourcePort  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (variant)  Array to store the data.  
chan |  (object)  A Channel object  
sourcePort |  (long integer)  The source port for which calibration data is being requested.  
  
#### Return Type

|  Variant array  automatically dimensioned to the size of the data.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varData As Variant  
Const port1 As Long = 1  
varData = chan.getSourcePowerCalData port1  
'Print the data  
For i = 0 to chan.NumberOfPoints - 1  
Print varData(i)  
Next i  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT getSourcePowerCalData(long sourcePort, VARIANT *pData);  
  
#### Interface

|  IChannel


##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## putSourcePowerCalDataScalarEx Method

* * *

#### Description

|  Note: This method replaces [putSourcePowerCalDataScalar
Method](put_SourcePowerCalDataScalar_Method.htm) Inputs source power
calibration data (as scalar values) to this channel for a specific source
port. The effect from this command on the channel is immediate. Do NOT send
ApplyPowerCorrectionValuesEX after this command as it may invalidate the
uploaded data. If the channel is sweeping the source backwards, then the first
data point is the highest frequency value; the last data point is the lowest.
Use the [Get X-Axis Values2](Get_X-Axis_Values_2.md) command to return the
X-axis values in the displayed order.  
---|---  
  
####  VB Syntax

|  chanData.putSourcePowerCalDataScalarEx buffer, srcPort, numValues, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chanData |  (interface)  An [ISourcePowerCalData2](../Objects/Channel_Object.md#ISourcePowerCalData) interface on the Channel (object)  
buffer |  (enum NASourcePowerCalBuffer) \- The source power cal data buffer to write to. 0 - naCorrectionValues This is the only buffer currently available.  
srcPort |  (long integer)  The source port for which calibration data is being input. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
numValues |  (long integer)  Number of data values being input. Note: If this does not equal the current number of points on the channel, the calibration will not be valid.  
data |  (single)  Array of source power cal data being input.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim chanData As ISourcePowerCalData2  
Set chanData = app.ActiveChannel  
chanData.putSourcePowerCalDataScalarEx naCorrectionValues, 1, 201,
scalarCalValues(0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT putSourcePowerCalDataScalarEx(tagNASourcePowerCalBuffer bufSelect,
long sourcePort, long numValues, float *pData);  
  
#### Interface

|  ISourcePowerCalData2  
  
* * *

  


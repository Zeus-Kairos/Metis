##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## getSourcePowerCalDataScalarEx Method

* * *

#### Description

|  Note: This method replaces [getSourcePowerCalDataScalar
Method](get_SourcePowerCalDataScalar_Method.htm) Retrieves (as scalar values)
source power calibration data, if it exists, from this channel. If the channel
is sweeping the source backwards, then the first data point is the highest
frequency value; the last data point is the lowest. Use the [Get X-Axis
Values2](Get_X-Axis_Values_2.htm) command to return the X-axis values in the
displayed order. Note: This method exists on a non-default interface. If you
cannot access this method, use the
[getSourcePowerCalDataEx](Get_SourcePowerCalDataEx_Method.md) Method on
IChannel4.  
---|---  
  
####  VB Syntax

|  chanData.getSourcePowerCalDataScalarEx buffer, srcPort, numValues, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chanData |  (interface)  An [ISourcePowerCalData2](../Objects/Channel_Object.md#ISourcePowerCalData) interface on the Channel object.  
buffer |  (enum NASourcePowerCalBuffer) \- The requested source power cal data buffer. 0 - naCorrectionValues Last iteration of Cal data. 1 - naPriorIterationCorrectionValues Prior iteration of Cal data. This argument can be used to determine the final power reading at each point of the power cal, for a cal that did not pass tolerance limits.  The following formula can be used to determine the power reading (in dB): Power reading = Target power at the source port + specified power cal offset value + prior iteration corr value  actual power corr value. The "actual" value in this equation is returned with naCorrectionValues.  
srcPort |  (long integer)  The source port for which calibration data is being requested. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
numValues |  (long integer)  Number of data values. [out]  specifies number of data values returned. [in]  specifies number of values being requested (this must not be larger than the capacity of the data array).  
data |  (single)  Array to store the data.  
  
#### Return Type

|  Single  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim numValues As Long  
Dim scalarCalValues() As Single  
Dim chanData As ISourcePowerCalData2  
Const port1 As Long = 1  
numValues = app.ActiveChannel.NumberOfPoints  
ReDim scalarCalValues(numValues)  
Set chanData = app.ActiveChannel  
  
chanData.getSourcePowerCalDataScalarEx naCorrectionValues, port1, numValues,
scalarCalValues(0)  
  
'Print the data  
For i = 0 to numValues - 1  
Print scalarCalValues(i)  
Next I  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT getSourcePowerCalDataScalarEx(tagNASourcePowerCalBuffer bufSelect,
long sourcePort, long *pNumValues, float *pData);  
  
#### Interface

|  ISourcePowerCalData2  
  
* * *

  


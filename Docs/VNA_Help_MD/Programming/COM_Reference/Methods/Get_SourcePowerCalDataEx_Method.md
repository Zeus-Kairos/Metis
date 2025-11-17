##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## **getSourcePowerCalDataEx Method**

* * *

#### Description

|  Note: This method replaces [getSourcePowerCalData
Method](get_SourcePowerCalData_Method.htm) Retrieves (as variant data type)
source power calibration data, if it exists, from the channel. If the channel
is sweeping the source backwards, then the first data point is the highest
frequency value; the last data point is the lowest. Use the [Get X-Axis
Values](Get_X-axis_Values_Method.htm) command to return the X-axis values in
the displayed order. Note: This method returns a variant which is less
efficient than methods available on the ISourcePowerCalData interface  
---|---  
  
####  VB Syntax

|  data = chan.getSourcePowerCalDataEx (buffer, srcPort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (variant)  Array to store the data.  
chan |  (object)  A [Channel](../Objects/Channel_Object.md) object  
buffer |  (enum NASourcePowerCalBuffer) \- The requested source power cal data buffer. 0 - naCorrectionValues Last iteration of Cal data 1 - naPriorIterationCorrectionValues Prior iteration of Cal data. This argument can be used to determine the final power reading at each point of the power cal, for a cal that did not pass tolerance limits.  The following formula can be used to determine the power reading (in dB): Power reading = Target power at the source port + specified power cal offset value + prior iteration corr value  actual power corr value. The "actual" value in this equation is returned with naCorrectionValues.  
srcPort |  (long integer)  The source port for which calibration data is being requested. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
  
#### Return Type

|  Variant array  automatically dimensioned to the size of the data.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim varData As Variant  
Const port1 As Long = 1  
varData = chan.getSourcePowerCalDataEx (naCorrectionValues, port1)  
'Print the data  
For i = 0 to chan.NumberOfPoints - 1  
Print varData(i)  
Next i  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT getSourcePowerCalDataEx(tagNASourcePowerCalBuffer bufSelect, long
sourcePort, VARIANT *pData);  
  
#### Interface

|  IChannel4  
  
* * *

  


##### Write-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## putSourcePowerCalDataEx Method

* * *

#### Description

|  Note: This method replaces [putSourcePowerCalData
Method](put_SourcePowerCalData_Method.htm) Inputs source power calibration
data (as variant data type) to this channel for a specific source port. The
effect from this command on the channel is immediate. Do NOT send
ApplyPowerCorrectionValuesEX after this command as it may invalidate the
uploaded data. If the channel is sweeping the source backwards, then the first
data point is the highest frequency value; the last data point is the lowest.
Use the [Get X-Axis Values](Get_X-axis_Values_Method.md) command to return
the X-axis values in the displayed order. The calibration is not valid if the
current number of points on the channel is not equal to the number of values
that were input. Note: This method sends variant data which is less efficient
than methods available on the ISourcePowerCalData interface.  
---|---  
  
####  VB Syntax

|  chan.putSourcePowerCalDataEx buffer, srcPort, data  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
chan |  (object)  A [Channel object](../Objects/Channel_Object.md)  
buffer |  (enum NASourcePowerCalBuffer) \- The source power cal data buffer to write to. 0 - naCorrectionValues This is the only data buffer currently available.  
srcPort |  (long integer)  The source port for which calibration data is being requested. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
data |  (variant)  Array of source power cal data being input.  
  
#### Return Type

|  None  
  
#### Default

|  Not Applicable  
  
#### Examples

|  chan.putSourcePowerCalDataEx naCorrectionValues, 1, varData  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT putSourcePowerCalDataEx(tagNASourcePowerCalBuffer bufSelect, long
sourcePort, VARIANT varData);  
  
#### Interface

|  IChannel4  
  
* * *


##### Read-only

|

##### [About Source Power Cal](../../../S3_Cals/PwrCalibration.md)  
  
---|---  
  
## CalPower Property Superseded

* * *

#### Description

|  This command is replaced with
chan.[TestPortPower](Test_Port_Power_Property.md). Returns the RF power level
for the channel.  
---|---  
  
####  VB Syntax

|  value = powerCalibrator.CalPower (chan, sourcePort)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (double) \- Variable to store the returned Cal power value in dBm.  
powerCalibrator |  (object) \- A SourcePowerCalibrator object  
chan |  (long integer) \- Channel number of the VNA.  
sourcePort |  (long integer) \- Source port number. Use [GetPortNumber](../Methods/GetPortNumber_Method.md) to return the port number of a source that only has a string name, such as an [External Source](../../../System/Configure_an_External_Device.md).  
  
#### Return Type

|  None  
  
#### Default

|  Not applicable  
  
#### Examples

|  Set powerCalibrator = pna.SourcePowerCalibrator power =
powerCalibrator.CalPower(1,2) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalPower(long channel, long sourcePort, double *pVal);  
  
#### Interface

|  ISourcePowerCalibrator  
  
* * *


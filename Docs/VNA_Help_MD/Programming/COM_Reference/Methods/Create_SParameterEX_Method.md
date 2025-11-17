##### Write-only

|

##### [About Measurement
Parameters](../../../S3_Cals/Measurement_Calibration.htm)  
  
---|---  
  
## CreateSParameterEx Method - Superseded

* * *

#### Description

| Note: This method is replaced by [Create
SParameter](CreateCustomMeasurementEx_Method.htm) method. The Load port
selection is no longer necessary. Creates a new S-Parameter measurement in an
existing or new window and specifies the load port for 3-port devices.  
---|---  
  
####  VB Syntax

| app.CreateSParameterEx chan,recvr,source[,loadPort][,window]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | [Application](../Objects/Application_Object.md) (object)  
chan | (long integer) - Channel number of the new measurement.  
recvr | (long integer) - Port number of the test port receiver.  
source  | (long integer) \- Port number of the source. Note: If the port is defined by a string name, such as an external source, a balanced port, or one of the Source 2 outputs on the 2-port 2-source VNA-x model, then you must use [chan.getPortNumber](GetPortNumber_Method.md) to translate the string into a port number. To learn more see [Remotely Specifying a Source Port](../../Remotely_Specifying_a_Source_Port.md).  
loadPort | (long integer) \- Port number of the load. Required for reflection measurements of 3-port devices on multiport VNA models.  
window | (long integer) \- Optional argument. Choose between 1and the [maximum number of windows allowed on the VNA.](../Properties/MaximumNumberOfWindows_Property.md). See also [Traces, Channels, and Windows on the VNA](../../../S0_Start/Traces_Channels_and_Windows.md#window). If unspecified, the S-Parameter will be created in the Active Window.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| app.CreateSParameterEx 1,2,1,1 'Creates a new S21 measurement in channel 1
and New window(1)  
app.CreateSParameterEx 2,1,1,3,1 'Creates a new S11 measurement on channel 2
with port 3 as the load. Create in the active window  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT CreateSParameterEx(long ChannelNum, long RcvPort, long SrcPort, long
LoadPort, long windowNumber)  
  
#### Interface

| IApplication  
  
* * *


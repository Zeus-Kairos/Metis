##### Write-only

|

##### [About Measurement
Parameters](../../../S3_Cals/Measurement_Calibration.htm)  
  
---|---  
  
## CreateS-Parameter Method

* * *

#### Description

| This method creates a new S-Parameter measurement in an existing or new
window.  
---|---  
  
####  VB Syntax

| app.CreateSParameter chan,recvr,source,[window]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app | [Application](../Objects/Application_Object.md) (object)  
chan | (long integer) - Channel number of the new measurement  
recvr | (long integer) - Number of receivers  
source  | (long integer) - Number of sources  
window | (long integer) \- Optional argument. Window number of the new measurement. Choose 1 to 4. If unspecified, the S-Parameter will be created in the Active Window.  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| app.CreateSParameter 1,2,1,1 'Creates a new S21 measurement in channel 1 and
New window(1)  
app.CreateSParameter 1,2,1 'Creates a new S21 measurement in channel 1 and in
the active window  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

| HRESULT CreateSParameter(long ChannelNum, long RcvPort, long SrcPort, long
windowNumber)  
  
#### Interface

| IApplication  
  
* * *


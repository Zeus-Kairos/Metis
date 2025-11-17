##### Write-only

## CreateCustomMeasurement Method Superseded

* * *

#### Description

|  This command is replaced with [CreateCustomMeasurementEx
Method](CreateCustomMeasurementEx_Method.htm). Creates a new custom
measurement.  
---|---  
  
####  VB Syntax

|  app.CreateCustomMeasurement chanNum,guid[,window]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  (object) - An [Application](../Objects/Application_Object.md) object  
chanNum |  (long) -Channel number used by the new measurement; can exist or be a new channel.  
guid |  (string) - the GUID (Globally Unique IDentifier) of the new custom measurement object. The new custom measurement must be installed and registered on the PNA. Should be in registry format. See example below.  
window |  (long) Optional argument. Number of the window the new custom measurement will be placed in. Choose 1 to 16. If unspecified, the measurement is placed in the active window.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.CreateCustomMeasurement 1, "{12345678-56D3-11D5-AD50-00108334AE98}"
'Not an actual custom measurement - for example purpose only  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT CreateCustomMeasurement (long ChannelNum, BSTR guid, long
windowNumber)  
  
#### Interface

|  IApplication


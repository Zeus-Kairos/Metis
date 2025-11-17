##### Read-only

|

##### [About Limit
Testing](../../../S4_Collect/Use_Limits_to_Test_Devices.htm)  
  
---|---  
  
## LoadPort Property

* * *

#### Description

|  Returns the load port number associated with an S-parameter reflection
measurement. If the measurement is not a reflection S-parameter, the number
returned by this property will have no meaning.  
---|---  
  
####  VB Syntax

|  loadPort = meas.LoadPort  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
loadPort |  (long integer) - The reflection measurements load port number.  
meas |  A Measurement (object)  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Set meas = pna.ActiveMeasurement  
loadPort = meas.LoadPort  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LoadPort(long *pPortNumber);  
  
#### Interface

|  IMeasurement


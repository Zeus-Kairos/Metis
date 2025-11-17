##### Read only

|

##### [About Receiver Temp](../../../Support/Receiver_Temperature.md)  
  
---|---  
  
## ReceiverTemperature Property

* * *

#### Description

|  Returns the current temperature on the VNA receiver board.  
---|---  
  
####  VB Syntax

|  value = cap.ReceiverTemperature (unit)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned temperature value.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
unit |  (Enum as NATempScale) - Units in which temperature is returned. Choose from:

  * 0 - naTempScale_Fahrenheit
  * 1 - naTempScale_Celsius

  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.ReceiverTemperature naTempScale_Celsius'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_ReceiverTemperature(NATempScale val, long temperature);  
  
#### Interface

|  ICapabilities9  
  
* * *

* * *


##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumSourceALCPower Property

* * *

#### Description

|  Returns a value indicating the maximum amount of source ALC power with 0 dB
source attenuation. To calculate the maximum amount of source ALC power with a
different level of attenuation, subtract the amount source attenuation from
this value.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumSourceALCPower (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned value for the maximum amount of source ALC power.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - source number to query for maximum ALC power  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumSourceALCPower'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumSourceALCPower(long sourceNum, double * power );  
  
#### Interface

|  ICapabilities  
  
* * *


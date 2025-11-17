##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MinimumSourceALCPower Property

* * *

#### Description

|  Returns a value indicating the minimum amount of source ALC power with 0 dB
source attenuation. To calculate the minimum amount of source ALC power with a
different level of attenuation, subtract the amount source attenuation from
this value.  
---|---  
  
####  VB Syntax

|  value = cap.MinimumSourceALCPower (n)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Double) \- Variable to store the returned minimum value of source ALC power.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
n |  (Long) - source number to query for the minimum value of source ALC power.  
  
#### Return Type

|  Double  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MinimumSourceALCPower'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MinimumSourceALCPower(long sourceNum, double * power );  
  
#### Interface

|  ICapabilities


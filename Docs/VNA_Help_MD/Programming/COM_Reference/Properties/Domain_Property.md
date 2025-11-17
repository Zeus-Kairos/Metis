##### Read-only

|  
---|---  
  
## Domain Property

* * *

#### Description

|  Returns the domain (frequency,time, power, phase) of the measurement. To
understand how this property is useful, see [IMeasurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface).  
---|---  
  
####  VB Syntax

|  value = meas.Domain  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Enum as NADomainType) - variable to store the returned value 0 - naDomainFrequency 1 - naDomainTime 2 - naDomainPower 4 - naDomainPhase  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
  
#### Return Type

|  Enum as NADomainType  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Print meas.Domain 'prints the value of the domain enum  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_Domain(tagNADomainType * Val);  
  
#### Interface

|  IMeasurement2  
  
* * *


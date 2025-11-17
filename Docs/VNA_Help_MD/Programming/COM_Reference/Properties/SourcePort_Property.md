##### Read-only

# SourcePort Property

* * *

#### Description

|  Returns the source port of measurement. To understand how this property is
useful, see [IMeasurement2
Interface](../Objects/Measurement_Object.htm#IMeasurement2Interface).  
---|---  
  
####  VB Syntax

|  value = meas.SourcePort  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (Long) \- Variable to store the returned value  
  
#### Return Type

|  Long Integer  
  
#### Default

|  Not Applicable  
  
#### Examples

|  sp = meas.SourcePort  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SourcePort( [out, retval] Long* srcPort);  
  
#### Interface

|  IMeasurement2


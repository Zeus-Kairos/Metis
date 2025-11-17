##### Write/Read

|

##### [About DC Sources](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
# LimitMax Property

* * *

#### Description

|  Sets and returns the Max DC limit value for a DC source.  
---|---  
  
####  VB Syntax

|  dc.LimitMax(deviceName) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
dc |  A [DCStimulus](../Objects/DCStimulus_Object.md) (object)  
deviceName |  (String) Name of the "DC source" Use [Source Property](Source_Property.md) to read a list of configured DC source names.  
value |  (Double) Max DC limit value. Choose a value within the range of the DC source.  
  
#### Return Type

|  Double  
  
#### Default

|  10  
  
#### Examples

|  dc.LimitMax("myDCSource") = 10 'Write value = dc.LimitMax("myDCSource")
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LimitMax(BSTR deviceName, double* value); HRESULT
put_LimitMax(BSTR deviceName, double value);  
  
#### Interface

|  IDCStimulus2  
  
* * *


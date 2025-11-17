##### Write/Read

|

##### [About DC Sources](../../../S1_Settings/DC_Control.md)  
  
---|---  
  
# LimitMin Property

* * *

#### Description

|  Sets and returns the Min DC limit value for a DC source.  
---|---  
  
####  VB Syntax

|  dc.LimitMin(deviceName) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
dc |  A [DCStimulus](../Objects/DCStimulus_Object.md) (object)  
deviceName |  (String) Name of the "DC source" Use [Source Property](Source_Property.md) to read a list of configured DC source names.  
value |  (Double) Min DC limit value. Choose a value within the range of the DC source.  
  
#### Return Type

|  Double  
  
#### Default

|  -10  
  
#### Examples

|  dc.LimitMin("myDCSource") = -10 'Write value = dc.LimitMin("myDCSource")
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_LimitMin(BSTR deviceName, double* value); HRESULT
put_LimitMin(BSTR deviceName, double value);  
  
#### Interface

|  IDCStimulus2  
  
* * *


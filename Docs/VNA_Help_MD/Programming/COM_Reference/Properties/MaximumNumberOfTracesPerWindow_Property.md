##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumNumberOfTracesPerWindow Property

* * *

#### Description

|  Returns the maximum possible number of traces that can reside in any
window.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumNumberOfTracesPerWindow  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) \- Variable to store the returned maximum value for number of traces.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumNumberOfTracesPerWindow 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumNumberOfTracesPerWindow(long * maximumNumberOfTraces );  
  
#### Interface

|  ICapabilities2


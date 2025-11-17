##### Read only

|

##### [About VNA Options](../../../Support/Configurations.md)  
  
---|---  
  
## MaximumNumberOfWindows Property

* * *

#### Description

|  Returns the maximum possible number of windows that can be present on the
VNA screen.  
---|---  
  
####  VB Syntax

|  value = cap.MaximumNumberOfWindows  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Long) \- Variable to store the returned maximum value for number of windows.  
cap |  A [Capabilities](../Objects/Capabilities_Object.md) (object)  
  
#### Return Type

|  Long  
  
#### Default

|  Not Applicable  
  
#### Examples

|  value = cap.MaximumNumberOfWindows 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_MaximumNumberOfWindows(long * maximumNumberOfWindows );  
  
#### Interface

|  ICapabilities2


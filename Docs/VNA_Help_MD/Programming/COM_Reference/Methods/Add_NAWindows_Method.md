##### Write-only

|

##### [About
Windows](../../../S0_Start/Traces_Channels_and_Windows.htm#window)  
  
---|---  
  
## Add (NAWindows) Method

* * *

#### Description

|  Add a window to the display. Does not add a measurement. The window number
must not already exist.  
---|---  
  
#### VB Syntax

|  wins.Add [item]  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
wins |  A [NAWindow](../Objects/NAWindows_Collection.md) collection (object)  
item |  (variant) \- Window number. Choose between 1and the [maximum number of windows allowed on the VNA.](../Properties/MaximumNumberOfWindows_Property.md) See also [Traces, Channels, and Windows on the VNA](../../../S0_Start/Traces_Channels_and_Windows.md#window)  
  
#### Return Type

|  Object  
  
#### Default

|  Not Applicable  
  
#### Examples

|  wins.Add 3 'Creates a window number 3  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Add(long windowNumber )  
  
#### Interface

|  INAWindows  
  
* * *


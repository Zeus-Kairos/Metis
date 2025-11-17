##### Write-only

|

##### [About Display
Formatting](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm)  
  
---|---  
  
## ShowTable Method

* * *

#### Description

|  Shows or Hides the specified table for the window's active measurement in
the lower part of the window.  
---|---  
  
####  VB Syntax

|  win.ShowTable value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
win |  A NAWindow (object)  
value |  (enum naTable) - The table to show or hide. Choose from: 0 - naTable_None  
1 - naTable_Marker  
2 - naTable_Segment  
3 - naTable_Limit  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  win.ShowTable naTable_limit  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ShowTable (tagNATableType table)  
  
#### Interface

|  INAWindow


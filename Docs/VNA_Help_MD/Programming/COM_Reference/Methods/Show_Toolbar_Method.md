##### Write-only

|

##### [About Display
Formatting](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm)  
  
---|---  
  
## ShowToolbar Method

* * *

#### Description

|  Shows and Hides the specified Toolbar.  
---|---  
  
####  VB Syntax

|  app.ShowToolbar toolbar,state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
toolbar |  (enum NAToolbarType) - The toolbar to show or hide. Choose from: 0 - naToolbar_None 1 - naToolbar_ActiveEntry 2 - naToolbar_Markers 3 - naToolbar_Measurement - OBSOLETE 4 - naToolbar_Stimulus - OBSOLETE 5 - naToolbar_SweepControl - OBSOLETE 6 - naToolbar_Transform 7 - naToolbar_PortExtensions 8 - naToolbar_Keys  
state |  (boolean) - True (1) \- Show the specified toolbar False (0) \- Hide the specified toolbar  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  1 - naToolbar_ActiveEntry showing; all others hiding.  
  
#### Examples

|  app.ShowToolbar 1,1 'shows the active entry toolbar  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ShowToolbar(tagNAToolbarType toolbar, VARIANT_BOOL bState)  
  
#### Interface

|  IApplication


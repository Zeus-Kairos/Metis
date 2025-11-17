##### Write-only

|

##### [About Display
Formatting](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm)  
  
---|---  
  
## ShowStatusBar Method

* * *

#### Description

|  Shows and Hides the Status Bar. The Status Bar is located across the bottom
of the display. The following information is shown for the active measurement:

  * Channel number
  * Parameter
  * Correction On or Off
  * Remote or Local operation

  
---|---  
  
####  VB Syntax

|  app.ShowStatusBar state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean) -  
True (1) \- Show the Status Bar  
False (0) \- Hide the Status Bar  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.ShowStatusBar True  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT ShowStatusBar (VARIANT_BOOL bState)  
  
#### Interface

|  IApplication


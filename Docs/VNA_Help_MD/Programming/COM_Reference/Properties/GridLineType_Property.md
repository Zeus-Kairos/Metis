##### Write / Read

|

##### [About Display
Items](../../../S1_Settings/Customize_Your_Analyzer_Screen.htm#GridLines)  
  
---|---  
  
## GridLineType Property

* * *

#### Description

|  Set and return whether the grid lines are displayed in solid or dotted
lines for all open windows. Grid lines are returned to solid when the VNA is
Preset.  
---|---  
  
#### VB Syntax

|  app.GridLineType = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  A [Application Object](../Objects/Application_Object.md) (object)  
value |  (Enum as naLineType) \- Choose from: 0 - naLineTypeSolid 1 - naLineTypeDotted  
  
#### Return Type

|  Enum  
  
#### Default

|  naLineTypeSolid  
  
#### Examples

|  app.GridLineType = naLineTypeSolid 'Write  
grid = app.GridLineType 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_GridLineType(tag naLineType* pVal); HRESULT
put_GridLineType(tag naLineType newVal);  
  
#### Interface

|  IApplication  
  
* * *

  


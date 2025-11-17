##### Write/Read

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## AllowEventSeverity Method

* * *

#### Description

|  Sets event filtering to monitor levels of severity.  
---|---  
  
####  VB Syntax

|  app.AllowEventSeverity severity,state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [ Application](../Objects/Application_Object.md) (object)  
severity |  (enum naEventSeverity) Choose from:naEventSeverityERROR  
naEventSeverityINFORMATIONAL  
naEventSeveritySUCCESS  
naEventSeverityWARNING  
state |  (boolean)  
True \- monitor  
False \- do not monitor  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.AllowEventSeverity  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT AllowEventSeverity( tagNAEventSeverity severity, VARIANT_BOOL
bAllow)  
  
#### Interface

|  IApplication


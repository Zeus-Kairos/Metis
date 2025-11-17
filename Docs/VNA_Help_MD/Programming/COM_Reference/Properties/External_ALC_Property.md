##### Write/Read

## ExternalALC Property

* * *

#### Description

|  Sets or returns the source of the analyzer leveling control.  
---|---  
  
####  VB Syntax

|  app.ExternalALC = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (boolean) \- Choose from:  
True \- Leveling control supplied through the rear panel. False \- Leveling
control supplied inside the analyzer  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  app.ExternalALC = True 'Write  
extALC = app.ExternalALC 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_ExternalALC(VARIANT_BOOL *pVal)  
HRESULT put_ExternalALC(VARIANT_BOOL newVal)  
  
####  Interface

|  IApplication


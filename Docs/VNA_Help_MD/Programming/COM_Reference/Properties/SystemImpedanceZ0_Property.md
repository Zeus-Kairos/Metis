##### Write/Read

|

##### [About System Impedance](../../../System/System_Impedance.md)  
  
---|---  
  
## SystemImpedanceZ0 Property

* * *

#### Description

|  Sets and returns the impedance for the analyzer.  
---|---  
  
####  VB Syntax

|  app.SystemImpedanceZ0 = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (double) Analyzer Impedance. Choose any number between 0 and 1000 ohms.  
  
#### Return Type

|  Double  
  
#### Default

|  50  
  
#### Examples

|  app.SystemImpedanceZ0 = 75 'Write  
z0 = app.SystemImpedanceZ0 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT get_SystemImpedanceZ0(double dSystemZ0)  
HRESULT put_SystemImpedanceZ0(double *pdSystemZ0)  
  
#### Interface

|  IApplication


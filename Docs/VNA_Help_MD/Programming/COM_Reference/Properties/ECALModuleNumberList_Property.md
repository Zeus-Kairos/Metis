##### Read-only

## ECALModuleNumberList Property

* * *

#### Description

|  Returns a list of index numbers to be used for referring to the ECal
modules that are currently attached to the VNA.  
---|---  
  
####  VB Syntax

|  clist = cal.ECALModuleNumberList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
clist |  Variable to store the returned list of index numbers.  
cal |  [Calibrator](../Objects/Calibrator_Object.md) (object)  
  
#### Return Type

|  Variant  
  
#### Default

|  Not Applicable  
  
#### Examples

|  clist = cal.ECALModuleNumberList  
'If 2 modules are attached to the VNA  
'then the returned list will be:  
1,2  
  
#### C++ Syntax

|  HRESULT get_ECALModuleNumberList( VARIANT *modules);  
  
#### Interface

|  ICalibrator6


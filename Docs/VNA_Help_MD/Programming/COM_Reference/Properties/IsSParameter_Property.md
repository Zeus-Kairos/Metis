##### Read-only

# IsSParameter Property

* * *

#### Description

|  Returns true if measurement represents an S-Parameter  
---|---  
  
####  VB Syntax

|  value = meas.IsSparameter  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A Measurement (object)  
value |  (Boolean) True - measurement is an S-Parameter False - measurement is NOT an S-Parameter  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  print app.IsSparameter  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT IsSparameter( [out, retval] VARIANT_BOOL * bVal);  
  
#### Interface

|  IMeasurement2


##### Read-only

|

##### [About Equation Editor](../../../S4_Collect/Equation_Editor.md)  
  
---|---  
  
## IsLibraryImported Method

* * *

#### Description

| Returns whether a DLL has been imported into the VNA.  
---|---  
  
####  VB Syntax

| flag = equation.IsLibraryImported location  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
flag | (Boolean) True \- DLL has been imported. False \- DLL has NOT been imported.  
equation | A [MeasurementEquation](../Objects/MeasurementEquation_Object.md) object  
location | (string)  Full path and filename of the *.dll.  
  
#### Return Type

| Variant boolean  
  
#### Default

| Not Applicable  
  
#### Examples

| flag=equation.IsLibraryImported C:\Program Files(x86)\Keysight\Network
Analyzer\UserFunctions\Expansion.dll  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT IsLibraryImported( BSTR filename, VARIANT_BOOL* pImported);  
  
#### Interface

| IMeasurementEquation  
  
* * *


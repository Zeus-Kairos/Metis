##### Write-only

|

##### [About Interface Control](../../../System/Interface_Control.md)  
  
---|---  
  
# ConfigurationFile Property

* * *

#### Description

| Recalls an Interface Control file from the hard drive into the analyzer.  
---|---  
  
####  VB Syntax

| IntControl.ConfigurationFile = filename  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
IntControl | An [InterfaceControl](../Objects/InterfaceControl_Object.md) (object)  
filename | (string) \- Full path, file name, and extension (.xml) of the file to recall. Files are typically stored in "c:\users\public\network analyzer\documents"  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| IntControl.ConfigurationFile = "c:\users\public\network
analyzer\documents\MySettings.xml"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT put_ConfigurationFile(BSTR bstrFile)  
  
#### Interface

| IInterfaceControl


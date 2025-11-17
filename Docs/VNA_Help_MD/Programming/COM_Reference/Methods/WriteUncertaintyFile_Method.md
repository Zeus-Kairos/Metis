##### Write-only  
  
---  
  
## WriteUncertaintyFile Method

* * *

#### Description

| Saves uncertainty data for the specified ports in three different formats.  
---|---  
  
#### VB Syntax

| data = uncert.WriteUncertaintyFile ports, filename  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data | (Variant) array to store the data.  
uncert | An [Uncertainty](../Objects/Uncertainty_Object.md) (object)  
ports | (Variant Array) One dimensional array containing a list of port numbers for which data is requested.  
filename | (string) \- Path, filename, and suffix of location to store the uncertainty data, enclosed in quotes. The suffix is not checked for accuracy.

  * (*.u*p) S-parameter Uncertainty File - If saving 2 ports, specify "filename.u2p"; If saving 4 ports, specify "filename.u4p.", and so forth.
  * (*.dsd) S-parameter Data Standard Definition file - Data for ONLY one or two ports is allowed.
  * (*.sdatcv) METAS S-parameter Covariance File.

  
  
#### Return Type

| Not Applicable  
  
#### Default

| Not Applicable  
  
#### Examples

| 'This VBScript example can be pasted into a notepad file and run on the VNA
as a macro. [Learn how.](../../Using_Macros.md) Dim app As
AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim oUncert as Uncertainty  
Set oUncert = app.ActiveMeasurement.Uncertainty 'List the port numbers for
required data ports = Array(1,2) 'specify where to save the data and data
suffix 'remove comment for one of the following: filename="D:\MyData.u2p"
'filename="D:\MyData.dsd" 'filename="D:\MyData.sdatcv"
OUncert.WriteUncertaintyFile ports,filename  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT WriteUncertaintyFile(VARIANT portsToMeasure,BSTR filename);  
  
#### Interface

| IUncertainty  
  
* * *


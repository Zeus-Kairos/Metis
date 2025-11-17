##### Write-only  
  
---  
  
## WriteSnpFileWithSpecifiedPorts Method

* * *

#### Description

| Note: This command replaces [app.Save (.snp)](Save_Method.md). This command
is more explicit regarding the data to be saved, and works for VNAs with
multiport test sets. Saves SNP data to the specified file. [Learn more about
SNP data.](../../../S5_Output/SaveRecall.htm#An *.s3p)  
---|---  
  
####  VB Syntax

| data = meas.WriteSnpFileWithSpecifiedPorts ports, filename  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data | (Variant) array to store the data.  
meas | A [Measurement](../Objects/Measurement_Object.md) (object)  
ports | (Variant Array) One dimensional array containing a list of port numbers for which snp data is requested.  
filename | (string) \- Full path, filename, and suffix to store the data. The suffix is not checked for accuracy. If saving 2 ports, specify "filename.s2p"; If saving 3 ports, specify "filename.s3p." and so forth. SNP data can be output using several data formatting options. See [SNPFormat Property](../Properties/SnPFormat_Property.md)  
  
#### Return Type

| Variant array - automatically dimensioned to the size of the data.  
  
#### Default

| Not Applicable  
  
#### Examples

| 'This VBScript example can be pasted into a notepad file and run on the VNA
as a macro. [Learn how.](../../Using_Macros.md) Set pna =
CreateObject("AgilentPnA835x.application") Set meas = pna.ActiveMeasurement
'List the port numbers for required data ports = Array(1,2,4) 'specify where
to save the data filename="C:\Program Files(x86)\Keysight\Network
Analyzer\Documents\MyData.s3p" meas.WriteSnpFileWithSpecifiedPorts
ports,filename  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

| HRESULT WriteSnpFileWithSpecifiedPorts(VARIANT portsToMeasure,BSTR
filename);  
  
#### Interface

| IMeasurement7  
  
* * *


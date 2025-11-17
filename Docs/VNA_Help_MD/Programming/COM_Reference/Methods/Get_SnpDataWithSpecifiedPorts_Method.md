##### Read-only  
  
---  
  
## GetSnPDataWithSpecifiedPorts Method

* * *

#### Description

|  Note: This command replaces [Get SnPData](Get_SnPData_Method.md). This
command is more explicit regarding the data to be returned, and works for VNAs
with multiport test sets. Reads SnP data for the measurement by specifying the
VNA port numbers. [Learn more about SnP that is returned from the
VNA.](../../../S5_Output/SaveRecall.htm#An *.s3p)  
---|---  
  
####  VB Syntax

|  data = meas.GetSnPDataWithSpecifiedPorts ports  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  (Variant) array to store the data.  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
ports |  (Variant Array) One-dimensional array containing the list of port numbers for which data is required.  
  
#### Return Type

|  Variant - 3 dimensional array.

  * First dimension size is number of parameters returned.
  * Second dimension size is number of points in the channel
  * Third dimension size is 2; format of the data is specified with [SnPFormat Property](../Properties/SnPFormat_Property.md).

For example: Data(0,5,1) returns the imaginary part of the fifth data point of
S11 (if the s2p request includes port #1)  
  
#### Default

|  Not Applicable  
  
#### Example

|  'This VBScript example can be pasted into a notepad file and run on the VNA
as a macro. [Learn how.](../../Using_Macros.md) Dim pna Dim meas Dim param
Dim point Dim snp Dim ports 'List the port numbers for required data ports =
Array(3,4) Set pna = CreateObject("AgilentPnA835x.application") Set meas =
pna.ActiveMeasurement 'limit amount of data to display set
chan=pna.ActiveChannel chan.NumberOfPoints=2 snp =
meas.GetSnPDataWithSpecifiedPorts (ports) ' returns a 3 dimensional array '
snp(param,point,data pair) '\------------------------------------- ' show me
the data For param = LBound(snp, 1) To UBound(snp, 1) MsgBox ("Parameter: " &
(param + 1)) For point = LBound(snp, 2) To UBound(snp, 2) MsgBox "Point:" &
(point + 1) & " " & snp(param, point, 0) & "," & snp(param, point, 1) Next
Next  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetSnpDataWithSpecifiedPorts(VARIANT portsToMeasure,VARIANT*
response);  
  
#### Interface

|  IMeasurement7  
  
* * *


##### Read-only  
  
---  
  
## GetSnPData Method Superseded

* * *

#### Description

|  Note: this command is replaced by [Get SnpDataWithSpecifiedPorts
Method](Get_SnpDataWithSpecifiedPorts_Method.htm). Reads SnP data from the
selected measurement. [Learn more about SnP that is returned from the
VNA.](../../../S5_Output/SaveRecall.htm#An *.s3p)  
---|---  
  
####  VB Syntax

|  data = meas.GetSnPData type  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
data |  Variant array to store the data.  
meas |  A Measurement (object)  
type |  (string) \- Type of SnP data to return. If unspecified, <n> is set to 2. Choose from: "S1P" r**eturns 1-Port data for the active measurement if the active measurement is a reflection parameter such as S11 or S22. The behavior is UNDEFINED if the active measurement is a transmission parameter such as an S21**. "S2P" returns data for the current 2-port measurement (4 S-parameters). "S3P" returns data for the current 3 port measurement (9 S-parameters). Valid only on instruments with 3 ports or more. "S4P" returns data for the current 4 port measurement (16 S-parameters). Valid only on instruments with 4 ports or more. SnP data can be output using several data formatting options. See [SnPFormat Property](../Properties/SnPFormat_Property.md)  
  
#### Return Type

|  Variant - 3 dimensional array.

  * First dimension size is number of parameters returned.
  * Second dimension size is number of points in the channel
  * Third dimension size is 2 (real,imaginary)

For example: Data(0,5,1) returns the imaginary value of the fifth data point
of S11 (if the s2p request includes port #1)  
  
#### Default

|  Not Applicable  
  
#### Examples

|  snp = meas.GetSnPData("s1p")  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT GetSnPData( BSTR snptype, VARIANT * response)  
  
#### Interface

|  IMeasurement3  
  
* * *


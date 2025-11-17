##### Write-Read

|

##### [SCPI Command Tree](../../GP-IB_Command_Finder/SCPI_Command_Tree.md)  
  
---|---  
  
## Parse Method

* * *

#### Description

|  Allows the use of COM to send a SCPI command. [See a C++
example](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)
of how to return error information when using this command. Note: The
SCPIStringParser Methods can NOT be used with [SCPI Status
Reporting](../../GP-IB_Command_Finder/Status.htm). However, the *OPC? will
work.  
---|---  
  
####  VB Syntax

|  scpi.Parse ("SCPI command")  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
scpi |  A [ScpiStringParser](../Objects/SCPIStringParser_Object.md) (object)  
SCPI command |  (string) - Any valid SCPI command  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim scpi As ScpiStringParser  
Set scpi = app.ScpiStringParser  
Dim startfreq As Double  
startfreq = 100e6  
'  
scpi.Parse "Sens:Freq:Start " & startfreq'Write  
|  Dim str As String  
str = scpi.Parse ("Sens:Freq:Start?")'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Parse(BSTR SCPI_Command, BSTR *pQueryResponse)  
  
#### Interface

|  IScpiStringParser  
  
* * *


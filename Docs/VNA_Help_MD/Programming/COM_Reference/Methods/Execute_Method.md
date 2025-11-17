##### Read-only

# Execute Method

* * *

#### Description

|  Allows the use of COM to send a SCPI command. This method can be used with
:SYST:ERR? to convert scpi errors into text. [See an
example](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)
of how to return error information when using the [Parse
method](Parse_Method.htm). Note: The SCPIStringParser Methods can NOT be used
with [SCPI Status Reporting](../../GP-IB_Command_Finder/Status.md). However,
the *OPC? will work.  
---|---  
  
####  VB Syntax

|  Scpi.Execute (SCPI_Command)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
scpi |  A [ScpiStringParser](../Objects/SCPIStringParser_Object.md) (Object)  
SCPI_Command |  (String) \- Any valid SCPI command  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim scpi As ScpiStringParser Set scpi = app.ScpiStringParser  
scpi.Execute("SYST:PRES"); ErrorString = scpi.Execute("SYST:ERROr?");  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  Execute(BSTR SCPI_Command, BSTR * pQueryResponse);  
  
#### Interface

|  IScpiStringParser2  
  
* * *


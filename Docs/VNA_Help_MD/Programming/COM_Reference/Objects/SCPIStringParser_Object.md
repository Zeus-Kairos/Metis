# SCPIStringParser Object

* * *

### Description

Provides the ability to send a SCPI command from within the COM command. The
two commands differ in the following ways:

Execute \- will not return an error unless the Execute command itself fails,
which is unlikely. Otherwise, you are required to read the SCPI error queue
for errors that were caused by the SCPI command. The Execute command operates
with minimal interference between you, the programmer, and the SCPI parser. It
does not presume how you want to handle errors: handle by ignore, handle by
reading the status byte, etc. This command was defined because automation
engines like VB throw runtime errors when a COM method returns a failed
HRESULT.

Parse \- parses the input command, and then reads the SCPI error queue until
the queue is empty. If the queue contains errors, Parse returns a failed
HRESULT (E_NA_BAD_SCPI_EXECUTE). It then creates an IErrorInfo object and
bundles the error numbers and descriptions into the error object. This object
is available so that you can detect the failed HRESULT and interrogate the
errorInfo object for more details.

The SCPIStringParser Methods can NOT be used with:

  * [SCPI Status Reporting](../../GP-IB_Command_Finder/Status.md). However, the *OPC? will work.
  * Transferring Binary (block) data with commands such as: [MMEM:TRAN](../../GP-IB_Command_Finder/Memory.md#Transfer) or [CALC:DATA](../../GP-IB_Command_Finder/Calculate/Data.md#data) with [Format:Data](../../GP-IB_Command_Finder/Format_SCPI.md#fd) set to Real32 or Real64

  
---  
  
### Accessing the ScpiStringParser object

Dim app As AgilentPNA835x.Application  
Set app = CreateObject("AgilentPNA835x.Application", <analyzerName>)  
  
Dim SCPI As IScpiStringParser  
Set SCPI = app.ScpiStringParser

### See Also:

  * [VNA Automation Interfaces](../../Learning_about_COM/PNA_Automation_Interfaces.md)

  * [The VNA Object Model](The_Analyzer_Object_Model.md)

  * [Example Programs](../../COM_Example_Programs/COM_Example_Intro.md)

  * [See an example](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.md) of how to return error information when using the [Parse method](../Methods/Parse_Method.md).

### Methods

|

### Interface

|

### Description  
  
---|---|---  
[Parse](../Methods/Parse_Method.md) |  ISCPIStringParser |  Provides the ability to send a SCPI command from within the COM command.  
[Execute](../Methods/Execute_Method.md) |  ISCPIStringParser2 |  Does not convert scpi errors. Use :SYST:ERR?  
  
#### Properties

|

####

|

####  
  
None |  |   
  
###  History

Interface |  Introduced with VNA Rev:  
---|---  
ISCPIStringParser |  1.0  
ISCPIStringParser2 |  3.0


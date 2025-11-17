# Transfer a VNA State File to an External PC Using C#

## Summary

Saving a state file and transferring that state file to another PC is a
commonly automated task.

## Prerequisites

This example was created in Microsoft Visual Studio 2022. Before running the
example code below, ensure the systems and code are set up properly:

  1. Change the IP address to that of the VNA host controller (or localhost to use on the same PC).

  2. (Optional) Change the file name or path to save the state file in and transfer it to.

  3. On the VNA system, make sure that Enable Remote Drive Access is enabled in Instrument > Setup > System Setup > Remote Interface 

  4. This program uses the Ivi.Visa.Interop library commonly found here:

C:\Program Files\IVI Foundation\VISA\VisaCom64\Primary Interop
Assemblies\Ivi.Visa.Interop.dll

Add this assembly as a project reference in Visual Studio or whatever IDE this
is running from to get access to ResourceManager and FormattedIO488.

Note: Enabling "Enable Remote Drive Access" may make your system less secure.
Please ensure you are following appropriate security measures before checking
this box.

## Example

* * *

`using` `System;`

`using` `Ivi.Visa.Interop;`

`namespace` `CSharp_TransferStateFile`

`{`

` ``internal` `class` `Program`

` ``{`

` ``static` `void` `Main(``string``[] args)`

` ``{`

` ``// Create the Visa Interop objects so we can use their API`

` ``ResourceManager rm = ``new` `ResourceManager();`

` ``FormattedIO488 fio = ``new` `FormattedIO488();`

` ``// Connect to a VISA address`

` ``string` `VISA_ADDRESS = ``"TCPIP0::localhost::hislip0::INSTR"``;`

` ``fio.IO = (IMessage)rm.Open(VISA_ADDRESS);`

` ``// Send identification request to instrument`

` ``fio.WriteString(``"*IDN?"``);`

` ``ReadResponse(fio);`

` ``// Save instrument state (change to desired path)`

` ``string` `stateSavePath = ``"c:/temp/myStateFile.sta"``;`

` ``fio.WriteString($``"MMEMory:STORe:CSARchive '{stateSavePath}'"``);`

` ``// Grab state file from controller`

` ``fio.WriteString($``"MMEM:TRAN? '{stateSavePath}'"``);`

` ``byte``[] data =
(``byte``[])fio.ReadIEEEBlock(IEEEBinaryType.BinaryType_UI1);`

` ``File.WriteAllBytes(``"c:/temp/myStateFile.sta"``, data);`

` ``// Close connection to instrument`

` ``fio.IO.Close();`

` ``}`

` ``private` `static` `void` `ReadResponse(FormattedIO488 fio)`

` ``{`

` ``// Try to read the instrument's response`

` ``try`

` ``{`

` ``string` `response = fio.ReadString();`

` ``Console.WriteLine(response);`

` ``PrintErrors(fio);`

` ``}`

` ``catch` `(Exception ex)`

` ``{`

` ``// If error, write to console instead of crashing program`

` ``Console.WriteLine(ex.Message);`

` ``}`

` ``}`

` ``private` `static` `void` `PrintErrors(FormattedIO488 fio)`

` ``{`

` ``// Check how many errors are in the queue`

` ``fio.WriteString(``"SYST:ERR:COUN?"``);`

` ``int` `errorCount = ``int``.Parse(fio.ReadString());`

` ``if` `(errorCount == 0)`

` ``return``; ``// no errors`

` ``else`

` ``{`

` ``string` `errorMessage;`

` ``// Print each error message to console`

` ``for` `(``int` `i = 0; i < errorCount; i++)`

` ``{`

` ``fio.WriteString(``"SYST:ERR?"``);`

` ``errorMessage = fio.ReadString();`

` ``Console.WriteLine(errorMessage);`

` ``}`

` ``}`

` ``}`

` ``}`

`}`

* * *


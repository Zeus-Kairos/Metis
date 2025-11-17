# Shut Down the VNA Remotely

* * *

Shutdown the VNA remotely by creating and then executing a macro.

Learn more about [Macros in the VNA](../Using_Macros.md)

### Create the Macro

  1. Click Utility, then Macro, then Macro Setup

  2. In the Macro Setup dialog, select a blank line, then click Edit.

  3. In the Edit Macro dialog:

     1. Under Title, enter Shutdown

     2. Under Macro Executable, enter Shutdown

     3. Under Macro run string parameters, enter -s -t 0 This will wait 0 seconds before executing the command.

### Execute the Macro Remotely

Send the following SCPI command:

  * [SYST:SHOR<n>:EXEC](../GP-IB_Command_Finder/System.md#MacroExecute) where <n> is the number (formerly 'blank' line) of the macro that is stored in the VNA.

### Variations

To see variations on this command, on any Windows computer:

  * From any command prompt, enter help shutdown

* * *


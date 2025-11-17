# RF PathConfiguration Example

* * *

Note: These commands are accessible only for PNA-X models.

These Visual Basic and [C# examples](PathConfiguration_Example.md#CSharp)
exercise various commands on the:

  * [PathConfigurationManager Object](../COM_Reference/Objects/PathConfigurationManager_Object.md)

  * [PathConfiguration Object](../COM_Reference/Objects/PathConfiguration_Object.md)

  * [PathElement Object](../COM_Reference/Objects/PathElement_Object.md)

### See Also

[IFPathConfiguration Setup](IFPathConfiguration_Setup.md) example

### VB Example

' Create / Get the VNA application Dim app Set app =
CreateObject("AgilentPNA835x.Application") ' Preset the instrument app.Preset
' Get a channel interface on which to operate Dim chan Set chan =
app.ActiveChannel ' Modify the Default configuration, and save it as My
Config chan.PathConfiguration = "Default" ' Set the Combiner element to
value Reversed chan.PathConfiguration.Element("Combiner").Value = "Reversed"
' Set the Src1 element to value High Power
chan.PathConfiguration.Element("Src1").Value = "High Power" ' Change the
description text chan.PathConfiguration.DescriptionText = "Connect J8 to J9."
' Store the modified configuration chan.PathConfiguration.Store ("My Config")
' Set the instruments path config back to the default (req. 8)
chan.PathConfiguration = "Default" ' Load a previously saved configuration
onto channel 1 app.PathConfigurationManager.Load 1, "My Config"  
---  
  
### C# Example

Type pnaType = Type.GetTypeFromProgID("AgilentPNA835x.Application", "PNA-NAME-
HERE"); AgilentPNA835x.Application pna =
(AgilentPNA835x.Application)Activator.CreateInstance(pnaType);
AgilentPNA835x.Channel chan = (AgilentPNA835x.Channel)pna.ActiveChannel; //
Preset the Instrument pna.Preset(); // Modify the Default configuration, and
save it as "My Config" chan.set_PathConfiguration("Default"); // Set the
"Combiner" element to value "Reversed"
chan.get_PathConfiguration().get_Element("Combiner").Value = "Reversed"; //
Change the description text chan.get_PathConfiguration().DescriptionText =
"Connect J8 to J9."; // Store the modified configuration
chan.get_PathConfiguration().Store("My Config"); // Set the instruments path
config back to the default (req. 8) chan.set_PathConfiguration("Default"); //
Load a previously saved configuration onto channel 2
pna.PathConfigurationManager.LoadConfiguration(1, "My Config");  
---  
  
* * *


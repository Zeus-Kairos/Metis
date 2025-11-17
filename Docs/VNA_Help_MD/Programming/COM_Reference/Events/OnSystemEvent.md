|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnSystemEvent

* * *

#### Description

|  Triggered by a system event. See a list of [System
Events](../../../Support/PNA_Errors.htm#General), also known as general
events. See also [EnableSourceUnleveledEvents
Property](../Properties/EnableSourceUnleveledEvents_Property.htm) Note: Some
Severe Events are also used as Error Messages  
---|---  
  
####  VB Syntax

|  Sub app_OnSystemEvent(ByVal eventID As Variant)  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
eventID |  Code number of the event which occurred  
chanNum |  Channel Number of the event  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  Private Sub pna_OnSystemEvent(ByVal eventID As Variant)  
MsgBox ("A System event has occured")  
End Sub  
  
* * *  
  
#### C++ Syntax

|  HRESULT OnSystemEvent(VARIANT eventID)  
  
#### Interface

|  IApplication  
  
### Selected System Events

2048 [naEventID_OPTION_NOT_INSTALLED](../../../Support/PNA_Errors.md#12048)

2049 [naEventID_FEATURE_NOT_AVAILABLE](../../../Support/PNA_Errors.md#12049)

2050 [naEventID_FEATURE_NOT_VALID](../../../Support/PNA_Errors.md#12050)

2051 [naEventID_SAVEFILE_OK](../../../Support/PNA_Errors.md#12051)

2063 [naEventID_RECALLFILE_SUCCESS](../../../Support/PNA_Errors.md#12063)

2130 [naEventID_PRINTER_TROUBLE](../../../Support/PNA_Errors.md#12130)

2133 [naEventID_TRIGGERDENIED](../../../Support/PNA_Errors.md#12133)

2134 [naEventID_MACRO_FAILED](../../../Support/PNA_Errors.md#12134)

2144 [naEventID_NO_LICENSE](../../../Support/PNA_Errors.md#12144)

2163 [naEventID_PRESET](../../../Support/PNA_Errors.md#12163)

2166 [naEventID_TRIGGERFAILED](../../../Support/PNA_Errors.md#12166)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *


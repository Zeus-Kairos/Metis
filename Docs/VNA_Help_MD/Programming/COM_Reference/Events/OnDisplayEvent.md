#####

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnDisplayEvent

* * *

#### Description

|  Triggered by a display event.  
---|---  
  
####  VB Syntax

|  Sub app_OnDisplayEvent(ByVal eventID As Variant, ByVal winNum As Variant,
ByVal traceNum As Variant)  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
eventID |  Code number of the event which occurred  
winNum |  Window Number of the event  
traceNum |  Trace Number of the event  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  Sub pna_OnDisplayEvent(ByVal eventID As Variant, ByVal windowNumber As
Variant, ByVal traceNumber As Variant)  
MsgBox ("A Display event has occured")  
End Sub  
  
* * *  
  
#### C++ Syntax

|  HRESULT OnDisplayEvent(VARIANT eventID, VARIANT windowNumber, VARIANT
traceNumber)  
  
#### Interface

|  IApplication  
  
### Selected Display Events

1541 [naEventID_PRINT_SETUP_FAILURE](../../../Support/PNA_Errors.md#11541)

1542 [naEventID_PRINT_CANCELED](../../../Support/PNA_Errors.md#11542)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *


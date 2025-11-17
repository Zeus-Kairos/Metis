#####

|

##### [About Analyzer
Events](../../Learning_about_COM/Working_with_PNA_Events.htm)  
  
---|---  
  
## OnMeasurementEvent

* * *

#### Description

|  Triggered by a measurement event.  
---|---  
  
####  VB Syntax

|  Sub app_OnMeasurementEvent(ByVal eventID As Variant, ByVal measNum As
Variant)  
  
* * *  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An Application (object)  
eventID |  Code number of the event which occurred  
measNum |  Measurement Number of the event  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
* * *  
  
#### Examples

|  Private Sub pna_OnMeasurementEvent(ByVal eventID As Variant, ByVal
measurementNumber As Variant)  
  
MsgBox ("A Measurement event has occured")  
  
End Sub  
  
* * *  
  
#### C++ Syntax

|  HRESULT OnMeasurementEvent(VARIANT eventID, VARIANT measurementNumber)  
  
#### Interface

|  IApplication  
  
### Selected Measurement Events

1024 [naEventID_NO_VALID_MEMORY_TRACE](../../../Support/PNA_Errors.md#11024)

1028 [naEventID_LIMIT_FAILED](../../../Support/PNA_Errors.md#11028)

1029 [naEventID_LIMIT_PASSED](../../../Support/PNA_Errors.md#11029)

1034 [naEventID_MEMORY_NOT_SAVED](../../../Support/PNA_Errors.md#11034)

1035 [naEventID_SET_AVERAGE_COMPLETE](../../../Support/PNA_Errors.md#11035)

1036 [naEventID_CLEAR_AVERAGE_COMPLETE](../../../Support/PNA_Errors.md#11036)

1111
[naEventID_MARKER_BANDWIDTH_NOT_FOUND](../../../Support/PNA_Errors.md#11111)

1112 [naEventID_PEAK_NOT_FOUND](../../../Support/PNA_Errors.md#11112)

1113 [naEventID_TARGET_VALUE_NOT_FOUND](../../../Support/PNA_Errors.md#11113)

### See Also

[Errors and the SCPIStringParser
Object](../../COM_Example_Programs/Errors_and_the_SCPIStringParser_Object.htm)

* * *


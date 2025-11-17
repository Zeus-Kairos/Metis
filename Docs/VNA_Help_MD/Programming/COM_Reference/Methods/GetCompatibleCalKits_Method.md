##### Read-only

## GetCompatibleCalKits Method

* * *

#### Description

|  Note: This command replaces [CompatibleCalKits
Property](../Properties/CompatibleCalKits_Property.htm) Returns a comma-
separated list of valid kits that use the specified connector type. This
includes mechanical cal kits, applicable characterizations found within ECal
modules currently connected to the VNA, and all user characterizations stored
in VNA disk memory. For ECal modules, the returned list includes the serial
numbers. See the [ECalUserCharacterizer
Object](../Objects/ECalUserCharacterizer_Object.htm). Use items in the list to
select the kit to be used with the [CalKitType
Property](../Properties/CalKitType_Property.htm)  
---|---  
  
####  VB Syntax

|  value = guidCal.GetCompatibleCalKits (connectorType)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
value |  (Variant) - Variable to store the returned list of cal kits. One-dimensional array of string values.  
guidCal |  A [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
connectorType |  (String) Connector type for which compatible cal kits will be returned. Use [ValidConnectorType](../Properties/ValidConnectorType_Property.md) to return a list of connector type strings. Use [ConnectorType](../Properties/ConnectorType_Property.md) to set the connector type for each port to be calibrated.  
  
#### Return Type

|  Variant  Containing one-dimensional array of strings.  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim kits As Variant kits = guidedCal.GetCompatibleCalKits "Type N (50)
male"  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT GetCompatibleCalKits(BSTR connector, VARIANT* Kits);  
  
#### Interface

|  IGuidedCalibration5  
  
* * *

  


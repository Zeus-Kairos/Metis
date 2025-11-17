# CoupledMarkersMethod Property

##### Write/Read

|

##### [About Coupled Markers](../../../S4_Collect/Markers.md#Coupled_Markers)  
  
---|---  
  
* * *

#### Description

|  Sets and Reads the scope Coupled Markers. Note: This command will not take
effect until [CoupledMarkers Property](CoupledMarkers_Property.md) is turned
on. Note: The preset behavior of Coupled Markers depends on the setting of
[MarkCoupControlsMkrState](MarkCoupControlsMkrState_Property.md),
[MarkCoupMethPresetIsChan](MarkCoupMethPresetIsChan_Property.md), and
[MarkCoupPresetIsOn](MarkCoupPresetIsOn_Property.md).  
---|---  
  
####  VB Syntax

|  app.CoupledMarkersMethod = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
value |  (Enum as NAMarkerCouplingMethod) 0 - naMarkerCouplingAll - Coupling occurs across all channels. 1 - naMarkerCouplingChannel - Coupling is limited to traces in the same channel.  
  
#### Return Type

|  Enum  
  
#### Default

|  0 - naMarkerCouplingAll  
  
#### Examples

|  app.CoupledMarkersMethod = naMarkerCouplingAll 'Write  
coupl = app.CoupledMarkersMethod 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CoupledMarkersMethod(tagNAMarkerCouplingMethod, value) HRESULT
get_CoupledMarkersMethod(NAMarkerCouplingMethod, *value)  
  
#### Interface

|  IApplication20  
  
* * *


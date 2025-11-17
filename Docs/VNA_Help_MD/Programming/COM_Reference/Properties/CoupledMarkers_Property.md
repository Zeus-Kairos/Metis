##### Write/Read

|

##### [About Coupled Markers](../../../S4_Collect/Markers.md#Coupled_Markers)  
  
---|---  
  
## CoupledMarkers Property

* * *

#### Description

|  Sets and Reads the state of Coupled Markers (ON and OFF). See also:
[CoupledMarkersMethod Property](CoupledMarkersMethod_Property.md)  
---|---  
  
####  VB Syntax

|  app.CoupledMarkers = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
state |  (boolean)  
False (0) \- Turns Coupled Markers OFF True (1) \- Turns Coupled Markers ON  
  
#### Return Type

|  Boolean  
False \- OFF True \- ON  
  
#### Default

|  False  
  
#### Examples

|  app.CoupledMarkers = True 'Write  
coupl = app.CoupledMarkers 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_CoupledMarkers(VARIANT_BOOL bState)  
HRESULT get_CoupledMarkers(VARIANT_BOOL *bState)  
  
#### Interface

|  IApplication  
  
* * *


##### Write only

## Initialize Method

* * *

#### Description

|  Begins a calibration. Note: chan must be the active channel. For ECal User
Characterization, use [Initialize (ECal](Initialize_ECal.md)).  
---|---  
  
####  VB Syntax

|  obj.Initialize (chan, useCalStorPref)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object)  
  
#### chan

|  (Long) Channel number to calibrate.  
  
#### useCalStorPref

|  (boolean) True or 1 \- Assignment of Cal Set will be based on the setting
of the
[RemoteCalStoragePreference](../Properties/RemoteCalStoragePreference_Property.md)
COM property. False or 0  If the channel currently has a selected Cal Set,
the calibration will be stored to that Cal Set. Otherwise, the assignment of
Cal Set is based upon the setting of the
[RemoteCalStoragePreference](../Properties/RemoteCalStoragePreference_Property.md)
COM property.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  smc.Initialize(2,True)  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_Initialize(long channelnumber, VARIANT_BOOL bCalPref);  
  
#### Interface

|  IGuidedCalibration SMCType VMCType  
  
* * *


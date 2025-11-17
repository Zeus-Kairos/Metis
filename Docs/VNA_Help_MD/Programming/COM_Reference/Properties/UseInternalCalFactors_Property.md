##### Write/Read

|

##### [About Sensor Cal
Factors](../../../System/Configure_a_Power_Meter_As_Receiver.htm#SensorDiag)

[About PMAR](../../../System/Configure_a_Power_Meter_As_Receiver.md)  
---|---  
  
## UseInternalCalFactors Property

* * *

#### Description

|  Enables/disables use of internal calibration factors for power sensors with
built-in calibration factors and reads the current state.  
---|---  
  
####  VB Syntax

|  pwrSensor.UseInternalCalFactors = state  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
pwrSensor |  A [PowerSensorAsReceiver](../Objects/PowerSensorAsReceiver_Object.md) (object)  
state |  (boolean) False \- Disables the use of internal calibration factors. True \- Enables the use of internal calibration factors.  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  ' This example script demonstrates the set/get of the
'UseInternalCalFactors' property ' on the PMAR PowerSensor COM object for an
existing PMAR named 'MyPMAR'. Option Explicit dim app Set app =
CreateObject("AgilentPNA835x.Application") app.Preset app.ActiveChannel.Hold
True app.ActiveChannel.CWFrequency = 1E9 app.ActiveChannel.SweepType = 3
'naCWTimeSweep app.ActiveChannel.NumberOfPoints = 3 dim externalDevices Set
externalDevices = app.ExternalDevices dim externalDevice Set externalDevice =
externalDevices.Item("MyPMAR") externalDevice.Active = True 'Create a PMAR
trace with power sensor connected to port 3
app.ActiveMeasurement.ChangeParameter "MyPMAR", 3 dim PMAR Set PMAR =
externalDevice.ExtendedProperties ' Disable use of the sensor's internal cal
factors, take a sweep and report the Mean PMAR.UseInternalCalFactors = False
externalDevice.IOEnable = True app.ActiveChannel.Single True MsgBox
"UseInternalCalFactors = " & PMAR.UseInternalCalFactors & ", Mean measured val
= " & app.ActiveMeasurement.Mean ' Enable use of the sensor's internal cal
factors, take another sweep and report the Mean again externalDevice.IOEnable
= False PMAR.UseInternalCalFactors = True externalDevice.IOEnable = True
app.ActiveChannel.Single True MsgBox "UseInternalCalFactors = " &
PMAR.UseInternalCalFactors & ", Mean measured val = " &
app.ActiveMeasurement.Mean  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_UseInternalCalFactors(VARIANT_BOOL *pVal) HRESULT
put_UseInternalCalFactors(VARIANT_BOOL Val)  
  
#### Interface

|  IPowerSensorAsReceiver3  
  
* * *


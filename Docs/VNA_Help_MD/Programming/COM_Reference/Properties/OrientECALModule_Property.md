##### Write/Read

## OrientECALModule Property

* * *

#### Description

|  Specifies if the VNA should perform orientation of the ECal module during
calibration. Orientation is a technique by which the VNA automatically
determines which ports of the module are connected to which ports of the VNA.
Orientation begins to fail at very low power levels or if there is much
attenuation in the path between the VNA and the ECal module. Note: For guided
calibrations where Orient is OFF and the same ECal module is used in more than
one Connection Step, you are not allowed to specify how the ECal module is
connected. Instead, the VNA determines the orientation. The VNA does not
verify that you made the connection properly. This setting remains until the
VNA is restarted or this command is sent again. This command, and
[ECALPortMapEx](ECALPortMapEx_Property.md), can be used to perform ECal using
the [Guided Calibration](../Objects/GuidedCalibration_Object.md) interface.  
---|---  
  
####  VB Syntax

|  cal.OrientECALModule = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A [Calibrator](../Objects/Calibrator_Object.md) (object)  
value |  (boolean) False  [DoECAL1PortEX](../Methods/DoECAL1PortEx_Method.md) and [DoECAL2PortEx](../Methods/DoECAL2PortEx_Method.md) methods will use the value of the [ECALPortMapEx](ECALPortMapEx_Property.md) property to determine the port connections. True \- [DoECAL1PortEX](../Methods/DoECAL1PortEx_Method.md) and [DoECAL2PortEx](../Methods/DoECAL2PortEx_Method.md) methods will use auto Orientation technique to determine port connections.  
  
#### Return Type

|  Boolean  
  
#### Default

|  True  
  
#### Examples

|  Dim cal As Calibrator Dim bOrient As Boolean Set cal =
PNAapp.ActiveChannel.Calibrator cal.OrientECALModule = False 'Write bOrient =
cal.OrientECALModule 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_OrientECALModule(VARIANT_BOOL bOrient); HRESULT
get_OrientECALModule(VARIANT_BOOL *bOrient);  
  
#### Interface

|  ICalibrator3  
  
* * *


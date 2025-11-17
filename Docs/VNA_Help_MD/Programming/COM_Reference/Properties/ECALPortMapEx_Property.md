##### Write/Read

## ECALPortMapEx Property

* * *

#### Description

|  This property replaces [ECALPortMap Property](ECALPortMap_Property.md)
Specifies which ports of the ECal module are connected to which ports of the
VNA for the [DoECAL1PortEx](../Methods/DoECAL1PortEx_Method.md) and
[DoECAL2PortEx](../Methods/DoECAL2PortEx_Method.md) methods when the
[OrientECALModule](OrientECALModule_Property.md) property = False. This
setting remains until the VNA is restarted or this command is sent again.
Note: For guided calibrations where Orient is OFF and the same ECal module is
used in more than one Connection Step, you are not allowed to specify how the
ECal module is connected. Instead, the VNA determines the orientation. The VNA
does not verify that you made the connection properly. This command, and
[OrientECALModule_Property](OrientECALModule_Property.md), can be used to
perform ECal orientation using the [Guided
Calibration](../Objects/GuidedCalibration_Object.htm) interface.  
---|---  
  
####  VB Syntax

|  cal.ECALPortMapEx (module) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
module |  (long integer)  Optional argument. ECal module. Choose from modules 1 through 8 Use [IsECALModuleFoundEx](IsECALModuleFoundEx_Property.md) to determine the number of modules connected to the VNA Use [GetECALModuleInfoEx](../Methods/Get_ECALModuleInfoEx_Method.md) to return the model and serial number of each module.  
value |  (string) -Format this parameter in the following manner: Aw,Bx,Cy,Dz where

  * A, B, C, and D are literal ports on the ECAL module
  * w,x,y, and z are substituted for VNA port numbers to which the ECAL module port is connected.

Ports of the module which are not used are omitted from the string. For
example, on a 4-port ECal module with

  * port A connected to VNA port 2
  * port B connected to VNA port 3
  * port C not connected
  * port D connected to VNA port 1

the string would be: A2,B3,D1 DoECAL1PortEx or DoECAL2PortEx methods will fail
if the port numbers passed to those methods are not in the string of this
property and [OrientECALModule](OrientECALModule_Property.md) property =
False.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim cal As Calibrator  
Dim sPortMap As String  
Set cal = PNAapp.ActiveChannel.Calibrator  
cal.ECALPortMapEx = a2,b1 'Write  
sPortMap = cal.ECALPortMap 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ECALPortMapEx( long moduleNumber, BSTR strPortMap); HRESULT
get_ECALPortMapEx( long moduleNumber, BSTR *strPortMap);  
  
#### Interface

|  ICalibrator4  
  
* * *


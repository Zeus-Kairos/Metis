##### Write/Read

## ECALPortMap Property - Superseded

* * *

#### Description

|  Note: This command is replaced by
[ECALPortMapEx](ECALPortMapEx_Property.md) Specifies which ports of the ECal
module are connected to which ports of the VNA for the
[DoECAL1Port](../Methods/DoECAL1Port_Method.md) and
[DoECAL2Port](../Methods/DoECAL2Port_Method.md) methods when the
[OrientECALModule](OrientECALModule_Property.md) property = False.  
---|---  
  
####  VB Syntax

|  cal.ECALPortMap = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
value |  (string) (string) -Format this parameter in the following manner: Aw,Bx,Cy,Dz where

  * A, B, C, and D are literal ports on the ECAL module
  * w,x,y, and z are substituted for VNA port numbers to which the ECAL module port is connected.

Ports of the module which are not used are omitted from the string. For
example, on a 4-port ECal module with

  * port A connected to VNA port 2
  * port B connected to VNA port 3
  * port C not connected
  * port D connected to VNA port 1

the string would be: A2,B3,D1 [DoECAL1Port](../Methods/DoECAL1Port_Method.md)
or [DoECAL2Port](../Methods/DoECAL2Port_Method.md) methods will fail if the
port numbers passed to those methods are not in the string of this property
and [OrientECALModule](OrientECALModule_Property.md) property = False.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim cal As Calibrator  
Dim sPortMap As String  
Set cal = PNAapp.ActiveChannel.Calibrator  
cal.ECALPortMap = a2,b1 'Write  
sPortMap = cal.ECALPortMap 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ECALPortMap(tagNAECALModule ecalModule, BSTR strPortMap);
HRESULT get_ECALPortMap(tagNAECALModule ecalModule, BSTR *strPortMap);  
  
#### Interface

|  ICalibrator3


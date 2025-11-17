##### Read/Write

|

#####  
  
---|---  
  
## EcalOrientation2Port Property

* * *

#### Description

|  Specifies which port of the ECal module is connected to which port of the
VNA for the [Do2PortECAL](Do2PortEcal_Property.md) property when the
[AutoOrient](AutoOrient_Property.md) property = False.  
---|---  
  
####  VB Syntax

|  VMC.EcalOrientation2Port (mod) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
mod |  (Long) Module being used for the calibration. Choose from 1 or 2.  
value |  (string) -Format this parameter in the following manner: Aw,Bx,Cy,Dz where

  * A, B, C, and D are literal ports on the ECAL module
  * w,x,y, and z are substituted for VNA port numbers to which the ECAL module port is connected.

Ports of the module which are not used are omitted from the string. For
example, on a 4-port ECal module with

  * port A connected to VNA port 2
  * port B connected to VNA port 3
  * port C not connected
  * port D connected to VNA port 1

the string would be: A2,B3,D1  
  
#### Return Type

|  String  
  
#### Default

|  "A1,B2"  
  
#### Examples

|  VMC.EcalOrientation1Port(1) = "A2,B1"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EcalOrientation2Port(long lModuleNum, BSTR orientation);
HRESULT get_EcalOrientation2Port(long lModuleNum, BSTR *orientation);  
  
#### Interface

|  VMCType


##### Read/Write

|

#####  
  
---|---  
  
## EcalOrientation1Port Property

* * *

#### Description

|  For Mixer Characterization ONLY Specifies which port of the ECal module is
connected to which port of the VNA for the
[Do1PortECAL](Do1PortEcal_Property.md) property when the
[AutoOrient](AutoOrient_Property.md) property = False.  
---|---  
  
####  VB Syntax

|  VMC.EcalOrientation1Port (mod) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
VMC |  [VMCType](../Objects/VMC_Type_Object.md) (object)  
mod |  (Long) 1 \- Use ECAL Module for the calibration.  
value |  (string) - Choose from: "A1" \- ECAL module port A is connected to VNA port 1 "B1" \- ECAL module port A is connected to VNA port 1  
  
#### Return Type

|  String  
  
#### Default

|  "A1" If anything other than port 1 is specified, "B1" will be used. For
example, if "A2" is specified, "B1" is used.  
  
#### Examples

|  VMC.EcalOrientation1Port(1) = "B1"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_EcalOrientation1Port(long lModuleNum, BSTR orientation);
HRESULT get_EcalOrientation1Port(long lModuleNum, BSTR  
  
#### Interface

|  VMCType


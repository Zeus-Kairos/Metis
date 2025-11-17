##### Write/Read

|

##### [About FCA Calibrations](../../../FreqOffset/FCA_Use.md)  
  
---|---  
  
## CalKitType Property

* * *

#### Description

|  Sets and returns the ECal or mechanical cal kit for the specified port
number to be used during the calibration. There is also a [CalKitType
Property](CalKitType_Property.htm) for use during an Unguided Cal. Note:
Sliding loads are not fully supported from the GuidedCalibration object. The
Measure button must be pressed manually on the VNA. Note: This command
replaces [Do1PortEcal Property](Do1PortEcal_Property.md) and [Do2PortEcal
Property](Do2PortEcal_Property.htm) for SMC and VMC Calibrations.  
---|---  
  
####  VB Syntax

|  object.CalKitType (port) = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
object |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object) [SMCType](../Objects/SMC_Type_Object.md) (object) [VMCType](../Objects/VMC_Type_Object.md) (object)  
port |  (Long) Port number to which the cal kit will be assigned. For Guided Cals and SMC, select port number. For VMC calibrations:

  * 1 \- Mixer Input.
  * Any unused port can be used for the mixer output.
  * Output port of MUT +1 \- Output port of the calibration mixer. Generally this is port 3.

  
value |  (string) \- Calibration Kit type. Case-sensitive. Use [GetCompatibleCalKits](../Methods/GetCompatibleCalKits_Method.md) to return a list of valid Cal Kits.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  'Note: All of the following specify port 1 only ' Mechanical Cal Kit
guidedCal.CalKitType(1) = "85052C" ' Standard ECal modules
guidedCal.CalKitType(1) = "N4691-60004 ECal" ' Non-factory ECal
characterizations are specified as follows: guidedCal.CalKitType(1) =
"N4691-60004 User 1 ECal" ' When two or more ECal modules with the same model
number are ' connected, also specify the serial number as follows:
guidedCal.CalKitType(1) = "N4691-60004 ECal 01234" ' When Disk Memory ECal
user characterizations are used, ' specify both the User char and the serial
number as follows: 'guidedCal.CalKitType(1) = "N4691-60004 MyDskChar ECal
01234" ' Turn on auto orientation for the ECal (default behavior).  
value = smc.CalKitType(1) 'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT get_CalKitType( long port, BSTR *calkit) HRESULT put_CalKitType(
long port, BSTR calkit)  
  
#### Interface

|  IGuidedCalibration SMCType VMCType  
  
* * *


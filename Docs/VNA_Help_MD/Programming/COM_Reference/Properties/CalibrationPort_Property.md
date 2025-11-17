##### Read / Write

|

#####  
  
---|---  
  
## CalibrationPort Property - Obsolete

* * *

#### Description

|  Note: Beginning with Rev 6.0, this command is no longer necessary. Because
of improved calibration techniques, Both is always selected although a power
meter measurement is performed only on port 1. Specifies which SMC port to
calibrate.  
---|---  
  
#### VB Syntax

|  SMC.CalibrationPort = value  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
SMC |  [SMCType](../Objects/SMC_Type_Object.md) (object)  
value |  (String) Port number to be calibrated. Choose from:

  * 1 \- SMC forward
  * 2 \- SMC reverse
  * Both

  
  
#### Return Type

|  String  
  
#### Default

|  1  
  
#### Examples

|  value = SMC.CalibrationPort = "Both"  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_CalibrationPort(BSTR port); HRESULT get_CalibrationPort(BSTR
*port);  
  
#### Interface

|  SMCType VMCType


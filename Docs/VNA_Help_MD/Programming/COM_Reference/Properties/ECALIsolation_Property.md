##### Read/Write

|

##### [ About ECAL](../../../S3_Cals/ModifyCalKits.md)  
  
---|---  
  
## ECALIsolation Property

* * *

#### Description

|  Note: The inherent isolation of the VNA is better than that attained with
this command. ONLY use this command when using an external test set, and ONLY
using a 8509x ECal module. Specifies whether the acquisition of the ECal
calibration should include isolation or not.  
---|---  
  
####  VB Syntax

|  cal.ECALIsolation = _value_  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
cal |  A Calibrator (object)  
value |  (boolean) **False** \- Exclude Isolation **True** \- Include Isolation  
  
#### Return Type

|  Boolean  
  
#### Default

|  False  
  
#### Examples

|  Dim oPNA as AgilentPNA835x.Application Dim oCal as Calibrator Set oPNA =
CreateObject("AgilentPNA835x.Application", "MachineName") Set oCal =
oPNA.ActiveChannel.Calibrator ' Uncomment the following line to have the cal
include isolation ' oCal.ECALIsolation = True ' Uncomment the following line
to have the cal omit isolation 'oCal.ECALIsolation = False oCal.DoECAL2Port '
Do the cal  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_ECALIsolation ( VARIANT_BOOL bIsolationState ); HRESULT
get_ECALIsolation ( VARIANT_BOOL *bIsolationState );  
  
#### Interface

|  Calibrator  
  
* * *


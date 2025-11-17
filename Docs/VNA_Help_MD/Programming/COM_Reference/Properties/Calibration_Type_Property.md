##### Write/Read

|

##### [About Performing a Calibration](../../../S3_Cals/Select_Cal.md)  
  
---|---  
  
## CalibrationType Property Superseded

* * *

#### Description

|  Note: This command has been replaced by
[CalibrationTypeID_property](CalibrationTypeID_property.md), which provides
selection of Calibration Type by string. Specifies the type of calibration to
perform or apply to the active S-Parameter measurement. This command determine
the ports involved in the CalType by the ports being used by the active
measurement. For example:

  * If the measurement is an S23, it uses ports 2 and 3.
  * If the measurement is an S22 it will use the legacy load port to figure out which two ports form the caltype. The legacy load port is set using [CreateMeasurement](../Methods/CreateMeasurement_Method.md).
  * If naCalType_ThreePort_SOLT is specified on a 4-port VNA, an E_NA_DEPRECATED_COMMAND error is returned. There is no way to determine the intended three ports.
  * If naCalType_FourPort_SOLT is specified on a 4-port VNA, it is obvious that the ports involved are ports 1,2,3, and 4.

Note: For FCA measurements, use
[CalibrationName](CalibrationName_Property.md) and
[CalibrationTypeID](CalibrationTypeID_property.md).  
---|---  
  
####  VB Syntax

|  meas.CalibrationType = type  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
meas |  A [Measurement](../Objects/Measurement_Object.md) (object)  
type |  (enum NACalType) - Calibration type. Choose from: 0 \- naCalType_Response_Open 1 \- naCalType_Response_Short 2 \- naCalType_Response_Thru 3 \- naCalType_Response_Thru_And_Isol 4 \- naCalType_OnePort 5 \- naCalType_TwoPort_SOLT 6 \- naCalType_TwoPort_TRL 7 - naCalType_None 8 \- naCalType_ThreePort_SOLT 9 \- Custom 10 \- naCalType_FourPort_SOLT  
  
#### Return Type

|  NACalType  
  
#### Default

|  naCalType_None  
  
#### Examples

|  meas.CalibrationType = naCalType_Response_Open 'Write  
meascal = meas.CalibrationType 'Read  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT put_CalibrationType (tagNACalType CalType)  
HRESULT get_CalibrationType (tagNACalType* pCalType)  
  
#### Interface

|  IMeasurement


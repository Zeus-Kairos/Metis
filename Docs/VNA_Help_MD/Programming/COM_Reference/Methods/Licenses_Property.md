##### Read-only

|

##### [About Options](../../../Support/Configurations.md)  
  
---|---  
  
# GetLicenses Method

* * *

#### Description

|  Returns the list of licenses. [See a list of common
licenses](../../../Support/Configurations.htm#options).  
---|---  
  
####  VB Syntax

|  app.Licenses(type)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
app |  An [Application](../Objects/Application_Object.md) (object)  
type |  (Enum as NALicenseSet) Choose the type of licenses to be recalled: 0 - naValidLicenses \- Return a list of licenses which have enabled VNA software features. 1 - naAllLicenses \- Return a list of all installed licenses including the ones not related to the VNA software. 2 - naIgnoredLicenses \- Return a list of VNA software licenses which are either invalid or ignored. This can occur when a transportable license is transported to an instrument that does not support the license feature. In addition, this can occur when multiple licenses for the same base feature are installed and only the least restrictive license is used (the more restrictive licenses are ignored). For example, when transporting multiple Spectrum Analyzer licenses to the same instrument, the license with the greatest frequency range is used and the other licenses are ignored. Note: Licenses not related to the VNA software but installed on the instrument are not reported as ignored when using naIgnoredLicenses.  
  
#### Return Type

|  String  
  
#### Default

|  Not Applicable  
  
#### Examples

|  app.Licenses(naAllLicenses)  
N5242B-423,N5242B-020,N5242B-021,N5242B-022,S93029A/B-1FP  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Licenses(tagNALicenseSet type, BSTR* LicenseString)  
  
#### Interface

|  IApplication23


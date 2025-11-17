##### Write-only

|

##### [About DIQ](../../../Applications/Differential_IQ.md)  
  
---|---  
  
## ActiveXAxis Property

* * *

#### Description

|  Sets the information to display on the X-axis of the selected DIQ
measurement. This command does not change the default setting for new traces.

### See Also:

[XAxisSource Property](XAxisDomain_Property.md) [XAxisDomain
Property](XAxisDomain_Property.htm)  
---|---  
  
####  VB Syntax

|  diqMeas.ActiveXAxis (domain) = source  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
diqMeas |  A [DIQMeas](../Objects/DIQMeasurement_Object.md) (object)  
domain |  (Enum as NAAxisDomainType) \- Domain to display on the X-axis. Choose from: 0  naFrequency \- display the primary frequency range. 1  naPower - display the power sweep range 2  naPhase \- display the phase sweep range 3  naDCValue - display the DC sweep range 4  naPoints - display the data points in the range  
source |  (String) Specific source for the selected domain.  
  
#### Return Type

|  Enum  
  
#### Default

|  0  naFrequency  
  
#### Examples

|  diqMeas.ActiveXAxis(1) = "Port 2" 'Write variable = diqMeas.ActiveXAxis(1)
'Read  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT put_ActiveXAxis(tagNAAxisDomainType domainType, BSTR source);  
  
#### Interface

|  IDifferentialIQMeas  
  
* * *


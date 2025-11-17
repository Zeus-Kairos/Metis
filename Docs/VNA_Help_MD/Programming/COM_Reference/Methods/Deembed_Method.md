##### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Deembed Method

* * *

#### Description

|  De-embeds a fixture from an existing Cal Set based on an S2P file. A new
Cal Set is created with the effects of the fixture removed. When the new Cal
Set is applied to a channel, the effects of the fixturing are removed from the
measurement data. Do NOT enable fixturing. The effects of the fixture are
removed when the new Cal Set is selected and correction is turned ON.  
---|---  
  
####  VB Syntax

|  calMgr.Deembed (cs1,cs2,s2p,port, compPwr,extrap)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  (object) - A [CalManager](../Objects/CalManager_Object.md) object  
cs1 |  (String) Name of an existing Cal Set which resides on the VNA.  
cs2 |  (String) Name of new Cal Set which contains updated error terms with fixture de-embedded.  
s2p |  (String) Name of the S2P file which characterizes the adapter/fixture.  
port |  (Long Integer) Port number from which fixture will be de-embedded.  
compPwr |  (Boolean) True \- When the Cal Set contains a power correction array for the fixture port, that array will be compensated for the fixture loss.  Warning: enabling power compensation can result in an increase in test port power and consequently, increased power to the DUT. Use with caution. False \- Do not compensate for loss in source power through the fixture.  
extrap |  (Boolean) True \- Applies a simple extrapolation when the S2P file has a narrower frequency range than the Cal Set. The values for the first and last data points are extended in either direction to cover the frequency range of the Cal Set. False \- Extrapolation is NOT performed (default setting).  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Example

|  calMgr.Deembed "MyCalSet","MyNewCalSet","Fixture.s2p",1,True,True  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT Deembed (BSTR srcSet, BSTR destSet,BSTR s2p, long port, BOOL
compPwr, BOOL extrap);  
  
#### Interface

|  ICalManager8  
  
* * *


#### Write-only

|

##### [About Cal Plane Manager](../../../S3_Cals/Cal_Plane_Manager.md)  
  
---|---  
  
## CharacterizeFixture Method

* * *

#### Description

|  Characterizes a single fixture based on two existing calsets. To
characterize two adapter/fixtures (on the input AND output of a fixture),
perform this operation twice.  
---|---  
  
#### VB Syntax

|  calmgr.CharacterizeFixture (tier1Cset, tier2Cset, portNum, s2pFile, format,
[dcPhase])  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calMgr |  [Cal Manager](../Objects/CalManager_Object.md) (Object)  
tier1Cset |  (String) Name of Tier-1 calset. The Tier-1 calset MUST be from a calibration that was performed at the input to the adapter/fixture.  
tier2Cset |  (String) Name of Tier-2 calset. The Tier-2 calset MUST be from a calibration that was performed at the DUT reference plane.  
portNum |  (Long Integer) Port number of the calsets to use when the specified calsets are used to calibrate more than one port.  
s2pFile |  (String) Path and filename to which the S2P file is to be saved.  
format |  (Enum as NAPairedDataFormat) Format in which the data is to be saved to the S2P file. Choose from: 0 - naLogMagPhase 1 - naLinMagPhase 2 \- naRealImaginary  
[dcPhase] |  (Integer) Optional argument. The projected phase of S21 at DC where it crosses the X-axis. [Learn more.](../../../S3_Cals/Cal_Plane_Manager.md#Phase)  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  CalManager.CharacterizeFixture ("Tier1", "Tier2", 1,"C:\Users\PNA-
ADMIN\AppData\Local\Keysight\Network Analyzer\CPM\FixtureA.s2p",1,0)  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT CharacterizeFixture(BSTR strCset1, BSTR strCset2, long pNum, BSTR
fileName, tagNAPairedDataFormat format, Int dcPhase);  
  
#### Interface

|  ICalManager10  
  
* * *


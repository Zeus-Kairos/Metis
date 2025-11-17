#### Write-only

|

##### [About Cal Sets](../../../S3_Cals/Cal_Sets.md)  
  
---|---  
  
## Copy Method

* * *

#### Description

|  Creates a new Cal Set and copies the current Cal Set data into it.
Therefore, you now have a clone Cal Set with a different ID. Use this command
to manipulate data on a Cal Set without corrupting the original cal data.  
---|---  
  
#### VB Syntax

|  CalSet.Copy  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
CalSet |  (object) - A [Cal Set](../Objects/CalSet_Object.md) object  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim mgr As CalManager  
Dim ocalset As CalSet  
Dim newcalset As CalSet  
Set mgr = pna.GetCalManager  
'Create a new (empty) Cal Set.  
Set ocalset = mgr.CreateCalSet(1)  
ocalset.Description = "original calset"  
pna.Channel(1).SelectCalSet ocalset.GetGUID, True  
  
'Launch the cal wizard and allow the user to perform the calibration.  
If pna.LaunchCalWizard(False) Then  
'If the Launch returns true then the calibration finished.  
ocalset.Save  
  
'Copy the Cal Set to the new one.  
Set newcalset = ocalset.Copy  
newcalset.Description = "copy of original calset"  
  
Else  
'If the cal doesn't finish, delete the old Cal Set  
'so it isn't taking up unnecessary memory.  
mgr.DeleteCalSet ocalset.GetGUID  
End If As a result, the programmer can manipulate the data in the new Cal Set
and always revert back to the old Cal Set as needed.  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT Copy( ICalSet** pCalSet);  
  
#### Interface

|  ICalSet


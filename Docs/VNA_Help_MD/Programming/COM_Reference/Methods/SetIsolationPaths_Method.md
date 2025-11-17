##### Write only

## SetIsolationPaths Method

* * *

#### Description

|  Adjusts the list of paths (port pairings) for which isolation standards
will be measured during calibration.  
---|---  
  
####  VB Syntax

|  guidedCal.SetIsolationPaths specifier, pathList  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
obj |  Any of the following: [GuidedCalibration](../Objects/GuidedCalibration_Object.md) (object)  
  
#### specifier

|  (Enum) \- Choose from: 0 - naPathsAll \- Measure isolation on all pairings
of the ports that are to be calibrated. 1 - naPathsNone \- Do not measure
isolation on any pairing of the ports to be calibrated. 2 - naPathsAdd \- Add
one or more specific pairings of ports to the list of port pairings for which
isolation will be measured. 3 - naPathsRemove \- Remove one or more specific
pairings of ports from the list of port pairings for which isolation will be
measured.  
  
#### pathlist

|  (Variant)  port numbers in pairs. One-dimensional array of Long Integers.
Note: pathList is evaluated only when specifier is naPathsAdd or
naPathsRemove. For naPathsAll and naPathsNone, pathList is ignored.  
  
#### Return Type

|  Not Applicable  
  
#### Default

|  Not Applicable  
  
#### Examples

|  Dim pathList  
'selecting to measure isolation on all possible paths for the ports about to
be calibrated  
guidedCal.SetIsolationPaths naPathsAll, pathList  
  
'now removing the paths 1-to-2, 2-to-3 and 2-to-4 from the set of all paths  
pathList = Array(1,2,2,3,2,4)  
guidedCal.SetIsolationPaths naPathsRemove, pathList  
  
#### [C++](../../Learning_about_COM/c++_and_the_com_interface.md) Syntax

|  HRESULT SetIsolationPaths(enum NAPortPathSpecifier specifier, VARIANT
pathList);  
  
#### Interface

|  IGuidedCalibration3  
  
* * *


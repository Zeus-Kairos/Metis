##### Write-only

# SetStandardsForClass Method

* * *

#### Description

|  Set the calibration standard numbers for a specified calibration class. To
read the cal standard numbers use [GetStandardsForClass
Method](Get_StandardForClass_Method.htm)  
---|---  
  
####  VB Syntax

|  calKit.SetStandardsForClass (calclassorder, std1, std2, std3, std4, std5,
std6, std7)  
  
#### Variable

|

#### [(Type)](../../Learning_about_COM/COM_Data_Types.md) \- Description  
  
calKit |  A CalKit (object)  
calclassorder |  (enum NACalClassOrder) Cal Class. Choose from: |  0 - naRefl_1_S11  
---  
1 - naRefl_2_S11  
2 - naRefl_3_S11  
3 - naTran_1_S21  
4 - naRefl_1_S22  
5 - naRefl_2_S22  
6 - naRefl_3_S22  
7 - naTran_1_S12  
8 - naRefl_1_S33  
9 - naRefl_2_S33  
10 - naRefl_3_S33  
11 - naTran_1_S32  
12 - naTran_1_S23  
13 - naTran_1_S31  
14 - naTran_1_S13  
15 - naTRL_T  
16 - naTRL_R  
17 - naTRL_L  
std1 std7 |  (long) Calibration Standard Number. Choose from 1 through 30. Std2 through Std7 are optional  
  
#### Return Type

|  Not applicable  
  
#### Default

|  Not applicable  
  
#### Examples

|  calkit.SetStandardsForClass naRefl_3_S11, 3, 5, 6
calkit.SetStandardsForClass naTran_1_S21, 4  
  
#### [C++](../../Learning_about_COM/c%2b%2b_and_the_com_interface.md) Syntax

|  HRESULT SetStandardsForClass(NACalClassOrder calclassorder, long std1, long
std2, long std3, long std4, long std5, long std6, long std7)  
  
#### Interface

|  ICalKit


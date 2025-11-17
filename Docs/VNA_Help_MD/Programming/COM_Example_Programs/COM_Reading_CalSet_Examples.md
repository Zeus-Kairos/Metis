# Reading Cal Set Data using COM

* * *

This example iterates over the entire collection of Cal Sets that currently
reside in the VNA. It reads the entire list of error term strings from each
Cal Set and queries the data for each term. It then does the same for the
standards data.

Learn more about [Reading and Writing Calibration data using
COM.](../Learning_about_COM/Read_and_Write_Calibration_Data_using_COM.htm)

Learn more about [Cal Sets.](../../S3_Cals/Cal_Sets.md)

See example: [Writing Cal Set Data using
COM](Writing_Cal_Set_Data_using_COM.htm)

[See Other COM Example Programs](COM_Example_Intro.md)

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save on
the VNA hard drive as CalSets.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

Dim pna  
Dim cset  
Dim calsets  
  
' create the pna object  
' to run on a remote PC, substitute 'name' for the full computer name of your
VNA  
' to run as a macro on the VNA, remove ,"name"  
Set pna = CreateObject("AgilentPNA835x.Application", "name")  
wscript.echo pna.IDString  
' obtain the calset collection  
Set calsets = pna.GetCalManager.calsets  
  
' loop thru the calsets  
Dim c  
For c = 1 To calsets.count  
Set cset = calsets.Item(c)  
  
' wscript.echo prints values to a message box  
wscript.echo "calset = ", cset.GetGUID, cset.Description  
  
' iterate through error terms data  
Dim vterms,fdata  
vterms = cset.GetErrorTermList2(0, "")  
if (Not IsEmpty(vterms)) then  
For i = LBound(vterms) To UBound(vterms)  
wscript.echo vterms(i)  
vdata = cset.GetErrorTermByString(0,vterms(i))  
fdata = cset.GetErrorTermStimulus(0,vterms(i))  
wscript.echo vdata(1,0), vdata(1,1)  
wscript.echo fdata(1,0), fdata(1,1)  
Next  
end if  
  
' iterate through standards data  
vterms = cset.GetStandardList2("")  
if (Not IsEmpty(vterms)) then  
For i = LBound(vterms) To UBound(vterms)  
wscript.echo vterms(i)  
vdata = cset.GetStandardByString( vterms(i) )  
wscript.echo vdata(1,0), vdata(1,1)  
Next  
end if  
Next

* * *

* * *


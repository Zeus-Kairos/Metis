# Uncertainty on Power Meter

The following program is an example of setting up power uncertainty on a power
meter.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as a <filename>.vbs file. [Learn how to setup and run the
macro.](../Using_Macros.htm#HowToSetup)

### See Also

[ExternalDevices
Collection](../COM_Reference/Objects/ExternalDevices_Collection.htm)

[ExternalDevice Object](../COM_Reference/Objects/ExternalDevice_Object.md)

[PowerSensor Object](../COM_Reference/Objects/PowerSensor_Object.md)

[PowerSensorAsReceiver
Object](../COM_Reference/Objects/PowerSensorAsReceiver_Object.htm)

[PowerSensorCalFactorSegmentPMAR
Object](../COM_Reference/Objects/PowerSensorCalFactorSegmentPMAR_Object.htm)

[PowerLossSegmentsPMAR_Collection](../COM_Reference/Objects/PowerLossSegmentsPMAR_Collection.md)

[PowerLossSegmentPMAR
Object](../COM_Reference/Objects/PowerLossSegmentPMAR_Object.htm)

[User Defined Power Meter Uncertainty File
](Power_Meter_Uncercainty_Using_Standard_Uncertainties.htm)

[Power Meter Uncertainty
dialog](../../System/Configure_a_Power_Meter_As_Receiver.htm#Power_Meter_Uncertainties)
description

[Application Note
(5988-9215EN)](https://www.keysight.com/main/gated.jspx?lb=1&gatedId=287962&cc=US&lc=eng&parentContId=worldwide_home&parentContType=sr&fileType=VIEWABLE&searchType=GR)

' ' Keysight Technologies 2018 ' ' Uncertainty on power meter COM example ' '
This script execute and print the result of all the ' commands related to the
uncertainty on power meter ' by using COM
''''''''''''''''''''''''''''''''''''''''' ' Create the Application object Dim
app Set app = CreateObject("AgilentPNA835x.Application")
''''''''''''''''''''''''''''''''''''''''' 'Get the external devices dim
externalDevices Set externalDevices = app.ExternalDevices
''''''''''''''''''''''''''''''''''''''''' ' Get the specific device in this
example is Device2 dim myExternalDevice Set myExternalDevice =
externalDevices.Item("Device2") ' print the selected external device type
msgbox("External Device type:"& myExternalDevice.DeviceType)
''''''''''''''''''''''''''''''''''''''''' ' Get the External device extended
propertiespecific ' dim PwrasRec Set PwrasRec
=myExternalDevice.ExtendedProperties ' ' Get the uncertainty object ' dim
PowerSensorUncertainty set PowerSensorUncertainty =
PwrasRec.PowerSensorUncertainty ' ' Get the list of all the model available
for uncertainty ' dim catalog
catalog=PowerSensorUncertainty.UncertaintyModelCatalog ' ' Print the first
element of the catalog ' msgbox("First Element of Power Meter with uncertainty
catalog: "&catalog(1)) ' ' Get the selected uncertainty model Dim pwrmodel
pwrmodel=PowerSensorUncertainty.UncertaintyModel ' print it  msgbox("Selected
Power Meter Model: "&pwrmodel) ' ' Get the custom uncertainty file  ' If the
model is not a CustomFile this will return Undefined as file name Dim
pwruncfile pwruncfile=PowerSensorUncertainty.UncertaintyFile ' print it
msgbox("Selected Power Meter Custom File: "&pwruncfile) ' ' Read the pwrmtr
uncertainty value for a specific frequency and pwrlevel ' in this example
10GHz and 0.0 dBm Dim PwrMtrReadingUncertianty
PwrMtrReadingUncertianty=PowerSensorUncertainty.PowerMtrReadingUncertainty(10e9,0.0)
msgbox("10GHz and 0.0dBm nominal value Power Meter reading uncertainty
variance: "&PwrMtrReadingUncertianty&" [W^2]") ' ' Read the power value which
offer the best accuracy for the power meter Dim PowerForBestAcc
PowerForBestAcc=PowerSensorUncertainty.PowerForBestAccuracy msgbox("Power
Meter power for best accurary: "&PowerForBestAcc&" [dBm]")  
---


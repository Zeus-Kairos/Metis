# Perform an Unguided ECal

* * *

This VBScript program performs an Unguided Full 2-Port ECal.

The SCPI commands in this example are sent over a COM interface using the
[SCPIStringParser](../COM_Reference/Objects/SCPIStringParser_Object.md)
object. You do NOT need a GPIB connection to run this example.

This VBScript (*.vbs) program can be run as a macro in the VNA. To do this,
copy the following code into a text editor file such as Notepad and save it on
the VNA hard drive as Unguided.vbs. [Learn how to setup and run the
macro.](../Using_Macros.htm)

[See Sense:Correction commands.](../GP-
IB_Command_Finder/Sense/Sense_Correction.htm)

[See other SCPI Examples](SCPI_Example_Programs.md)

Set pna = CreateObject("AgilentPNA835x.Application")  
Set scpi = pna.ScpiStringParser  
' Preset the analyzer  
scpi.Execute "SYSTem:PRESet"  
  
' Start frequency of 10 MHz  
scpi.Execute "SENSe:FREQuency:STARt 10E6"  
  
' Stop frequency of 9 GHz  
scpi.Execute "SENSe:FREQuency:STOP 9E9"  
  
' Select the preset S11 measurement  
scpi.Execute "CALCulate:PARameter:SELect 'CH1_S11_1'"  
' Read the information about the Keysight factory  
' characterization data of ECal module #1 on the USB bus  
module1Info = scpi.Execute("SENSe:CORRection:COLLect:CKIT:INFormation?
ECAL1,CHAR0")  
  
' Prompt for the ECal module  
MsgBox "Description of ECal Module #1:" & Chr(10) & Chr(10) & module1Info &
_Chr(10) & Chr(10) & "Make port connections to the ECal module, then press
enter"  
' ECal full 1 port and 2 port  
' Choose a Calibration Type (comment out one of these)  
scpi.Execute "SENSe:CORRection:COLLect:METHod refl3"  
scpi.Execute "SENSe:CORRection:COLLect:METHod SPARSOLT"  
' Specify to have the VNA automatically determine which port of the  
' ECal module is connected to which port of the VNA.  
scpi.Execute "SENSe:CORRection:PREFerence:ECAL:ORIentation ON"  
' Alternatively, if you are measuring at very low power levels where  
' the VNA fails to sense the module's orientation, you may need to turn  
' off the auto orientation and specify how the module is connected (as in  
' these next two commented lines of code -- "A1,B2" would indicate Port A  
' of the module is connected to Port 1 and Port B is connected to Port 2).  
'scpi.Execute "SENSe:CORRection:PREFerence:ECAL:ORIentation OFF"  
'scpi.Execute "SENSe:CORRection:PREFerence:ECAL:PMAP ECAL1,'A1,B2'"  
' Acquire and store the calibration terms. *OPC? causes a "+1" to be  
' returned when finished. CHAR0 indicates to use the Keysight factory  
' characterized data within the ECal module (as opposed to a user
characterization).  
x = scpi.Execute("SENSe:CORRection:COLLect:ACQuire ECAL1,CHAR0;*OPC?")  
' Note: if you have set up a slow sweep speed (for example, if  
' youre using a narrow IF bandwidth), and while this calibration is  
' being acquired you wish to have your program perform other operations  
' (like checking for the click event of a Cancel button) and youre  
' NOT using the COM ScpiStringParser, you can use the optional  
' ASYNchronous argument with the ACQuire command as shown here below  
' instead of sending that command in the way shown above. The SCPI  
' parser then will return immediately while the cal acquisition  
' proceeds (i.e., the parser will NOT block-and-wait for the  
' cal to finish, so you can send additional commands in the meantime).  
' So you can do *ESR? or *STB? queries to monitor the status register  
' bytes to see when the OPC bit gets set, which indicates the cal has  
' finished. That type of OPC detection works for all of the VNAs SCPI  
' parsers except the COM ScpiStringParser.  
' An alternative to querying the status register, is to setup an SRQ handler  
' if your IO Libraries supports that.  
' When an SRQ event occurs, a call back will automatically  
' SENSe:CORRection:COLLect:ACQuire ECAL1,CHAR0,ASYNchronous;*OPC  
MsgBox "Done with calibration."  


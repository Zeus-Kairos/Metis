[File](FileTopic.md) | [Instrument](XTraceChanTopic.md) | [Response](XResponseTopic.md) | [Stimulus](XStimulusTopic.md) | [Utility](XUtilityTopic.md) | [Cal](CalTopic.md) | [Apps](MixerTopic.md) | [Remote ONLY](DataTopic.md)

* * *

[Save /Recall](FileTopic.md#Save) | [Manage Files](FileTopic.md#files) | [Manage Folders](FileTopic.md#folders) | [Print](FileTopic.md#Print) | [Read Clock](FileTopic.md#clock)

Description |  SCPI |  COM  
---|---|---  
Save / Recall  
Save Instrument States (*.csa, *.cst, *.sta, *.cal) and type of file |  [MMEMory:STORe](GP-IB_Command_Finder/Memory.md#save) |  [app.Save](COM_Reference/Methods/Save_Method.md)  
Save Data (except snp) |  [MMEMory:STORe:DATA](GP-IB_Command_Finder/Memory.md#StoreData) |  [app.SaveData](COM_Reference/Methods/SaveData_Method.md)  
Recall Files |  [MMEMory:LOAD](GP-IB_Command_Finder/Memory.md#recall) |  [app.recall](COM_Reference/Methods/Recall_Method.md)  
Recall softkey list sort preference |  [SYSTem:PREFerences:ITEM:MRU](GP-IB_Command_Finder/System_Preferences.md#mru) |  [RecallSoftkeysMostRecent](COM_Reference/Properties/RecallSoftkeysMostRecent_Property.md)  
Reads SNP data for the specified ports |  [CALCulate:MEASure:DATA:SNP:PORTs?](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:SNP:PORTs) |  [Get SnpDataWithSpecifiedPorts](COM_Reference/Methods/Get_SnpDataWithSpecifiedPorts_Method.md)  
Saves SNP data for the specified ports |  [CALCulate:MEASure:DATA:SNP:PORTs:SAVE](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:SNP:PORTs:SAVE) |  [WriteSnpFileWithSpecifiedPorts](COM_Reference/Methods/WriteSnpFileWithSpecifiedPorts_Method.md)  
Reads SnP data from the selected measurement |  [CALCulate:MEASure:DATA:SNP?](GP-IB_Command_Finder/Calculate/MeasureDATA.md#CALCulate:MEASure:DATA:SNP:PORTs:SAVE) |  [GetSnPData](COM_Reference/Methods/GetSnpData_Method.md)  
Sets format for .SNP files |  [MMEMory:STORe:TRACe:FORMat:SNP](GP-IB_Command_Finder/Memory.md#snp) |  [pref.SnPFormat](COM_Reference/Properties/SnPFormat_Property.md)  
Set/get formatted measurement data |  [CALCulate:MEASure:DATA:FDATa](GP-IB_Command_Finder/Calculate/MeasureDATA.md#FDATA) |  [getData](COM_Reference/Methods/Get_Data_Method.md) [putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md)  
Set/get complex measurement data |  [CALCulate:MEASure:DATA:SDATa](GP-IB_Command_Finder/Calculate/MeasureDATA.md#SDATA) |  [getData](COM_Reference/Methods/Get_Data_Method.md) [putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md)  
Set/get formatted memory data |  [CALCulate:MEASure:DATA:FMEMory](GP-IB_Command_Finder/Calculate/MeasureDATA.md#FMEM) |  [getData](COM_Reference/Methods/Get_Data_Method.md) [putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md)  
Set/get complex memory data |  [CALCulate:MEASure:DATA:SMEMory](GP-IB_Command_Finder/Calculate/MeasureDATA.md#SMEM) |  [getData](COM_Reference/Methods/Get_Data_Method.md) [putDataComplex](COM_Reference/Methods/Put_Data_Complex_Method.md)  
Manage Files  
List Files |  [MMEMory:CATalog](GP-IB_Command_Finder/Memory.md#cat) |  None  
Copy Files |  [MMEMory:COPY](GP-IB_Command_Finder/Memory.md#copy) |  None  
Move Files |  [MMEMory:MOVE](GP-IB_Command_Finder/Memory.md#move) |  None  
Delete Files |  [MMEMory:DELete](GP-IB_Command_Finder/Memory.md#del) |  None  
Manage Folders  
Change |  [MMEMory:CDIRectory](GP-IB_Command_Finder/Memory.md#chgdir) |  None  
Delete |  [MMEMory:RDIRectory](GP-IB_Command_Finder/Memory.md#remvedir) |  None  
Make |  [MMEMory:MDIRectory](GP-IB_Command_Finder/Memory.md#mkdir) |  None  
Read directory location for the specified file type |  [SYSTem:CONFigure:DIRectory?](GP-IB_Command_Finder/System.md#ConfDir) |  [DirectoryPath](COM_Reference/Properties/DirectoryPath_Property.md)  
Print  
Print |  [HCOPy](GP-IB_Command_Finder/Hardcopy.md) |  [app.DoPrint](COM_Reference/Methods/Do_Print_Method.md)  
Saves image of VNA screen to file. (Print to File) |  [HCOPy:FILE](GP-IB_Command_Finder/Hardcopy.md#file) |  [app.PrintToFile](COM_Reference/Methods/PrintToFile_Method.md)  
Return the display image in arbitrary binary block |  [HCOPy:SDUMp:DATA?](GP-IB_Command_Finder/Hardcopy.md#sdump) |  None  
Set format of display image |  [HCOPy:SDUMp:DATA:FORM](GP-IB_Command_Finder/Hardcopy.md#SdumpFormat) |  None  
  
Read Date and Time |  SCPI |  COM  
---|---|---  
Read the last modified date of a Cal Set |  [CSET DATE?](GP-IB_Command_Finder/CSET.md#Date) |  [LastModified](COM_Reference/Properties/LastModified_Property.md)  
Read the last modified time of a Cal Set |  [CSET:TIME?](GP-IB_Command_Finder/CSET.md#time) |  [LastModified](COM_Reference/Properties/LastModified_Property.md)  
Read the last modified date of a file |  [MMEM:DATE?](GP-IB_Command_Finder/Memory.md#Date) |  None  
Read the last modified time of a file |  [MMEM:TIME?](GP-IB_Command_Finder/Memory.md#Date) |  None  
  
* * *


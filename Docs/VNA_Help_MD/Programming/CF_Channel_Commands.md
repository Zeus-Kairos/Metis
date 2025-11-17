# Channel Commands

Channel  
1-8 | Channel  
Setup  
---|---  
Channel 1 - 8 Tab Commands  
---  
Softkey | Sub-item | SCPI | COM  
Channel 1 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 2 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 3 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 4 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 5 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 6 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 7 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel 8 | On/Off | None | [Add](COM_Reference/Methods/Add_channels_Method.md)  
Channel Setup Tab Commands  
Softkey | Sub-item | SCPI | COM  
Select | ChN | [SENSe:CLASs:NAME?](GP-IB_Command_Finder/Sense/Class.md#name) | [ActiveChannel](COM_Reference/Properties/Active_Channel_Property.md)  
Meas Class... |  | [CALCulate:MEASure:DEFine](GP-IB_Command_Finder/Calculate/Measure.md#CALCulate:MEASure:DEFine) | [CreateCustomMeasurementEx](COM_Reference/Methods/CreateCustomMeasurementEx_Method.md)  
Add Channel | New Trace + Channel | [DISP:CHANnel:NEW](GP-IB_Command_Finder/Display.md#ChanNew) | None  
New Trace + Channel + Window | [DISP:CHANnel:NEW](GP-IB_Command_Finder/Display.md#ChanNew) | None  
Copy Channel | Copy to Active Window | None | None  
Copy to New Window | None | None  
Copy Channel... | [SYSTem:MACRo:COPY:CHANnel[:TO]](GP-IB_Command_Finder/System.md#COPY_CHANnel) | [CopyToChannel](COM_Reference/Methods/CopyToChannel_Method.md)  
Delete Channel | ChN | [SYSTem:CHANnels:DELete](GP-IB_Command_Finder/System.md#ChanDelete) or  [DISP:CHANnel:STATe](GP-IB_Command_Finder/Display.md#ChanStat) | [RemoveChannelNumber](COM_Reference/Methods/RemoveChannelNumber_Method.md)


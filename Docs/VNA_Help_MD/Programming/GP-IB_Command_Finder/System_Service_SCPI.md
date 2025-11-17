# SYSTem:SERVice Commands

* * *

Controls and queries for programmatically interacting with the PathWave
Calibration Advisor software application.

SYSTem:SERVice: MANagement | CALibration | INFormation? | INTerval | DEFault | TYPE? | [:VALue] | NOTification | ENABle | PASScode | CHANge | [:VALue] | PERiodic | ENABle | REMinder  
---  
  
Click on a red keyword to view the command details.

See Also

  * [SCPI Command Tree](SCPI_Command_Tree.md)

* * *

## SYSTem:SERVice:MANagement:CALibration:INFormation?

Applicable Models: All (Read only) Returns the instrument calibration
information in JSON format. The returned value includes the following:

  * CalID  Calibration ID number created by the service center when the instrument was calibrated.
  * CalBy  Service center that calibrated this instrument  either "Keysight Technologies" or "Keysight Authorized Calibration Provider".
  * CalDate  Date of last calibration.
  * CalDueDate  Calibration due date. The due date is calculated as CalDate \+ Calibration Interval, unless a _shelf life policy_ is applied.
  * Status  returned value depends on: 
    * If SystemTime≤CalDueDate, Status is "CalibrationValid".
    * If SystemTime>CalDueDate, Status is "CalibrationRequired".
    * If CalDueDate is empty, and CalDate is presented, Status is "CalibrationValid".
    * If SystemTime<CalDate, Status is "CalibrationUnknown".
    * If Cal Data is unavailable, Status is "CalibrationNotFound".
  * SystemTime  Current system time.

  
---  
Parameters | None  
Examples | SYSTem:SERVice:MANagement:CALibration:INFormation? 'returns this format: {"CalId":"1-00000000000-1","CalBy":"Keysight Technologies","CalDate":"27-May-2020","CalDueDate":"27-May-2021","Status":"CalibrationValid","SystemTime":"2020-11-18 10:38:08"}  
Return Type | String of JSON format including all calibration info   
Default | Not Applicable  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:INTerval:DEFault

Applicable Models: All (Write-only) Sets calibration interval to Keysight
Recommended (according to the instrument model).  
---  
Parameters | None  
Examples | SYST:SERV:MAN:CAL:INT:DEF  
Query Syntax | Not Applicable  
Default | Not Applicable  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:INTerval:TYPE?

Applicable Models: All (Read only) Returns the instrument calibration interval
type. Three types may return:

  * DEFault: When current calibration interval is "Keysight recommended", the returned value is DEFault.
  * CUSTomer: When the current calibration interval is "user defined", the returned value is CUSTomer.
  * EMPTY: After new calibration info is imported and the calibration interval is not confirmed, the returned value is empty.

  
---  
Parameters | None  
Examples | SYSTem:SERVice:MANagement:CALibration:INTerval:TYPE? CUSTomer  
Return Type | Enum  
Default | Not Applicable  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:INTerval[:VALue] <value>

Applicable Models: All (Read-Write) Sets and returns the calibration interval
value (interval in months). Notes:

  * If using this command to set to the calibration interval, the calibration interval type will be switched to user defined (CUSTomer).
  * This command only returns the value of current saved calibration interval type. Any unsaved changes will not be returned.

  
---  
Parameters |   
<value> | Calibration interval in months. An integer between 1 and 120.   
Examples | SYSTem:SERVice:MANagement:CALibration:INTerval:VALue 12  
Query Syntax | SYSTem:SERVice:MANagement:CALibration:INTerval[:VALue]?  
Return Type | Numeric  
Default | Not Applicable  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:NOTification:ENABle <bool>

Applicable Models: All (Read-Write) Sets and returns the calibration
status/due popup notification state during instrument running. If disabled,
the notification will pop up only on power up. If enabled, the notification
will also pop up at 12:00 AM every day when the current date is ≤ the Cal Due
Reminder days set by SYSTem:SERVice:MANagement:CALibration:REMinder.  
---  
Parameters |   
<bool> | **OFF** (or **0**): Popup notification is NOT visible while the instrument is running.  
**ON** (or **1**): Popup notification is visible while the instrument is
running.  
Examples | SYSTem:SERVice:MANagement:CALibration:NOTification:ENABle 0  
SYSTem:SERVice:MANagement:CALibration:NOTification:ENABle OFF  
Query Syntax | SYSTem:SERVice:MANagement:CALibration:NOTification:ENABle?  
Return Type | Boolean  
Default | 1  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:PASScode:CHANge <value>

Applicable Models: All (Write-only) Sets new passcode.  
---  
Parameters |   
<value> | Passcode.  
Requirements: 6-10 characters, limited to alpha (a-Z) and numeric (0-9)
characters.  
Examples | SYSTem:SERVice:MANagement:CALibration:PASScode:CHANge '1q2w3e4r'  
Query Syntax | Not Applicable  
Default | Not Applicable  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:PASScode[:VALue] <value>

Applicable Models: All (Write-only) Input existing passcode and enable all
setting features.  
---  
Parameters |   
<value> | Last saved passcode (see SYSTem:SERVice:MANagement:CALibration:PASScode:CHANge)   
Examples | SYSTem:SERVice:MANagement:CALibration:PASScode '1q2w3e4r'  
Query Syntax | Not Applicable  
Default | Key4Cal  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:PERiodic:ENABle <bool>

Applicable Models: All (Read-Write) Sets and returns the periodic calibration
state.  
---  
Parameters |   
<bool> | **OFF** (or **0**): Periodic calibration is disabled.   
**ON** (or **1**): Periodic calibration is enabled.  
Examples | SYSTem:SERVice:MANagement:CALibration:PERiodic:ENABle 0  
SYSTem:SERVice:MANagement:CALibration:PERiodic:ENABle OFF  
Query Syntax | SYSTem:SERVice:MANagement:CALibration:PERiodic:ENABle?  
Return Type | Boolean  
Default | 1  
  
* * *

## SYSTem:SERVice:MANagement:CALibration:REMinder <value>

Applicable Models: All (Read-Write) Sets and returns the calibration due
reminder days (30, 15, or 7).  
---  
Parameters |   
<value> | Calibration due reminder in days. Only one number: 30, 15, or 7.   
Examples | SYSTem:SERVice:MANagement:CALibration:REMinder 30  
Query Syntax | SYSTem:SERVice:MANagement:CALibration:REMinder?  
Return Type | Numeric  
Default | 30  
  
* * *


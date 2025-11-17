# Creating a New Connector Family

* * *

To create a custom calibration kit that uses a new connector type, you must
first define the connector family. The connector family is the name of the
connector-type of the calibration kit, such as:

  * 7 mm

  * 2.4 mm

  * Type-N (50)

Although more than one connector family is allowed, it is best to limit each
calibration kit to only one connector family. One exception to this is if
specific thrus are required on a per-port-pair basis (see the following note).

Note: One way to accomplish assigning specific thrus to specific port pairs is
to define connectors on a per-port basis. For example, if it is desired for
THRU1 to be used between Ports 1 and 2, and THRU2 to be used, then you can set
up connectors, 2.4mm Port1, 2.4mm Port2, 2.4mm Port3. And then in the
standards definition, create THRU1 standard with connectors 2.4mm Port1 and
2.4mm Port2 and THRU2 standard with 2.4mm Port2 and 2.4mm Port3.

If you are using a connector family that has male and female connectors,
include definitions of both genders. If you are using a family with no gender,
only one connector definition is required.

Use the following steps to create a custom calibration kit:

  1. Press Cal > Cal Sets & Cal Kits > Cal Kit....

  2. Click Edit....

  3. In the [Connectors Tab](connectors_tab.md), click Add to name the new connector family.

  4. Enter the Kit Description for the custom cal kit.

  5. Click Add in the Connectors section of the dialog box.

  6. Enter a Connector Family name.

  7. Enter a Description of the connector. 

  8. Select the Gender of one of the connectors. 

  9. Enter the minimum and maximum Frequency Range.

  10. Enter the Impedance.

  11. Click the down-arrow to select the Media.

  12. Enter the cut-off frequency

  13. Click Apply. 

  14. Click OK.

  15. If you need to add another connector gender, in the [Connectors Tab](Connectors_Tab.md), click Add in the Connectors section again for the next connector gender. 

  16. If you are adding another connector gender, repeat step 3.

Note: If you have male and female versions of the connector family, you
probably do NOT also have a NO GENDER version.

### Enter Standards

Now that the connector family is added to the custom cal kit, you are ready to
add new calibration standards.

  1. In the [Standards Tab](Standards_Tab.md), under the list of standards, click Add.

  2. Select the type of standard (OPEN, SHORT, LOAD, or THRU), then click OK. 

  3. Complete the information in the dialog box for the standard you selected. Note that for banded standards, the start and stop frequency may be different than the frequency range of the specified connector. Edit the start and stop frequencies as needed. Click OK when all the settings are correct.

  4. Repeat steps 2 - 3, as necessary, to add all standards and definitions to the new custom cal kit.

  5. Assign each of the standards to a calibration class. This is done through the [TRL Tab](TRL_Tab.md) or [SOLT Tab](SOLT_Tab.md)

  6. Save the Cal Kit.

* * *


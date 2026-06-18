# Lab 2: UML Use Case Diagrams

## Course Context
This directory contains the use case modeling deliverables for the Software Engineering course at the Lodz University of Technology (IFE), taught by dr. inż. Abdulla Juwaied. The implementation follows the specific guidelines set out in Lab_2_UML_UseCase.pdf.

## Objective
The objective of this laboratory was to analyze functional requirements and establish system boundaries by mapping user interactions with a software system. This involved defining primary and secondary actors, identifying core use cases, and establishing relationship dependencies using standard UML notation.

## System Implementation: Medical Clinic System
For this assignment, the Medical Clinic System was selected and modeled. The system coordinates administrative tasks, client services, and external financial processing.

### Actors
- Patient: A primary actor who interacts with the clinic services to view records and manage scheduling.
- Receptionist: A primary actor responsible for managing appointments and initiating front-desk workflows.
- Insurance and Billing System: A secondary external system actor that handles financial and coverage workflows.

### Core Use Cases and Relationships
The diagram implements five interconnected use cases that capture the essential behavior of the clinic application:
- View Medical Records: Allows patients or staff to access historical medical history securely.
- Book Appointment: The central scheduling feature. This use case includes a mandatory check to ensure system consistency.
- Check Doctor Availability: A sub-process automatically triggered by the system during scheduling via an include relationship.
- Process Payment: Handles financial transactions and communicates directly with the external Insurance and Billing System.
- Apply Discount Coupon: An optional use case that extends the payment flow under specific structural conditions using an extend relationship.

## Design Standards Followed
The model establishes a clear system boundary box labeled for the Medical Clinic System, keeping external actors separated from internal functions. The use of include ensures that doctor availability is verified before any appointment is finalized, while the extend relationship handles the optional promotional coupon flow without cluttering the baseline transaction logic.

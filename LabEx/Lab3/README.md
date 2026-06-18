# Lab 3: UML Class Diagrams

## Course Context
This repository contains the structural design documentation for Lab 3 of the Software Engineering course at the Lodz University of Technology (IFE), conducted by dr. inż. Abdulla Juwaied. The design paradigms, member variables, and object-oriented relationships match the requirements set forward in Lab_3_UML_Class.pdf.

## Objective
The focus of this lab was to transition from the functional perspective of use cases to a static structural architecture using UML Class diagrams. This involved defining core classes, organizing attributes and operations, establishing data types, and mapping object-oriented relationships.

## Structural Architecture
Following the guidelines in Lab_3_UML_Class.pdf, the systems are broken down into precise, multi-class structures containing at least 5 interconnected classes per system.

1. ATM System Structure
   - Core Classes: ATM, CardReader, Keypad, CashDispenser, BankAccount, Transaction.
   - Design Focus: Secure hardware encapsulation and account balance state updates.

2. Medical Clinic System Structure
   - Core Classes: Person, Patient, Doctor, Appointment, MedicalRecord, Bill.
   - Design Focus: Setting up clean inheritance hierarchies for roles and handling relational data for appointments.

3. Car Insurance System Structure
   - Core Classes: Customer, InsurancePolicy, Vehicle, Claim, PolicyProvider.
   - Design Focus: Structuring policy terms, vehicle profiles, and tracking claims processing attributes.

## Object-Oriented Principles Applied
- Access Modifiers: Visibility is strictly defined using standard notation: (+) Public for interfaces, (-) Private for internal data encapsulation, and (#) Protected for inheritance structures.
- Relationships:
  - Inheritance is used to abstract general entity behavior.
  - Composition is applied where child component lifecycles depend directly on the parent container (such as an ATM owning its component hardware readers).
  - Aggregation is utilized for looser configurations where independent objects are pooled together.

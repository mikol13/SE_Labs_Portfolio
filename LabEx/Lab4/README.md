# Lab 4: UML Behavioral Diagrams

## Course Context
This repository contains the dynamic system designs created for Lab 4 of the Software Engineering course at the Lodz University of Technology (IFE), under the instruction of dr. inż. Abdulla Juwaied. The behavioral models and workflows comply with the lab criteria specified in Lab_4_UML_Class-2.pdf.

## Objective
The purpose of this lab was to model the dynamic, time-dependent, and conditional aspects of software systems. By moving beyond static classes, this work visualizes how objects collaborate over time, how systems shift between operational states, and how data flows through complex business processes.

## Behavioral Perspective Breakdown
As requested in Lab_4_UML_Class-2.pdf, three different UML behavioral diagrams were implemented to capture distinct execution characteristics across the target systems:

1. ATM System - Sequence Diagram
   - Focus: Maps the chronological timeline of a cash withdrawal transaction.
   - Logic: Illustrates message exchanges between the Customer, ATM Interface, Card Reader, and Bank Server. It heavily features alternative (alt) blocks to handle operational branching, such as successful processing versus insufficient funds or incorrect PIN entries.

2. Medical Clinic System - State Diagram
   - Focus: Tracks the complete lifecycle changes of a core system entity or operational state machine.
   - Logic: Documents transitions between operational baselines like Idle, Processing, Maintenance, and Out of Service, noting the specific triggers, guards, and action parameters that cause state changes.

3. Car Insurance System - Activity Diagram
   - Focus: Models the procedural workflow of submitting and processing an insurance claim from start to finish.
   - Logic: Uses decision nodes to manage validation paths, alongside concurrent fork and join synchronization bars to model parallel office operations (such as simultaneously assessing vehicle damage and reviewing policy terms).

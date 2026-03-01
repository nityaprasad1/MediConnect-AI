# MediConnect AI – LLM Powered Smart Pharmacy Assistant

## Overview

MediConnect AI is an AI for Social Good project that provides safe preliminary medical guidance for minor health issues and connects users with nearby pharmacies and clinics.
The system uses a Large Language Model with safety guardrails to ensure users only receive over-the-counter advice and are redirected to healthcare professionals when required.

## Problem

People frequently self-medicate using unreliable internet sources or visit hospitals for minor issues.
This wastes medical resources and may cause unsafe drug usage.
There is no intelligent assistant that safely bridges users and local pharmacies.

## Solution

MediConnect AI acts as a virtual pharmacist assistant.

The chatbot:

* Understands symptoms in natural language
* Suggests only OTC medicines and home remedies
* Detects emergency symptoms
* Blocks prescription drug recommendations
* Shows nearby pharmacies and clinics
* Supports multilingual conversations

## Features

* Symptom based guidance
* Emergency detection and escalation
* Ethical AI safety guardrails
* Nearby pharmacy discovery
* Multilingual support
* Pharmacist contact information

## Safety Policy

The system never diagnoses diseases and never prescribes restricted medication.
Severe symptoms automatically trigger medical escalation.

## Tech Stack

Python
Flask
LLM API
JSON database
Geolocation distance calculation

## How to Run

pip install -r requirements.txt
python app.py

Open browser: http://127.0.0.1:5000

## Project Structure

MediConnect-AI/
app.py
safety.py
triage.py
prompts.py
pharmacy_db.json
templates/index.html
requirements.txt

## Example Use

User: I have throat pain
Bot: Suggests lozenges and home care

User: I want antibiotics
Bot: Advises doctor consultation

User: chest pain and breathlessness
Bot: Immediate hospital recommendation

## Disclaimer

This software is an informational support tool and does not replace professional medical advice.

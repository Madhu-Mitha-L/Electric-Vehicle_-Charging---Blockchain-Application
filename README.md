# ⚡ Blockchain EV Charging & Billing System  

**A simple Python-based Blockchain EV Charging & Billing System that ensures secure, transparent, and tamper-proof energy transactions using blockchain technology.**

---

## 📌 Table of Contents  
- [Overview](#-overview)  
- [Problem Statement](#-problem-statement)  
- [Features](#-features)  
- [How it Works](#-how-it-works)    
- [Tech Stack](#-tech-stack)  
- [Future Improvements](#-future-improvements)  
- [File Structure](#-file-structure)  
- [Run the Script](#-run-the-script)  

---

## 📌 Overview  
This project is a **Blockchain-based Electric Vehicle Charging & Billing System** built using Python.  

It demonstrates how blockchain can be applied in **energy and charging infrastructures** to ensure:  
- 🔎 Transparency  
- 🔒 Security  
- ⛓️ Immutability (transactions cannot be changed once recorded)  
- ⚡ Fair billing for users and stations  

The system allows users to **recharge wallets, charge vehicles at stations, and store all billing sessions securely on the blockchain.**

---

## ❓ Problem Statement  
Traditional EV charging and billing systems face several challenges such as:  

- 🕵️ Lack of transparency in billing  
- ✏️ Possibility of fraud or incorrect meter readings  
- 🔁 Duplicate or fake transactions  
- 🐌 Delayed settlements between station owners and users  

👉 To solve these issues, we need a **secure, transparent, and tamper-proof billing mechanism**.  
Blockchain provides this by recording every charging session in an **immutable distributed ledger**.  

---

## 🚀 Features  

### 🔹 User Functionalities  
- 👤 **User Registration** – Only registered users can access charging services.  
- 💰 **Wallet Recharge** – Users can recharge their wallet with money (₹).  
- ⚡ **Charging Sessions** – Users charge vehicles at stations (units × cost).  
- 📊 **Transaction History** – Track all sessions with unique IDs.  
- ⚠️ **Low Balance Alerts** – Warns users when their wallet balance is low.  

### 🔹 Station / System Functionalities  
- 🏭 **Station Registration** – Only registered stations can provide charging services.  
- ⛓️ **Blockchain Ledger** – All sessions are recorded permanently on blockchain.  
- 🛡️ **Fraud Prevention** – Invalid users or stations are denied access.  
- ✅ **Blockchain Validation** – Ensures transactions are tamper-proof.  

---

## 🔎 How it Works  

### 1️⃣ Wallet & Registration  
- Users register and get a wallet balance.  
- Stations register with a set charging rate.  

### 2️⃣ Charging Session  
- User selects a station and requests units.  
- System calculates **cost = units × rate**.  
- Wallet balance is checked → if enough, charging succeeds.  
- Balance updates for both user and station.  

### 3️⃣ Blockchain Transaction  
- Each session is stored as a **transaction**.  
- Transactions are grouped into **blocks**.  
- Proof-of-Work secures the block.  
- Blocks link to form an **immutable ledger**.  

### 4️⃣ Transparency & Billing  
- Once recorded, charging data cannot be altered.  
- Blockchain ensures **trust** between users and stations.  

---

## 💻 Tech Stack  

- **Language**: Python 🐍  
- **Core Concept**: Blockchain (custom implementation)  
- **Libraries**:  
  - `hashlib` → hashing blocks  
  - `json` → transaction storage  
  - `time` → timestamps  
  - `uuid` → unique session IDs  

---

## 🔮 Future Improvements  

- Add a web-based UI (Flask/Streamlit) for easier interaction.  
- Integrate with real EV station APIs for live data.  
- Implement smart contracts using Ethereum or Hyperledger.  
- Add transaction validation with consensus mechanisms.  
- Enable payment gateway support (UPI, PayPal, crypto).  
- Store data in a persistent database (PostgreSQL/MongoDB).  
- Add role-based access (user vs station owner vs admin).  
- Improve security features like digital signatures for transactions.  

---

## 📂 File Structure  

EV-Charging-Blockchain/
│
├── ev_charging_blockchain.py # Main application script
├── README.md # Project documentation
├── Output/ # Images of the output


---

## Run the Script  
To run the blockchain-based EV charging system:  

```bash
python ev_charging_blockchain.py

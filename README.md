# Blood Bank Management System

A Python and MySQL-based management system designed to streamline donor registration, track donation history, and automate eligibility checks via a menu-driven interface.


---

## 🚀 Key Features
* **Donor Management:** Full CRUD operations (Add, Modify, Remove) for donor profiles using unique IDs.
* **Smart Search:** Quickly filter and locate donors by blood group.
* **Eligibility Logic:** Automated checks to ensure a minimum **90-day interval** between donations.
* **Donation Tracking:** Maintains a chronological history (`HIST` table) for every registered donor.
* **User-Friendly CLI:** Intuitive menu-driven interface for ease of use.

---

## 🛠️ Technical Setup

### Prerequisites
Before running the application, ensure you have the following installed:
* **Python 3.x**
* **MySQL Server**
* **MySQL Connector for Python**: Install it via terminal/command prompt:
  ```bash
  pip install mysql-connector-python

### CREATING DATABASE IN SQL
-- 1. Create the Database:
```bash
CREATE DATABASE IF NOT EXISTS bloodbank;
USE bloodbank;
```

-- 2. Create Donor Details Table:
```bash
CREATE TABLE IF NOT EXISTS DETAILS (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    dob DATE,
    aadhaarno VARCHAR(12),
    bg VARCHAR(3),
    lastdon DATE,
    HN_city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100),
    mobno VARCHAR(50),
    email VARCHAR(100),
    TEMPDATE DATE
);
```
-- 3. Create Donation History Table
CREATE TABLE IF NOT EXISTS HIST (
    id INT, 
    DonHist DATE,
    FOREIGN KEY (id) REFERENCES DETAILS(id) ON DELETE CASCADE
);

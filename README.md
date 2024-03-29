# EnergyInsight 💡

## Project Overview

EnergyInsight is a Python console-based application designed to provide comprehensive analysis and insights into global energy consumption, production trends, and environmental impacts. The project utilizes SQL as the primary tool for data storage and analysis, with Python, BigQuery, and GCP forming the tech stack.

### Functionalities and Constraints

#### Data Management 📊

- **Data Import:**
  - Ability to import multiple datasets into the SQLite database, containing ISO code, country, year, and energy-related information.

- **Data Integrity:**
  - Ensure data integrity and validation during the import process to avoid inconsistencies.

- **Data Update:**
  - Provide functionality to update existing dataset records or append new data to existing records.

#### Analysis and Insights 📈

- **SQL-Based Analysis:**
  - Perform SQL queries for various analytical tasks like trend analysis, growth rates calculation, and correlation analysis between different energy sources.

- **Trend Identification:**
  - Identify trends in energy consumption and production over different periods and across various countries.

- **Environmental Impact Assessment:**
  - Analyze the environmental impact by identifying countries with significant changes in energy production (e.g., coal production increase).

#### Visualization  📊

- **Data Visualization (Optional):**
  -1.	Visualize the chart that illustrates the contribution of gas, oil, and other energy sources to the total energy produced for select countries, enabling a clear understanding of energy source distribution

#### CRUD Operations 🔄

- **Create, Read, Update, Delete Operations:**
  - Enable importing new datasets, adding new records, retrieving information based on SQL queries, modifying existing data records, and allowing removal of unnecessary datasets or data records.

#### Scalability and Performance ⚙️

- **Performance Optimization:**
  - Optimize SQL queries and database operations for improved application performance, especially with large datasets.

- **Scalability Consideration:**
  - Design the application architecture considering future scalability and potential integration of additional datasets or functionalities.

## User Stories

### User Stories:

1. **User Registration:**
   - As a new user, I want to register in the Energy Insight system.
     - Provide a unique username, a secure password, email, and country during the registration process.
     - Details stored in `users`.

2. **User Login:**
   - As a registered user, I want to log into the Energy Insight system.
     - Prompted to enter username and password.
     - Access to the user menu with various options upon successful login.

3. **View the Energy Data Summary:**
   - As a user, I want to view a summary of my energy consumption and production data.
     - Summary includes ISO Code, Year, Coal Consumption, Coal Production, Oil Production, Oil Consumption, Gas Production, and Gas Consumption.

4. **Update Profile Information:**
   - As a user, I want the ability to update my profile information.
     - Modify password or contact details as needed for accuracy.

5. **Compare Energy Data:**
   - As a user, I want to compare my energy consumption and production data with global averages or those of other users.
     - Utilizing keys such as ISO Code and User ID for accurate analysis.

6. **Search Energy Data:**
   - As a user, I want to search for specific information within my dataset.
     - Use keys such as ISO code, year, or other relevant criteria for quick data retrieval.

7. **Access Energy Insights:**
   - As a user, I want to access insights on coal, oil, and gas consumption and production trends based on my energy data.
     - Utilizing keys such as ISO Code and User ID for accurate environmental impact analysis.

### Admin Stories:

1. **Admin Login:**
   - As an admin, I want to log into the Energy Insight system.
     - Prompted to enter admin ID and password.
     - Access to the admin menu with various options upon successful login.

2. **View the User Management Overview:**
   - As an admin, I want to view a comprehensive list of all registered users.
     - List includes details such as user IDs, usernames, contact details, and user roles (admin or user).

3. **Add a New User:**
   - As an admin, I want the capability to add new users to the system.
     - Assign a unique user ID and provide essential details, including username, password, contact details, and user roles.

4. **Update User Details:**
   - As an admin, I want the ability to update existing user details.
     - Modifications allowed for usernames, passwords, contact details, and user roles.

5. **Remove User:**
   - As an admin, I want the authority to remove users from the system.
     - Ensure proper management of user accounts and associated data.

6. **Access User Data:**
   - As an admin, I want to access detailed information about any user, excluding their password.
     - Retrieve information using the user ID as the primary key.

7. **Perform Energy Data Management:**
   - As an admin, I want to perform Create, Read, Update, and Delete (CRED) operations on energy data for any user.
     - User ID utilized as a foreign key in the Energy Data table, linking data to the respective user.

8. **Access Global Energy Insights:**
   - As an admin, I want to access insights on global trends in coal, oil, and gas consumption and production.
     - Utilizing keys such as ISO Code and User ID for accurate analysis and decision-making.

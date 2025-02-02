# QR Code-Based Smart Office Seat Allocation System

## Overview
This project is designed to create an efficient seat allocation system for office spaces, aimed at optimizing space utilization and minimizing operational costs. The system leverages QR codes for booking, confirmation, and live tracking of seat occupancy, integrating seat booking, real-time tracking, and electricity/cold water consumption management.

## Features
- **Employee Login**: Secure login using employee ID and password.
- **Seat Booking**: Allows employees to select available seats, book for a specific time duration, and receive a QR code or OTP for confirmation.
- **Live Seat Tracking**: Real-time tracking of seat availability, updated when employees scan their QR codes.
- **Power and Water Usage Tracking**: Calculates energy and water consumption based on seat usage, helping monitor and reduce costs.
- **Admin Dashboard**: HR or managers can track seat usage, and energy consumption, and view reports.

## Tech Stack
- **Frontend**: HTML, CSS, JavaScript, React.js
- **Backend**: Python (Flask/Django)
- **Database**: PostgreSQL / MySQL
- **QR Code Generation**: qrcode Python library
- **Real-time Updates**: WebSockets or Firebase
- **Authentication**: OAuth 2.0 for secure login

## Installation
To run the system locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/QR-Code-Seat-Allocation.git
   ```

2. **Install Dependencies**:
   Navigate to the project folder and install required dependencies:
   ```bash
   cd QR-Code-Seat-Allocation
   pip install -r requirements.txt
   ```

3. **Run the Backend Server**:
   For Flask:
   ```bash
   flask run
   ```
   Or for Django:
   ```bash
   python manage.py runserver
   ```

4. **Frontend Setup**:
   Navigate to the frontend folder and run:
   ```bash
   npm install
   npm start
   ```

5. **Database Setup**:
   - Configure the database in `settings.py` (for Django) or in the Flask app configuration.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

6. **Access the Application**:
   Visit `http://localhost:8000` or `http://localhost:3000` to view the web interface.

## Usage
- **Employee**:
  - Log in using the employee ID and password.
  - Choose an office location and select an available seat.
  - Select the booking duration and confirm.
  - Upon arrival at the office, scan the QR code to confirm occupancy.
  - On leaving, scan the QR code again to mark the seat as available.

- **Admin**:
  - View the dashboard to see the seat usage and power/water consumption reports.
  - Manage seat availability and occupancy statuses.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Flask/Django - For building the backend.
- React.js - For creating the frontend.
- qrcode Python library - For generating QR codes.
- PostgreSQL/MySQL - For managing the database.


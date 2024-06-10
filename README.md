Here's a README file for your GPS subsystem simulation project:

---

# Simulated GPS Subsystem

## Overview

This project simulates a GPS subsystem using Python. The simulated GPS subsystem stores states and data typically held by a GPS and communicates over a TCP socket. The main features of this subsystem include:

- Storing and sending UTC time.
- Sending latitude and longitude data.
- Returning the state (on/off) of the GPS.
- Sending an ACK (acknowledgment) when pinged.

## Features

1. **Get Stored UTC Time**
   - The subsystem can store and send the current UTC time upon request.
   
2. **Send Latitude and Longitude Data**
   - The subsystem can store and send latitude and longitude data upon request.
   
3. **Return State (On/Off)**
   - The subsystem can report its current state (on/off) upon request.
   
4. **Send ACK When Pinged**
   - The subsystem can send an acknowledgment (ACK) when it receives a ping.

## Data Simulation

For simplicity, all data (UTC time, latitude, longitude) is randomly generated using sensible formats:
- **UTC Time:** `YYYY-MM-DD HH:MM:SS`
- **Latitude:** `DD.DDDD° N/S`
- **Longitude:** `DDD.DDDD° E/W`

## Installation

1. Ensure you have Python installed (Python 3.6 or higher recommended).
2. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/simulated-gps-subsystem.git
    ```
3. Navigate to the project directory:
    ```sh
    cd simulated-gps-subsystem
    ```

## Usage

1. Run the GPS subsystem:
    ```sh
    python gps_subsystem.py
    ```
2. The subsystem will start listening for TCP socket connections.

## Commands

The subsystem responds to the following commands over TCP:

- **Get UTC Time**
    ```sh
    GET_UTC_TIME
    ```
  - Response: Current stored UTC time.

- **Get Latitude and Longitude**
    ```sh
    GET_LAT_LONG
    ```
  - Response: Current stored latitude and longitude.

- **Get State**
    ```sh
    GET_STATE
    ```
  - Response: Current state of the GPS subsystem (ON/OFF).

- **Ping**
    ```sh
    PING
    ```
  - Response: `ACK`

## Example

You can use a TCP client to send commands to the subsystem. Here is an example using `telnet`:

1. Open a terminal and run:
    ```sh
    telnet localhost 12345
    ```
2. Send commands like `GET_UTC_TIME`, `GET_LAT_LONG`, `GET_STATE`, or `PING` to interact with the subsystem.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

For any questions or suggestions, please contact [yourname@example.com].

---

This README provides a comprehensive guide to understanding, installing, and using the simulated GPS subsystem. Adjust the contact information and repository URL as per your requirements.

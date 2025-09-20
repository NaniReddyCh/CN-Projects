# Stop-and-Wait Protocol

## Introduction

This folder contains the implementation of the Stop-and-Wait protocol using Python. It demonstrates basic UDP communication, handling retransmissions, and calculating throughput.

## Requirements

- Python 3.x
- Required libraries: `socket`, `struct`, `os`, `time`

## How to Run the Program

1. **Clone or Download the Repository**:

   - Clone the repository or download it as a ZIP file and extract it.

2. **Navigate to the Stop-and-Wait Folder**:

   - Open your terminal or command prompt.
   - Change the directory to the `stopandwait` folder:
     ```bash
     cd stopandwait
     ```

3. **Prepare the File to Send**:

   - Place the file you want to send (e.g., `testFile.jpg`) in the same folder.

4. **Run the Sender**:

   - Execute the sender program by running all the commands as in given sheet:
     ```bash
     python ES22BTECH11006_senderStopWait.py
     ```
   - Follow the prompts to input the retransmission timeout in milliseconds.

5. **Run the Receiver**:
   ```bash
   python ES22BTECH11006_receiverStopWait.py
   ```
   - Ensure the receiver is running before starting the sender.

## Notes

- The sender will send packets to the receiver and manage retransmissions based on the specified timeout.
- Ensure your firewall settings allow UDP traffic on the specified ports.

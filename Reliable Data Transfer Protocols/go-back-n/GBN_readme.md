# Go-Back-N Protocol

## Introduction

This folder contains the implementation of the Go-Back-N protocol using Python. It enables efficient data transfer over UDP with support for sliding window techniques.

## Requirements

- Python 3.x
- Required libraries: `socket`, `struct`, `os`, `time`

## How to Run the Program

1. **Clone or Download the Repository**:

   - Clone the repository or download it as a ZIP file and extract it.

2. **Navigate to the Go-Back-N Folder**:

   - Open your terminal or command prompt.
   - Change the directory to the `go-back-n` folder:
     ```bash
     cd go-back-n
     ```

3. **Prepare the File to Send**:

   - Place the file you want to send (e.g., `testFile.jpg`) in the same folder.

4. **Run the Sender**:

   - Execute the sender program by running:
     ```bash
     python ES22BTECH11006_senderGBN.py
     ```
   - Follow the prompts to input the window size and retransmission timeout in milliseconds.

5. **Run the Receiver**:
   ```bash
   python ES22BTECH11006_receiverGBN.py
   ```
   - Ensure the receiver is running before starting the sender.

## Notes

- The sender implements the Go-Back-N protocol, allowing multiple packets to be sent before requiring an acknowledgment.
- Make sure your firewall settings allow UDP traffic on the specified ports.

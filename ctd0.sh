#!/bin/bash
# SYSTEM INFORMATION REPORT

# Display the current date and time
echo "Current Date and Time: $(date)"

# Display the system uptime
echo "System Uptime: $(uptime -p)"

# Display the currently logged-in users
echo "Logged-in Users:"
who

# Display the disk usage of the root filesystem
echo "Disk Usage of Root Filesystem:"
df -h /

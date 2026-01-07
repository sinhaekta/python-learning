# Conditional Statements: if, elif, else -> Condition evaluates to True or False
# DevOps Use Case: Environment checks, Status Validation, Access Control, Exit on Errors

disk_usage = 85  

if disk_usage > 90:
    print("Critical Alert: Disk usage is above 90%!")
elif disk_usage > 70:
    print("Warning: Disk usage is above 70%.")
else:
    print("Disk usage is within normal limits.")

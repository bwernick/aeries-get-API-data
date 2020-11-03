# aeries-get-API-data
Using Python and the Aeries API to get data.

## Usage
1. Download `data.py` and 

### All school codes and school names
```python3 data.py getSchools 0```

### Specfic School Information
```python3 data.py getSchools_SC <schoolCode>```

- Example: `python3 data.py getSchools_SC 994`

### School Bell Schedule
```python3 data.py getSchoolBellSchedule <schoolCode>```

- Example: `python3 data.py getSchoolBellSchedule 994`

### Student Info CSV file
```python3 data.py getStudentInfo_CSV <schoolCode>```

- Example: `python3 data.py getStudentInfo_CSV 994`

### Grade Level Student Info CSV file
```python3 data.py getStudentInfo_GL_CSV <schoolCode> <gradeLevel>```

- Example: `python3 data.py getStudentInfo_GL_CSV 994 9`

### Specfic Student Info
```python3 data.py getStudentInfo_SID <schoolCode> <studentID>```

- Example: `python3 data.py getStudentInfo_SID 994 99400001`



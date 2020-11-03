import requests, csv, json, argparse
from argparse import ArgumentParser

#base url to acess the Aeries API (default is the Aeries demo API)
baseURL = "https://demo.aeries.net/aeries/api/v5/schools/" 

#header for Aeries API
#place your Aeries cert here (this is not secure at all)
headers = {'content-type': 'application/json',
            "AERIES-CERT": "477abe9e7d27439681d62f4e0de1f5e1"
          }
path = []
        
#simple api call function        
def makeAPICall(url):
  return requests.get(url, headers=headers)

#Prints all school codes and school names
def getSchools():
  resp = makeAPICall(baseURL)
  data = resp.json()
  for entry in data:
    sc = entry["SchoolCode"]
    sn = entry["Name"]
    print(sc, ' - ', sn)

#displays information on a specfic school to the console
def getSchools_SC(schoolCode):
  schoolCode = args.schoolCode
  url = baseURL + str(schoolCode)
  resp = makeAPICall(url)
  data = resp.json()
  print(json.dumps(data, indent=4))

#displays the bell schedule on the console
def getSchoolBellSchedule(schoolCode):
  schoolCode = args.schoolCode
  url = baseURL + str(schoolCode) + "/BellSchedule"
  resp = makeAPICall(url)
  data = resp.json()
  print(json.dumps(data, indent=4))

#generates a CSV file of all student info from a specfic school
def getStudentInfo_CSV(schoolCode):
  schoolCode = args.schoolCode
  url = baseURL + str(schoolCode) + "/students"
  resp = makeAPICall(url)
  data = resp.json()
  linecount = -1

  #https://gist.github.com/mabroor/2828962
  f = open("students.csv", 'w')
  fieldnames = data[0].keys()
  csvwriter = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
  csvwriter.writerow(dict((fn, fn) for fn in fieldnames))
  for row in data:
      csvwriter.writerow(row)
      linecount += 1
  f.close() 
  print('Wrote ' + str(linecount) + ' students to "students.csv"')

#displays a specfic student's information on the console 
def getStudentInfo_SID(schoolCode, studentID):
  schoolCode = args.schoolCode
  studentID = args.studentID
  url = baseURL + str(schoolCode) + "/students/" + str(studentID) + "/extended"
  resp = makeAPICall(url)
  data = resp.json()
  print(json.dumps(data, indent=4))

#generates a CSV file of retrived student info from a specfic school in a specific grade level
def getStudentInfo_GL_CSV(schoolCode, gradeLevel):
  schoolCode = args.schoolCode
  gradeLevel = args.gradeLevel
  url = baseURL + str(schoolCode) + "/students/grade/" + str(gradeLevel) + "/extended"
  resp = makeAPICall(url)
  data = resp.json()
  linecount = -1

  #https://gist.github.com/mabroor/2828962
  f = open("students_grade_" + gradeLevel + ".csv", 'w')
  fieldnames = data[0].keys()
  csvwriter = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames)
  csvwriter.writerow(dict((fn, fn) for fn in fieldnames))
  for row in data:
      csvwriter.writerow(row)
      linecount += 1
  f.close() 
  print('Wrote ' + str(linecount) + ' students to "students_grade_' + gradeLevel + '.csv"')

#command line function calling achieved via argparse
#Reference: https://docs.python.org/3/library/argparse.html, https://stackoverflow.com/a/30669126, https://stackoverflow.com/a/24584876
parser = ArgumentParser()
parser.add_argument("function", 
                    nargs="?",
                    choices=['getSchools', 'getSchools_SC', 'getSchoolBellSchedule', 'getStudentInfo_CSV', 'getStudentInfo_SID', 'getStudentInfo_GL_CSV'],
                    default='getSchools',
                    )
args, sub_args = parser.parse_known_args()

# Manually handle the default for "function"
function = "getSchools" if args.function is None else args.function

# Parse the remaining args as per the selected subcommand
if function == "getSchools":
  getSchools()
elif function == "function2":
  parser.add_argument('schoolCode')
  args = parser.parse_args(sub_args)
  getSchools_SC(args.schoolCode)
elif function == "getSchoolBellSchedule":
  parser.add_argument('schoolCode')
  args = parser.parse_args(sub_args)
  getSchoolBellSchedule(args.schoolCode)
elif function == "getStudentInfo_CSV":
  parser.add_argument('schoolCode')
  args = parser.parse_args(sub_args)
  getStudentInfo_CSV(args.schoolCode)
elif function == "getStudentInfo_SID":
  parser.add_argument('schoolCode')
  parser.add_argument('studentID')
  args = parser.parse_args(sub_args)
  getStudentInfo_SID(args.schoolCode, args.studentID)
elif function == "getStudentInfo_GL_CSV":
  parser.add_argument('schoolCode')
  parser.add_argument('gradeLevel')
  args = parser.parse_args(sub_args)
  getStudentInfo_GL_CSV(args.schoolCode, args.gradeLevel)
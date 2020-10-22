import requests, csv, json, argparse

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
  schoolCode = args.studentID
  url = baseURL + str(schoolCode) + "/students/" + str(studentID) + "/extended"
  resp = makeAPICall(url)
  data = resp.json()
  print(json.dumps(data, indent=4))

#generates a CSV file of retrived student info from a specfic school in a specific grade level
def getStudentInfo_GL(schoolCode, gradeLevel):
  schoolCode = args.schoolCode
  schoolCode = args.gradeLevel
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
#Reference: https://docs.python.org/3/library/argparse.html, https://stackoverflow.com/a/30669126
p = argparse.ArgumentParser()
subparsers = p.add_subparsers()

#parser for getSchools_SC
getSchools_SC_parser = subparsers.add_parser('getSchools_SC')
getSchools_SC_parser.add_argument('schoolCode')
getSchools_SC_parser.set_defaults(func=getSchools_SC)

#parser for def getSchoolBellSchedule:
BellSchedule_parser = subparsers.add_parser('getSchoolBellSchedule')
BellSchedule_parser.add_argument('schoolCode')
BellSchedule_parser.set_defaults(func=getSchoolBellSchedule)

#parser for getStudentInfo_CSV
getStudentInfo_CSV_parser = subparsers.add_parser('getStudentInfo_CSV')
getStudentInfo_CSV_parser.add_argument('schoolCode')
getStudentInfo_CSV_parser.set_defaults(func=getStudentInfo_CSV)

#parser for getStudentInfo_SID
getStudentInfo_SID_parser = subparsers.add_parser('getStudentInfo_SID')
getStudentInfo_SID_parser.add_argument('schoolCode')
getStudentInfo_SID_parser.add_argument('studentID')
getStudentInfo_SID_parser.set_defaults(func=getStudentInfo_SID)

#parser for getStudentInfo_GL
getStudentInfo_GL_parser = subparsers.add_parser('getStudentInfo_GL')
getStudentInfo_GL_parser.add_argument('schoolCode')
getStudentInfo_GL_parser.add_argument('gradeLevel')
getStudentInfo_GL_parser.set_defaults(func=getStudentInfo_GL)

#do the parse
args = p.parse_args()
args.func(args)
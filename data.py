import requests
import csv

baseURL = "https://demo.aeries.net/aeries/api/v5/schools/" #base url to acess the aeries demo api
headers = {'content-type': 'application/json',
            "AERIES-CERT": "477abe9e7d27439681d62f4e0de1f5e1"
          }
path = []
        
#simple api call function        
def makeAPICall(url):
  return requests.get(url, headers=headers)

#Walks through json/dicts that include lists
#https://stackoverflow.com/a/54000999
def walk(d):
  global path
  for k,v in d.items():
    if isinstance(v, str) or isinstance(v, int) or isinstance(v, float):
        path.append(k)
        print("{} - {}".format(".".join(path), v)) 
        path.pop()
    elif v is None:
        path.append(k)
        # do something special
        path.pop()
    elif isinstance(v, list):
        path.append(k)
        for v_int in v:
          walk(v_int)
        path.pop()
    elif isinstance(v, dict):
        path.append(k)
        walk(v)
        path.pop()
    else:
        print("###Type {} not recognized: {}.{}={}".format(type(v), ".".join(path),k, v))

#Prints all school codes and school names
def getSchools():
  resp = makeAPICall(baseURL)
  data = resp.json()
  for entry in data:
    sc = entry["SchoolCode"]
    sn = entry["Name"]
    print(sc, ' - ', sn)

def getSchools_SC(schoolCode):
  url = baseURL + str(schoolCode)
  resp = makeAPICall(url)
  data = resp.json()
  walk(data)

def getSchoolBellSchedule(schoolCode):
  url = baseURL + str(schoolCode) + "/BellSchedule"
  resp = makeAPICall(url)
  data = resp.json()
  for entry in data:
    print(entry)

def getStudentInfo(schoolCode):
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

def getStudentInfo_SID(schoolCode, studentID):
  url = baseURL + str(schoolCode) + "/students" + str(studentID)

def getStudentInfo_GL(schoolCode, gradeLevel):
  url = baseURL + str(schoolCode) + "/students/grade/" + str(gradeLevel)

def getStudentInfo_NM(schoolCode, studentNumber):
  url = baseURL + str(schoolCode) + "/students/sn/" + str(studentNumber)

#main
if __name__ == "__main__":
  getStudentInfo("994")
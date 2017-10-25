




data = {
  "1":
    {
      "name": "rajiv lamba",
      "title": "sre director",
      "reports": [2,3]
    },
    "2":
    {
      "name": "ariel casas",
      "title": "sre manager",
      "reports": [5,6,7]
    },
    "3":
    {
      "name": "nina mushiana",
      "title": "sre manager",
      "reports": [8,9,10]
    },
    "5":
    {
      "name": "matt knecht",
      "title": "sre",
      "reports": []
    },
    "6":
    {
      "name": "ahmed sharif",
      "title": "sre",
      "reports": []
    }
    ,
    "7":
    {
      "name": "terry bates",
      "title": "sre",
      "reports": []
    },
    "8":
    {
      "name": "michael kehoe",
      "title": "sr sre",
      "reports": []
    },
    "9":
    {
      "name": "brian sherwin",
      "title": "sr sre",
      "reports": []
    },
    "10":
    {
      "name": "scott church",
      "title": "noc engineer",
      "reports": []
    }
}


def api(id):
  return data[id]


def print_emp(id):
  _print_emp(id, 0)


def _print_emp(id, spc):
  e_data = api(id)
  ind = "\t" * spc
  print ind + e_data["name"] + " - " + e_data["title"]
  for report in e_data["reports"]:
    _print_emp(str(report), spc+1)

print_emp("1")

from collections import deque

def print_emp_dfs(id):
  emp_list = deque()
  emp_list.append((id, 0))
  spc = 0
  while emp_list:
    curr, spc = emp_list.popleft()
    e_data = api(curr)
    ind = "\t" * spc
    print ind + e_data["name"] + " - " + e_data["title"]
    for reports in e_data["reports"]:
      emp_list.append((str(reports), spc + 1))
    # spc += 1

print_emp_dfs("1")


1  2  3  4  5  6  7  8
1  2  5  3  4  6  7  8    ----2
1  2  5  3  7  4  6  8    ----2
1  2  5  3  7  8  4  6    ----2

0  0  2 -1  2  2 -3 -2

1  2  5  3  7  8  6  4    ----1



1  2  5  3  7  8  6  4



1  2  5  3  7  8  6  4
0  0  2 -1  2  2 -1 -4


1  2  3  4  5
2  1  5  3  4
1 -1  2  -1 -1 







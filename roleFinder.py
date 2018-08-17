import sys
import json
import subprocess

class RoleBinding:
  def __init__(self):
    pass

  def __main__(self):
    pass

  def _loop(self,dataItemo):
    pass

  def findClusterRole(self):
    pass

  def findRole(self):
    pass



if __name__ == "__main__":
  data = {}
  #with open("./clusterrole.json") as jsonData:
  #with open("./clusterrole_one.json") as jsonData:
  #with open("./role.json") as jsonData:
  with open("./role_one.json") as jsonData:
    data = json.load(jsonData)

  if 'items' in data:
    print("loop")

  elif data['kind'] == "ClusterRoleBinding":
    print("cluster")

  elif data['kind'] == "RoleBinding":
    print("Role")
  

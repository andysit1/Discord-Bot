import pyexcel


#in progress...
class gymTracker:
  def __init__(self):
    self.backStat = []
    self.legStat = []
    self.chestStat = []

  def inputBack(self, list):
    self.backStat = list

  def inputLeg(self, list):
    self.legStat = list

  def inputChest(self, list):
    sheet = pyexcel.get_sheet(file_name="gym_activity_chest.xlsx")
    self.chestStat = list
    sheet.row += self.chestStat
    sheet.save_as("gym_activity_chest.xlsx")




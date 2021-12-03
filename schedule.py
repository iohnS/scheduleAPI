
class Schedule:

    def getAgenda(self, currentDate):
        from bs4 import BeautifulSoup
        import requests

        URL = "https://cloud.timeedit.net/lu/web/lth1/ri1X50gQ6560YfQQ95Z5971Y0Zy5007495Y67Q564.html"
        agenda = []
        htmlSource = requests.get(URL).text
        soup = BeautifulSoup(htmlSource, "lxml")

        currentBlock = soup.find('div', {"data-dates": f"{currentDate}"})
        if currentBlock is not None:
            courses = currentBlock.find_all("div", {"tabindex": "0"})
            blockTimes = currentBlock.find_all("div", {"class": "timeDiv"})

        # course1:
        #     course -> EITF123
        #     typeofecuter -> föResu
        #     room -> E:A
        #     class -> Digitalteknik
        #     stutentgroup -> D2
        #     lärare -> björn

            blockInfo = {0: "course",
                         1: "lectureType",
                         3: "room",
                         4: "class",
                         5: "studentgrupp",
                         6: "teacher",
                         7: "startTime",
                         8: "endTime"
                         }

            # Reads the block info for each of the classes
            courseNbr = 0

            for info in courses:
                courseNbr += 1
                blockDict = {}
                #agenda[f"course{courseNbr}"] = {}
                for i in [0, 1, 3, 4, 5, 6]:
                    for value in info.find_all("div", {"class": f"c col{i}"}):
                        blockDict[blockInfo[i]
                                  ] = value.string if value != None else ""
                end = True
                for times in blockTimes[courseNbr*2-2:courseNbr*2]:
                    if end:
                        blockDict[blockInfo[8]] = times.string
                        end = False
                    else:
                        blockDict[blockInfo[7]] = times.string
                        end = True
                blockDict["date"] = currentDate
                agenda.append(blockDict)
        return agenda

    def getToday(self, currentDate):
        agenda = {}
        agenda["agenda"] = self.getAgenda(currentDate)
        return agenda

    def getSchedule(self):
        from datetime import date, timedelta

        today = date.today()
        allDays = [today + timedelta(days=i) for i in range(0, 7)]
        schedules = {}
        blockList = []

        for day in allDays:
            currentDay = day.strftime("%Y%m%d")
            blockList.append(self.getAgenda(currentDay))

        schedules["schedule"] = blockList

        return schedules

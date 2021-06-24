def countMatches(items, ruleKey, ruleValue):
        total = 0
        for i in range(len(items)):
            if ruleKey == 'type':
                if items[i][0] == ruleValue:
                    total+=1
            elif ruleKey == 'color':
                if items[i][1] == ruleValue:
                    total+=1
            else:
                if items[i][2] == ruleValue:
                    total+=1
        return total

print(countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],"color", "silver"))
